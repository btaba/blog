---
layout: post
title:  "Recursive Context Managers"
date:   2018-05-15 00:00:00
categories: projects
tags: regular
comments: True
---

After several years as a Python user, I think I'm finally coming around to really appreciating the language. Whatever it lacks as a dynamically typed scripting language (granted there is now [mypy](http://mypy-lang.org)), it makes up for it with its ease of use and readability.

To illustrate what I mean, I'll use an example from a problem I had at work with context managers. But first, I'll describe what context managers are.

## WTF is a context manager?

A context manager is basically what allows you to use the `with` statement in Python. For example if you wanted to write to a file, you *could* do this:


```python
f = open('test.txt', 'w')
f.write('hey!')
f.close()

assert f.closed is True  # this is True!
```

We always have to use `open` and `close` on files anyways, so context managers offer a convenient syntax using the `with` statement instead:


```python
with open('test.txt', 'w') as f:
    f.write('hey')

assert f.closed is True  # this is also True!
```

The `with` statement will call `f.close()` for us automagically, so we just saved ourselves 1 line of code!

## But how does it work?

You are probably thinking, that's fine but I have no idea wtf is happening with the `with` thing. Well then, let's just re-implement it:

{% highlight python linenos %}
from contextlib import contextmanager

@contextmanager
def open_context_manager(name, mode):
    f = open(name, mode)
    yield f
    f.close()

with open_context_manager('test.txt', 'w') as f:
    f.write('hey!')

{% endhighlight %}

That might look scary, but it's not really. When you call `with open_context_manager` on line 9, the `open_context_manager(...)` function gets called on line 4 and gives you back the file handler `f` using the `yield` statement on line 6. Then it returns back to the code in the `with` block on line 10, and we write `'hey!'` to the file with `f.write('hey!')`. Once we leave the `with` block, we return back to the `open_context_manager(..)` function on line 7, which calls `f.close()`. That's it!

You could also implement a context manager with a `try` and `finally` statement:

```python

def open_context_manager(name, mode):
    try:
        f = open(name, mode)
        yield f
    finally:
        f.close()

with open_context_manager('test.txt', 'w') as f:
    f.write('hey!')
```

Try it out! It works the same way.


## So what was the problem?

The problem I had was that I needed to enter context managers all at the same time in a nested data structure. 

If we simply wanted to enter a lot of context managers at the same time, we could start off by doing something like this:

```python
with open('test1.txt', 'w') as f1,\
        open('test2.txt', 'w') as f2,\
        open('test3.txt', 'w') as f3:
    # do stuff here ...
    pass
```

But that isn't really usable is it? Let's say we had 100 files? I sure wouldn't want to type that all out.

It turns out that all you really need to implement a context manager in Python is to implement a class with an `__enter__` and `__exit__` method. `__enter__` gets called when `with` is invoked on the object, and `__exit__` gets called when you leave the `with` scope. 

So here is how to implement a context manager for opening and closing files using a class:

{% highlight python linenos %}

class Open:

    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __enter__(self):
        self.f = open(self.name, self.mode)
        return self.f

    def __exit__(self, *exc):
        self.f.close()

with Open('test.txt', 'w') as f:
    f.write('hey!')

{% endhighlight %}

It works the same way as before. `__enter__` gets called when `with Open(...)` happens, and `__exit__` gets called when you leave the `with` scope.

You might be wondering what the `*exc` is on line 11? It's basically a list of required arguments for any `__exit__` magic method, which get passed around so that you can handle exceptions gracefully. The arguments for `*exc` are `exception_type`, `exception_value`, and `traceback` respectively.

So how can we leverage what we just did to enter multiple context managers at the same time? It becomes kind of simple really. Let's say we had files in a list, we could implement the following context manager:


{% highlight python linenos %}

class OpenFileList:

    def __init__(self, file_list, mode):
        self.file_list = file_list
        self.mode = mode

    def __enter__(self):
        self.fs = [open(f, self.mode) for f in self.file_list]
        return self.fs

    def __exit__(self, *exc):
        [f.close() for f in self.fs]

{% endhighlight %}

Boom! All we had to do was open files in a list on line 8, and then close them on line 12.

And now to use it:

```python

with OpenFileList(['test.txt', 'test2.txt', 'test3.txt'], 'w') as fs:
    for f in fs:
        f.write('hey!')

with OpenFileList(['test.txt', 'test2.txt', 'test3.txt'], 'r') as fs:
    for f in fs:
        print(f.read())

```

It's that easy!

## Back to the original problem!

Unfortunately that doesn't solve the original problem. I had multiple objects in a nested data structure made of lists and dicts. To solve the problem, we need to traverse the data strucutre and enter all nested contexts, then exit them later.

First we need a few useful functions:

1. Call a method on an object programmatically, so that we can do `_apply_method(target, 'open', mode='r')` instead of `target.open('r')`:

    ```python
    from operator import methodcaller

    def _apply_method(f, method, *args, **kwargs):

        m = methodcaller(method, *args, **kwargs)

        if hasattr(f, method):
            return m(f)

        return f
    ```

2. We need to apply the method recursively so that we can enter/exit all nested context managers. Here we apply it recursively on nested `dict`s and `list`s:


    ```python

    def _recursive_apply_method(f, method, *args, **kwargs):

        if isinstance(f, dict):
            return {k: _recursive_apply_method(v, method, *args, **kwargs)
                    for k, v in f.items()}
        elif isinstance(f, list):
            return [_recursive_apply_method(v, method, *args, **kwargs)
                    for v in f]

        return _apply_method(f, method, *args, **kwargs)

    ```

Using these two useful functions, we can now enter multiple nested contexts using a single context manager!

{% highlight python linenos %}

class recursive_file_context_manager(object):

    def __init__(self, files):
        self.files = files

    def __enter__(self):
        self.contexts = _recursive_apply_method(self.files, 'open', mode=self.mode)
        self.files = _recursive_apply_method(self.contexts, '__enter__')

        return self.files

    def __exit__(self, *exc):
        _recursive_apply_method(self.contexts, '__exit__', *exc)


class Read(recursive_file_context_manager):

    mode = 'r'


class Write(recursive_file_context_manager):

    mode = 'w'

{% endhighlight %}

We open all the file objects on line 7 by applying `'open'` to each nested object. Then we enter the contexts we got back on line 8 by calling `__enter__` on them. Finally, we exit the contexts on line 13 by calling `__exit__` on all the nested contexts. 

Sweet that wasn't too bad. Now we could have some files in a nested structure like so:

```python

from pathlib import Path

files = {
    'hey': Path('test1.txt'),
    'list': [Path('test2.txt'), Path('test3.txt')]
}

```

And we can enter all of them easily like this:

```python

with Write(files) as fobj:
    fobj['hey'].write('yo!')
    fobj['list'][0].write('yo1!')
    fobj['list'][1].write('yo1!')

assert fobj['hey'].closed is True  # yay!
```


And that works fine! So yeah, Python can be pretty neat sometimes.
