---
layout: post
title:  "MLE Interviews"
date:   2020-01-10 00:00:00
categories: projects
tags: projects
comments: True
---

About this time last year, I was studying for Machine Learning Engineer (MLE) interviews for large tech companies. I received offers from Google, Facebook, Magic Leap, Twitter, Airbnb, Etsy, and Wework. I got rejections after 3 onsites (Stripe, Two Sigma, and a startup) and several other phone screens (Pinterest, NVIDIA, OpenAI, MIRI, etc).

Looking back, I don't recommend, nor do I think it is worth, applying to a majority of these large tech companies (ask me about this in private). Nevertheless, I wanted to post a blueprint for how to do it...for posterity.

If you want to cut to the chase, here are the most important links in this article:

* [Michael Nielsen's article about Anki](http://augmentingcognition.com/ltm.html). If you want to learn anything, I can't recommend Anki enough. This is arguably the most valuable tool I acquired during this time.
* [Algorithmic Study Notes]({{ site.url }}/algorithm-data-structure-notes/)
* [ML Design Study Notes]({{ site.url }}/ml-design-notes/)
* [System Design Study Notes]({{ site.url }}/system-design-notes/)

## What is an MLE interview

An MLE interview is mainly comprised of three types of questions:

1. Algorithmic
2. System Design
3. ML Design

Each one can be prepared for separately. I'll go through them in order.

## Algorithmic

The classic algorithmic coding question will be asked at almost any tech company for software roles. There are several ways to prepare: [1] understand core concepts, [2] solve problems, and [3] do mock interviews. Do all of the above.

### Understand Core Concepts

Learn [these core concepts]({{ site.url }}/algorithm-data-structure-notes/) and supplement what you don't understand with a textbook.

I went a bit overkill this time; for kicks I read Skiena's [Algorithm Design Manual](http://www.algorist.com/) cover to cover. While I think the book is not the most comprehensive, the informal way Skiena writes is refreshing. My favorite chapters were on Combinatorial Search and Dynamic Programming, providing the most intuitive explanations I've seen on these topics. Reading an entire textbook is not required however :).

### Solving Problems

Apart from understanding the core algorithmic concepts, it is imperative to practice. The canonical platform for coding problems is of course [Leetcode](https://leetcode.com/). I did 2-3 problems every day and took place in competitions on Saturdays to see how I ranked over time.

Practicing coding problems can be a tricky endeavor. You really have to approach these methodically in order to really get the most out of your time. Here are some general guidelines:

1. Think of the solution or write pseudo code before actually coding up the solution. If you can't conceptually understand the solution, there isn't much point in writing real code.
2. Timing is key. If you can't think of the solution after 20-30m, look at the answer briefly and mark the question for re-review.
3. Coding the solution should take 5-10m. If it takes longer, then look at the solution and mark the question for re-review.
4. Occassionally redo all questions you did previously, especially the ones you had trouble with.
5. Try to balance easy, medium, and hard questions for each study session so that you are challenged, yet also remain confident with your progress.
6. Do problems regularly, say 4-5 times a week.
7. If there is an important concept you don't understand, spend all the time you need to really understand it. But do it during a time specifically allocated for studying concepts. You should be timing yourself quite strictly when doing coding problems.

Some traps to avoid:

1. Don't start trying to fix your test cases one-by-one. This is a trap. Coding interviews are not like this. Take a step back and think about the correctness of your solution. If it is mostly right, think of edge cases. If the test cases are just not realistic to solve in 45m, just skip the question altogether after understanding the gist.
2. Do not start coding unless you think of the solution first...

Oh and remember to have fun! Solving coding problems makes you sharper in general and that's not a bad thing.

### Mock Interviews

Later on, I started doing mock interviews with a friend, which helped me talk through the problems out loud while solving them on paper. Thinking out loud is a skill that needs to be acquired.

Ask a friend to pick a problem completely at random, and then solve it on the spot. Then ask not only for technical feedback, but also qualitative feedback. Soft skills are super important to make sure the interviewer understands your thought process and feels like they would want to work with you.

Here is a guideline for taking an interview in general:

1. Before coding, think of the solution and explain your thought process clearly.
2. State your assumptions and clarify (e.g. I'm assuming the input is clean so I can move on, or I'm assuming I have this function available to me).
3. Remember to state the runtime and space complexity.
4. State the edge cases and describe tests that you would write.

Mock interviews are about getting feedback, improving, and staying humble.

## System Design

Arguably, the best way to prepare for the system design interview is to acquire real life experience. That's sort of why these questions are asked to begin with.

I was lucky enough to shadow real interviews at my current company. I also did mock interviews with several co-workers and had worked quite a bit on ML systems, pipelines, and deployment strategies.

Nevertheless, system design interviews can still be prepared for thoroughly, especially through mock interviews. That's why I'd be happy to mock interview anyone that pings me :).

There are a couple of sources you can read to understand the core concepts: the [system-design-primer](https://github.com/donnemartin/system-design-primer) and [Grokking the System Design Interview](https://www.educative.io/courses/grokking-the-system-design-interview). I couldn't find anything better unfortunately, but I also compiled a short list of core concepts [here]({{ site.url }}/system-design-notes/) that might be helpful.


## ML Design

The ML design is the most ambigious interview because ML is an extremely broad subject. I was lucky enough to have conducted several ML Design interviews at my company. To make sure I wasn't caught by suprise, I made over [100 Anki]({{ site.url }}/ml-design-notes/) cards about core ML concepts.

I found this [paper](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45530.pdf) to contain essential knowledge to answer any search/ranking/recsys question in an efficient manner.

I still use Anki daily and I highly recommend it.

## There you have it.

The skeleton for passing an MLE interview can be found above. I don't recommend anyone spend their time studying any of it; but if you fall into the trap, then this is a good blueprint for what some call "success."

Don't be surprised if the best thing you get out of studying is falling in love with Anki. :D
