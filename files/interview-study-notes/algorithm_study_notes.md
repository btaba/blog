---
layout: page
title: Algorithm & Data Structure Notes
permalink: /algorithm-data-structure-notes/
---


Use these notes to brush up on core CS concepts. Please let me know if you find any errors.

<div id="toc"></div>

## Big O

Take a functions f(n) and g(n) defined for real valued numbers n. $f(n) = O(g(n))$ iff as $n \rightarrow \inf, |f(n)| \leq c g(n)$ for real-valued constants c. That is f(n) is at most some constant times g(n) for large values of n. 
f(n) could be the number of operations needed to solve a problem of length n. g(n) would be an upper bound on that problem times some constant.

$$
n! \gg c^n \gg n^3 \gg n^2 \gg n^{1 + \epsilon} \gg n\text{log}(n) \gg  n \\ \gg \sqrt{n} \gg \text{log}^2(n) \gg \text{log}(n) \gg \frac{\text{log}(n)}{\text{log}\text{log}(n)} \gg \text{log}\text{log}(n) \gg 1
$$

## Linked Lists

Linked lists are a linear collection of elements that are stored based on the memory reference of each element to the next element.

Cons: Fast access, such as random access is O(N). 

Pros: Insertion and deletion is O(1) if you have the location of the element you want to insert/delete after.

```
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
```


## Stacks

Support two principle ops, push and pop. Can be implemented with a singly linked list or dynamic array. Stacks are last in first out (LIFO).

```
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.past = None


class LIFOStack:
    def __init__(self):
        self.head = None

    def push(self, val):
        n = Node(val)
        if not self.head:
            self.head = n
        else:
            self.head.next = n
            n.past = self.head
            self.head = n

    def pop(self):
        if not self.head:
            raise Exception('empty')
        r = self.head.val
        self.head = self.head.past
        return r

l = LIFOStack()
l.push(1); l.push(2); l.push(3)
assert l.pop() == 3
assert l.pop() == 2
assert l.pop() == 1
```

## Queues

Queues are first in first out (FIFO), like a line at a shopping store. 

```
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.past = None


class FIFOQueue:
    def __init__(self):
        self.tail = None
        self.head = None

    def enqueue(self, val):
        n = Node(val)
        if not self.head:
            self.head = n
            self.tail = self.head
        else:
            self.tail.next = n
            self.tail = self.tail.next

    def dequeue(self):
        if not self.head:
            raise Exception('empty')

        r = self.head.val
        self.head = self.head.next
        return r


q = FIFOQueue()
q.enqueue(1)
assert q.dequeue() == 1
q.enqueue(1); q.enqueue(3); q.enqueue(5)
assert q.dequeue() == 1
assert q.dequeue() == 3
assert q.dequeue() == 5
```

## Deque

Doubled ended queue or a doubly linked list.

```
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_left(self, val):
        x = Node(val)
        if not self.head:
            self.head = x   
            self.tail = self.head
        else:
            x.next = self.head
            self.head.prev = x
            self.head = x   

            
    def insert_right(self, val):
        x = Node(val)
        if not self.tail:
            self.tail = x
            self.head = self.tail
        else:
            self.tail.next = x
            x.prev = self.tail
            self.tail = x


    def pop_left(self):
        if not self.head:
            raise Exception("empty ll")
        res = self.head.val
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return res
    
    def pop_right(self):
        if not self.tail:
            raise Exception("empty ll")
        res = self.tail.val
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return res
    
    def search(self, val):
        current = self.head
        while current:
            if current.val == val:
                return current
            current = current.next
                
        
    def pp(self):
        ll = []
        current = self.head
        while current:
            ll.append(current.val)
            current = current.next
        print(ll)
    
    def delete(self, node):
        prev_node = node.prev
        next_node = node.next
        if prev_node:
            prev_node.next = next_node
        else:
            self.head = next_node
        if next_node:
            next_node.prev = prev_node
        else:
            self.tail = prev_node

d = Deque()
d.insert_left(4)
assert d.pop_right() == 4 
d.insert_right(5)
assert d.pop_left() == 5
d.insert_left(44)
assert d.pop_left() == 44
d.insert_right(2)
assert d.pop_right() == 2

d.insert_right(5)
d.insert_right(6)
assert d.search(5) == d.head
assert d.search(6) == d.tail

d.delete(d.search(6))
assert d.search(5) == d.tail 
```

## Vectors / ArrayLists

These are fixed blocks in memory that support O(1) indexing. O(1) amortized insert/delete at end (since we might need to resize array), O(N) insert/delete at beginning.


## Merge Sort

Keep splitting the array, and recursively sort arrays to the left and to the right. Then merge the left and right arrays.

```
import numpy as np


def merge_sort(arr):
    N = len(arr)
    if N == 1:
        return arr
    mid = N // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    left_idx, right_idx, idx = 0, 0, 0
    merged = []
    while idx < N:
        if left_idx >= len(left):
            merged.append(right[right_idx])
            right_idx += 1
        elif right_idx >= len(right):
            merged.append(left[left_idx])
            left_idx += 1
        elif left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

        idx += 1

    return merged


for _ in range(10):
    arr = np.random.random(100)
    assert list(sorted(arr)) == merge_sort(arr)
```

## Quicksort

Partition elements recursively. O(N * lg(N)) amortized, and O(N^2) worst-case.

```
def quick_sort(arr):

    def _qsort(arr, left, right):
        if left >= right:
            return

        oleft, oright = left, right
        # partition the leftmost element
        p = left
        left += 1
        while left <= right:
            if arr[left] < arr[p]:
                # swap left and p
                tmp = arr[left]
                arr[left] = arr[p]
                arr[p] = tmp
                p = left
                left += 1
            elif arr[left] > arr[right]:
                # swap left and right
                tmp = arr[right]
                arr[right] = arr[left]
                arr[left] = tmp
                right -= 1
            else:
                right -= 1

        _qsort(arr, p+1, oright)
        _qsort(arr, oleft, p-1)

    arr = list(arr)
    _qsort(arr, 0, len(arr)-1)
    return arr

for _ in range(10):
    arr = np.random.random(100)
    assert list(sorted(arr)) == quick_sort(arr)
```

The partition can be done more easily if we copy into a new array (more inefficient memory wise).

```
def partition(array, partition_idx):
    p = array[idx]

    left, mid, right = [], [], []
    for v in array:
        if v < p:
            left.append(v)
        elif v == p:
            mid.append(v)
        else:
            right.append(v)

    return left + mid + right
```

The more memory efficient partition keeps a left and right pointer for the left and right arrays, and a pointer for the partitioned element.

## Binary Search

Once the array is sorted, binary search is O(lg(N))

```
def binary_search(arr, target):

    arr.sort()

    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return arr[left] == target


assert binary_search([0, 5, 9], 0) is True
assert binary_search([0, 5, 9], 5) is True
assert binary_search([0, 5, 9], 9) is True
assert binary_search([0, 5, 9], -1) is False
assert binary_search([0, 5, 9], 1) is False
assert binary_search([0, 5, 9], 6) is False
assert binary_search([0, 5, 9], 10) is False
```

## Hash Tables

Hash tables support O(1) amortized lookups, inserts and deletes, with O(N) in the worts-case. Keys are hashed and mapped to a location in memory. Collisions can be avoided with chaining each slot in the hash table (using a linked list), or using open addressing (double hashing if we find a collision). Perfect hashing means that performance is O(1) in the worst-case and we have no collisions; this can only be done if all the keys are known beforehand.

When an insert is made, we may need to resize the hash table to accomodate the extra values. The simplest way is to copy all entries to the new hash table in O(N). We could also create two tables and check both, slowly moving old keys to the new table.

### Hash Functions:

A good hash function will hash each key with equal likelihood for the m slots available. If the distribution of keys is a uniform integer k, the simplest hash is to do k mod m. In practice we use random hash functions that are independent of the keys stored (universal hashing) to avoid malicious attacks.

## Bloom Filters

Bloom filters efficiently represent "sets" of elements. The false-negative rate is 0 and the false-positive rate is non-zero. In other words, a set-miss occurs with absolute certainty, but a set-hit has a non-zero probability of being wrong.

Bloom filters are implemented as an array of m bits, initially set to 0. There are also k different hash functions defined, where k < m. To add an element, we feed it to k hash functions, and set bits in the k array positions to 1. To query an element, we feed it to k hash functions, and check if all k array positions are set to 1. If at least 1 array element is 0, we know with absolute certainty that the element does not exist in the set. If all positions are 1, we know with some probability that the element is in the set. As the number of elements grows in the array, the false-positive rate increases.

Bloom filters are memory efficient since they don't store hashes directly, just bits and booleans.

## Heap

A heap is a binary tree that maintains the heap property, which states that for any node, all its children must be less/greater than that node. Min/Max heaps are used as priority queues. They are implemented with arrays:

```
class MinHeap:

    def __init__(self):
        self.a = []

    def insert(self, val):
        self.a.append(val)
        # bubble up the value
        idx = len(self.a) - 1
        while idx > 0:
            parent = (idx-1) // 2
            if self.a[parent] > self.a[idx]:
                # swap elements
                tmp = self.a[idx]
                self.a[idx] = self.a[parent]
                self.a[parent] = tmp
            idx = parent

    def _min_child(self, i):
        if i * 2 + 2 > len(self.a) - 1:
            return i*2 + 1

        if self.a[i*2 + 1] < self.a[i*2 + 2]:
            return i*2+1
        return i*2+2

    def pop(self):
        # swap first element with last
        # then bubble down the first element
        if len(self.a) == 0:
            raise Exception('empty')

        answer = tmp = self.a[0]
        self.a[0] = self.a[len(self.a)-1]
        del self.a[len(self.a)-1]

        # bubble down
        idx = 0
        while idx < len(self.a):
            child = self._min_child(idx)

            if child > len(self.a) - 1:
                break

            if self.a[idx] > self.a[child]:
                tmp = self.a[idx]
                self.a[idx] = self.a[child]
                self.a[child] = tmp
            idx = child

        return answer
```

The runtime is O(lgN) for insert and pop in the worst case.

## Binary Search Trees

Binary Search Trees are binary trees with the search-tree property (a node to the left is <= the current node, and a node to the right is >= the current node).
Order traversals are O(N). In Order: Retrieve elements in sorted order. We recursively go left, then process the root item, then recursively go right.

```
def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root.val)
    in_order(root.right)
```

Pre-Order: The process item occurs before we search left.

```
def pre_order(root):
    if root is None:
        return
    print(root.val)
    pre_order(root.left)
    pre_order(root.right)
```

Post-Order: The process item occurs after we search right.

```
def post_order(root):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.val)
```

### Search

Search is O(h) where h=lgN for a balanced tree

```
def search(root, val):
    while root.val != val and root:
        if val < root.val:
            root = root.left
        else:
            root = root.right
    return root

def search_recursive(root, val):
    if not root or root.val == val:
        return root
    if val < root.val:
        return search_recursive(root.left, val)
    return search_recursive(root.right, val)
```

### Min/Max

The minimum is the left-most element and the maximum is the right-most element in the tree, both done in O(h) time.

### Successor/Predecessor

Getting the successor can also be done in O(h) time. If there is a right node, get the min element to the right of node x. Otherwise get the first parent who's left child is an ancestor of node x (first parent that is greater).

```
def successor(node):
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    parent = node.parent
    while parent and parent.right == node:
        node = parent
        parent = node.parent
    return parent if parent and parent.val > node.val else None
```

Predecessor is symmetrical to successor:

```
def predecessor(node):
    if node.left:
        node = node.left
        while node.right:
            node = node.right
        return node
    parent = node.parent
    while parent and parent.left == node:
        node = parent
        parent = node.parent
    return parent if parent and parent.val < node.val else None
```

### Insertion

Insertions are O(h) where h is the height of the tree. A balanced search tree has height O(lgN).

```
def insert(tree, node):
    parent = None
    x = tree.root
    while x:
        parent = x
        if node.val < x.val:
            x = x.left
        else:
            x = x.right
            
    node.parent = parent
    if parent is None:
        tree.root = node
    elif node.val < parent.val:
        parent.left = node
    else:
        parent.right = node
```

### Deletion

For deletion of a node z, there are a few cases. If z has no left child then we can replace z with its right child. If there is no right node,  we can replace z with its left child. If there are both left and right nodes and z's right node has no left child, then we can replace z with z's right node. If there are both left and right nodes, then we must first promote the successor of the right node as z's right node, then replace z with this node.

```
def transplant(T, u, v):
    # replace tree rooted at u with v in the tree T
    if u.p is None:
        T.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    if not v:
        v.p = u.p

def delete(T, z):
    if z.left is None:
        transplant(T, z, z.right)
    elif z.right is None:
        transplant(T, z, z.left)
    else:
        y = minimum(z.right)  # inorder successor
        if y.p != z:
            transplant(T, y, y.right)
            y.right = z.right
            y.right.p = y
        transplant(T, z, y)
        y.left = z.left
        y.left.p = y
```

For a randomly created BST, the average depth of the tree is O(h).

## Balanced Search Trees

A balanced tree has height lg(N), guaranteeing the above operations to run in O(lgN) time.

### Red black tree

Each node of a red-black tree has extra information, its color (either red or black). A tree is balanced (with height lgN) if it satisfies the red-black property:

* Every node is either red or black
* The root is black
* Every NIL leaf is black
* If a node is red, then both its children are black
* For each node, all simple paths from the node to descendant leaves contain the same number of black nodes.

We just need to mofidy insert and delete in O(lgN) to preserve the red-black property. We do this using rotations (left and right) which preserve the binary tree property.

```
def rotate_left(T, x):
    y = x.right
    x.right = y.left
    if y.left:
        y.left.p = x
    y.p = x.p
    if x.p is None:
        T.root = y
    elif x == x.p.left:
        x.p.left = y
    else:
        x.p.right = y
    y.left = x
    x.p = y
```

To insert a node onto a red-black tree, we insert the node as before and color it red. All instances of NIL leafs are replaced with T.NIL (in order to maintain the proper tree structure). To preserve the red-black property, we call another method to fix the tree.

If the parent of the new node is black, then done. If parent is red, and the parent and parent's sibling are both red, recolor and walk two nodes up the tree. If the parent's sibling is black or absent, we have 4 cases to deal with LL, LR, RR, RL (R=right, L=left). For each case we need to do 1-2 rotations. LL->R, RL->LR, RR->L, LR->RL.

### AVL tree

An AVL tree is height balanced, meaning that for every node x, the left and right subtrees have height that differ by at most 1. We need to have an extra attribute at each node, its height. To insert, we place a node and then balance the tree.

The balance factor is the difference of the height from the left and right nodes. An AVL tree is balanced if the balance factor is in [-1, 0, 1]. Here is a [link](https://bradfieldcs.com/algos/trees/avl-trees/) to the rebalancing algo, which is similar to Red-black trees. [Here](https://www.geeksforgeeks.org/avl-tree-set-1-insertion/) is another implementation copied below:

```
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
  

class AVL_Tree(object):
  
    def insert(self, root, key):
      
        # Step 1 - Perform normal BST
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
  
        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
  
        # Step 3 - Get the balance factor
        balance = self.getBalance(root)
  
        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
            
        # Case 3 - Left Right
        if balance > 1 and key >= root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
            
        # Case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
            
        # Case 2 - Right Right
        if balance < -1 and key >= root.right.val:
            return self.leftRotate(root)
        return root
  
    def leftRotate(self, z):
  
        y = z.right
        T2 = y.left
  
        # Perform rotation
        y.left = z
        z.right = T2
  
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
  
        # Return the new root
        return y
  
    def rightRotate(self, z):
  
        y = z.left
        T3 = y.right
  
        # Perform rotation
        y.right = z
        z.left = T3
  
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
  
        # Return the new root
        return y
  
    def getHeight(self, root):
        if not root:
            return 0
  
        return root.height
  
    def getBalance(self, root):
        if not root:
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right)
  
    def preOrder(self, root):
  
        if not root:
            return

        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)
```

## Union Find

Union find supports two operations. Union - merge two connected components. Find - do vertices v1 and v2 exist in the same component. Most algorithms can do one of the operations in constant time and the other in linear time.

Quick-find does a union in O(N) by changing the parent of all nodes affected in the union. Find is an O(1) operation with an array-lookup.

```
class QuickFind:
    def __init__(self):
        self.parent = {}

    def find(self, i):
        if i not in self.parent:
            self.parent[i] = i

        return self.parent[i]

    def union(self, p, q):
        pid, qid = self.find(p), self.find(q)
        for p in self.parent:
            if self.parent[p] == pid:
                self.parent[p] = qid


qf = QuickFind()
qf.find('A')
qf.union('A', 'B')
qf.union('C', 'D')
qf.union('A', 'D')
print(qf.parent)
```

Quick-union solves the problem with a tree. The problem with the tree is that it can get tall, and the runtimes are thus O(N) for both find and union.

```
class QuickUnion:
    def __init__(self):
        self.parent = {}

    def find(self, i):
        # find the root of the set for element i
        if i not in self.parent:
            self.parent[i] = i
            return i

        while i != self.parent[i]:
            i = self.parent[i]
        return i

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        self.parent[i] = j


qu = QuickUnion()
qu.find('A')
qu.union('A', 'C')
qu.find('C')
```

We can improve quick-union by doing a union by making the root of the smaller tree point to the root of the larger tree (critical for reducing depth of tree), which is O(h) to find the root of the trees of both components. Find is done by finding the root of both trees which is also O(h), where h = lg(N) for a balanced tree. There are better implementations outlined in this [link](https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf).

Weighted Quick-Union is O(lgN) for both find and union. Find is identical to Quick-Union, and the union checks which tree is smaller to join to the larger tree.

```
class WeightedQuickUnion:
    def __init__(self):
        self.parent, self.rank = {}, {}

    def find(self, i):
        if i not in self.parent:
            self.parent[i] = i
            self.rank[i] = 1
            return i

        while i != self.parent[i]:
            i = self.parent[i]
        return i

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)

        if self.rank[i] < self.rank[j]:
            self.parent[i] = j
            self.rank[j] += self.rank[i]
        else:
            self.parent[j] = i
            self.rank[i] += self.rank[j]
```

## Tries

Tries are suitable for looking up strings or bits. Each string is stored in a prefix tree structure. Searching and inserting is O(S) where S is the length of the string. Also called a prefix/radix tree, since each successive node creates a string lexicographically greater than strings above in the tree. 

```
class Trie:
    def __init__(self):
        self.t = {}

    def __repr__(self):
        return str(self.t)

    def insert(self, word):
        t = self.t
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t['#'] = '#'  # end of word

    def search(self, word):
        t = self.t
        for w in word:
            if w not in t:
                return False
            t = t[w]

        return t.get('#') == '#'

    def search_prefix(self, pre):
        t = self.t
        for w in pre:
            if w not in t:
                return False
            t = t[w]
        return True
```

## Range Sum - Binary Index Tree

In order to quickly caluclate the range sum in an array, we can compute a cummulative sum array. The range sum from i to j in cumsum[j] - cumsum[i], computed in O(1) time. However, if we want to update the original array, we need to update the cumsum in O(N) time. Likewise, if we want quick updates in O(1) time, the range sum query takes O(N) to compute.

We can also use binary index trees to efficiently calculate range sum and do updates in O(lg(N)) time. The binary index tree has nodes that contain the cummulative sum of that node and all nodes in its left subtree. To get the sum for a leaf, we find the leaf; every time we go right, we add that value to a counter. To do an update, we also find the leaf to update; every time we follow a left link back up to the root, we update the value of that node.

The binary index tree cleverly uses an array with binary indexing to traverse the tree structure. To go up a left link, we subtract the right-most 1 bit (used for summing). To go up a right link, we add the right-most 1 bit (used for updating).

```
class BinaryIndexTree:
    def __init__(self, size):
        self.binary_index_tree = [0] * (size + 1)
        self.n = size

    def update(self, value, pos):
        pos += 1
        while(pos < self.n + 1):
            self.binary_index_tree[pos] += value
            pos += pos & (-pos)  # go up the next right link
    
    def _get_sum(self, pos):
        pos += 1
        _sum = 0
        while(pos > 0):
            _sum += self.binary_index_tree[pos]
            pos -= pos & (-pos)  # go up the next left link
        return _sum
    
    def get_sum(self, begin, end):
        begin -= 1
        _sum2 = self._get_sum(end)
        if begin >= 0:
            _sum1 = self._get_sum(begin)
            return _sum2 - _sum1
        return _sum2
```

## Graphs

### Graph representations

Adjacency List: is a dictionary of all the nodes, and for each node key, a list of the nodes that it connects to. These efficiently represent sparse graphs. Space is O(V + E), adding a vertex and edge is O(1), deleting a vertex is O(E) and deleting an edge is O(V).

Adjacency Matrix: A VxV matrix with a boolean value saying if there is an edge between two vertices. Preferred if graphs are dense. Space is O(V^2), adding/deleting a vertex is O(V^2), adding/removing an edge is O(1). 

Nodes and pointers.

## BFS

Breadth first search searches a graph by fanning out and adding elements to a FIFO queue to search next. We also keep track of which nodes we visited in a set. BFS is easiest when implemented iteratively. This takes O(V) in memory and O(V+E) in time.

```
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': [],
    'D': ['E', 'F'],
    'E': [],
    'F': [],
    'G': ['A'],
    'H': []
}

from collections import deque


def bfs(graph, node):

    q = deque([node])  # FIFO queue
    visited = set([])

    while q:
        n = q.popleft()
        if n not in visited:
            visited.add(n)

            for neighbor in graph[n]:
                q.append(neighbor)

    return visited
```

"Because vertices are discovered in order of increasing distance from the root, this [BFS] tree has a very important property. The unique tree path from the root to each node x ∈ V uses the smallest number of edges (or equivalently, intermediate nodes) possible on any root-to-x path in the graph."

Finding the shortest path from a start node to an end node in an undirected, graph amounts to using a BFS. To keep track of the path, we just need to store the parent of every node, and backtrack from the end to the start to store the path.

## DFS

Depth first search uses a LIFO queue to visit nodes, and thus searches for depth first. A recursive solution is easiest to implement here. This takes O(v) in memory and O(V+E) in time.

```
def dfs(graph, node, visited=set()):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

def dfs_iterative(graph, node):
    visited = set()
    stack = [node]

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            for n in graph[v]:
                stack.append(n)
    return visited
```

## Cycle Detection

In an **undirected** graph, use DFS to detect cycles! It's sufficient to find a back-edge during a DFS to conclude that there is a cycle in an undirected graph. This runs in O(E + V) time.

```
def dfs_undirected_cycle(graph):
    visited = set()

    def dfs(node, p):

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor in visited and neighbor != p:
                # we have a neighbor that we already visited that
                # isn't the preceding node we just came from
                return True
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
        return False

    for n in graph:
        if n not in visited and dfs(n, None):
            return True

    return False
```

In a **directed** graph, we have a directed loop if there are back-edges to ancestors that we visited in our current function call stack for DFS. We need to keep track of which nodes we are currently visiting, whereas before we just needed to keep track of which nodes we ever visited. A DAG can have two edges pointing to the same node, but not resulting in a cycle. Also O(E + V).

```
def directed_cycle(graph):
    visited = set()
    processing = set()

    def dfs(node):
        visited.add(node)
        processing.add(node)

        for n in graph[node]:
            if n not in visited:
                if dfs(n):
                    return True
            elif n in processing:
                # we visited a node that is currently being processed
                # so there is a cycle
                print(node, '->', n)
                return True

        processing.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False
```

## Connectivity

In an undirected graph, the graph is connected if every pair of vertices is connected. Parts of a graph that are connected are called connected components. O(E+V)

```
def connected_components(graph):

    count = 0
    connected_components = {}

    def dfs(node, visited=set()):
        visited.add(node)
        for n in graph[node]:
            if n not in visited:
                dfs(n, visited)
        return visited

    for node in graph:
        if node not in connected_components:
            results = dfs(node, set())
            for r in results:
                connected_components[r] = count
            count += 1

    return connected_components
```

A directed graph is weakly connected if the graph without the direction results in a connected undirected graph. It is strongly connected if there are directed paths to all pairs of vertices (i.e. there is a directed cycle).

## Topological Sorting

Every DAG has a topological sort. We do a DFS and order the nodes in the reverse order that they are marked as processed. O(V+E)

```
def topological_sort(graph):
    order, processing, visited = [], set(), set()

    def dfs(node):
        processing.add(node)
        visited.add(node)

        for n in graph[node]:
            
            if n in processing:
                raise ValueError('cycle', node, '->', n)
            elif n not in visited:
                dfs(n)
        processing.remove(node)
        order.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return order[::-1]
```

## Shortest Path

In an edge-weighted graph, the shortest path between a vertex and any other vertex, is the path with the smallest sum of edge weights.

## Djikstra

Finds the single destination shortest path, assuming no negative edge weights. Djiktsra is a greedy algorithm, that repeatedly picks the minimum distance vertex to the source and relaxes its neighbors (similar to Prim's algo). It runs in O(V^2) time if we get the minimum in O(V) time.  If we use a min-heap to get the minimum, it runs in O((V + E) lgV). (Think of this algorithm as maintaining a queue of the frontier, and repeatedly relaxing edges on the frontier).

```
def djikstra(graph, source):
    dist, parent, q = {}, {}, set()
    for v in graph:
        dist[v] = float("inf")
        parent[v] = None
        q.add(v)
    dist[source] = 0

    while q:
        m = min(q, key=lambda x: dist[x])
        print(dist, q)
        q.remove(m)

        for neighbor in graph[m[0]]:
            u, v, w = m[0], neighbor[0], neighbor[1]
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                parent[v] = u
    return dist, parent
```

## Bellman Ford

Finds the single destination shortest path, and detects negative edge cycles if they exist. Takes O(EV) time.

```
graph = {
    'A': [('B', 2), ('C', 10)],
    'B': [('D', 1), ('E', 10)],
    'C': [('D', 2), ('E', 1)],
    'D': [('E', -1)],
    'E': [('D', -10)]
}


def bellman_ford(graph, source):
    edges = [((v, e[0]), e[1]) for v in graph for e in graph[v]]
    dist, parent = {}, {}
    for v in graph:
        dist[v] = float("inf")
        parent[v] = None
    dist[source] = 0

    for _ in range(len(graph)-1):
        for edge in edges:
            # relax each edge
            u, v = edge[0]
            w = edge[1]
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                parent[v] = u
    for e in edges:
        u, v = e[0]
        if dist[v] > dist[u] + e[1]:
            raise ValueError('negative weight cycle')
    return dist, parent
```

## Floyd-Warshall

Finds all-pairs shortest paths, assuming no negative weight cycles. Negative edge weights are ok. Runs in O(V^3) time and O(V^2) space.

Given an adjacency matrix of distances, we look at all pairs of vertices, and check if their is a shortest path through some node k. We loop though all vertices k.

```
dist = [
    [0, 1, 2],
    [float("inf"), 0, 1],
    [1, 2, 0]
]

def floyd_warshall(distance_matrix):
    # intialize distance and path matrices
    distance = np.array(distance_matrix)
    path = [[None for _ in range(len(distance_matrix))] for _ in range(len(distance_matrix))]
    for i in range(len(distance_matrix)):
        for j in range(len(distance_matrix)):
            if i != j and distance[i][j] != float("inf"):
                path[i][j] = i

    for k in range(len(distance)):
        for i in range(len(distance)):
            for j in range(len(distance)):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    path[i][j] = path[k][j]
    return distance, path
```

## Max-Flow

Given a source and sink node, we find the maximum units to move from source to sink. First we initialize the flow of every edge to 0. An augmented path is a path from source to sink such that the residual capacity on every edge is greater than 0. Ther residual capacity, is the capacity minus the flow on an edge. We add an extra edges (residual edges) for residual capacity, if we ever need to send flow back, to get it from somewhere else in the graph.

Edmonds-Karp solves runs in O(VE^2).

Maximum bipartite matching can be solved using Edmonds-Karp by connecting a source and sink node to the graph.

## Dynamic Programming

1. Formulate the solution as a recurrence relation.
2. Show that the number of different parameter values taken on by the recurrence is bounded (hopefully by a polynomial).
3. Specify an order of evaluation for the recurrence so the partial results you need are always available when you need them (or just call the recursive function with memoization).

## A* Search

An extension to Djikstra, but is used for a single-pairs shortest path with an additional heuristic that keeps track of the estimate cost from source to destination. The estimate cost should never over-estimate the cost (such a function is called **admissible**), so that A* is guaranteed to return the shortest path. Worst-case runtime is O(E). A* search avoids exploring every vertice like Djikstra does in a BFS manner.

```
graph = {
    'A': [('B', 2), ('C', 10)],
    'B': [('D', 1), ('E', 10)],
    'C': [('D', 2), ('E', 1), ('A', 3)],
    'D': [('E', 1)],
    'E': []
}
heuristic_score = {
    'A': 0,
    'B': 1,
    'C': 5,
    'D': 1,
    'E': 2
}


def astar_search(graph, start, goal, heuristic_score):
    # intialize
    dist, parent, fscore = {}, {}, {}
    for v in graph:
        fscore[v] = dist[v] = float("inf")
        parent[v] = None
    dist[start] = 0
    fscore[start] = heuristic_score[start]

    # open set is the frontier
    open_set = set([start])
    # closed set is the interior of visited areas
    closed_set = set()

    while open_set:
        u = min(open_set, key=lambda v: fscore[v])
        if u == goal:
            break

        open_set.remove(u)
        closed_set.add(u)

        for n in graph[u]:
            v, w = n
            if v in closed_set:
                continue  # ignore neighbor which we already evaluated

            if v not in open_set:
                open_set.add(v)  # found a new vertex on the frontier

            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                fscore[v] = dist[v] + heuristic_score[v]  # the only real mod compared to Djikstra
                parent[v] = u

    return dist, parent
```

## Combinatorial Search and Pruning

Backtracking/pruning are general algorithms where you incrementally build candidate solutions to a problem, and candidates are abandoned as soon as they can no longer be solutions. The algorithm backtracks to the last possible candidates to keep searching in a depth-first-search manner.

### Minimax with Alpha Beta Pruning

Alpha-beta pruning is a [minimax](https://en.wikipedia.org/wiki/Minimax#Minimax_algorithm_with_alternate_moves) algorithm with pruning. A minimax algorithm attempts to minimize the maximum loss that a player will have. Minimax with branching factor b and depth depth d has O(b^d) leaf nodes. Alpha-beta has O(b^d/2) leaf node evaluations if the best moves are searched first.


```
def minimax(node, depth, is_maximizing_player):
    if depth == 0 or is_terminal(node):
        # return the value of landing in the terminal node
        return node.value

    if is_maximizing_player:
        # maximize the worst score that player A can get
        value = -float("inf")
        for child in node.children:
            value = max(value, minimax(child, depth - 1, False))
        return value
    else:
        # minimize the best score that player A can get
        value = float("inf")
        for child in node.children:
            value = min(value, minimax(child, depth - 1, True))
        return value

minimax(start, D, True)
```

The pruning idea behind alpha-beta is that: whenever the minimum score for the minimizing player is less than or equal to the maximum score for the maximizing player, we don't need to search that part of the tree anymore (since the maximizing player won't be able to get a higher score by going down that path in the tree).

```
def alphabeta(node, depth, alpha, beta, is_maximizing_player):
    if depth == 0 or is_terminal(node):
        # return the value of landing in the terminal node
        return node.value

    if is_maximizing_player:
        # maximize the best score that player A can get
        value = -float("inf")
        for child in node.children:
            value = max(value, minimax(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        # minimize the best score that player A can get
        value = float("inf")
        for child in node.children:
            value = min(value, minimax(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value
```

## Bit Manipulation

* 1 byte = 8bits
* A signed twos complement n-bit number has range 2^(n-1)-1 to -(2^n-1)
* An unsigned n-bit number of all 1s is 2^n-1
* 2^10 = 1024, 2^20 /approx 1e6, 2^30 /approx 1e9 
* 2^10 bytes is 1KiB, 2^20 bytes is 1MiB, 2^30 bytes is 1GiB
* (~) is bit-wise not, (&) is bit-wise and, (\|) is bit-wise or
* (^) is XOR
* (<<) is lshift. E.g. 2 << 3 is 16
* (>>) is rshift. E.g. 16 >> 3 is 2
* 3.15e7 seconds in a year


## Combinatorics

Permutations: Order of items matters. Total number of permutations of k out of N items is N! / (N-k)!

Combintaions: Order doesn't matter. Total number of combinations of k out of N items is N! / [k! * (N-k)!] since there will be k! repeats of items in the permutation.

## P vs NP

P = there exists a polynomial time algorithm to solve this problem

NP = the solution to this problem can be verified in polynomial time (or solved in non-deterministic-polynomial time).

NP-hard = X is NP-hard if every problem in NP reduces to X in polynomial time, so you are at least as hard as everything in NP

NP-complete = X is NP-complete if X is in NP and X is NP-hard.

Reduction = a reduction is a conversion of a problem from A -> B that is done in polynomial time

The question is whether there are problems that are NP that *cannot* be in P. The belief is P != NP, but there is no strong proof other than, we can't find algorithms fast enough to solve problems that are NP-complete in polynomial time.

## OOP

Encapsulation: Couple properties and methods into a single object. If the methods are stateful, it's cleaner to encapsulate them in objects so that they are coupled to the object's properties.

Abtsraction: Hide properties and methods of an object from the user to make the user interface simpler. Private properties/methods makes it easier to refactor the implementation without affecting the user.

Inheritance: Re-use properties and methods of higher level objects to eliminate redundant code.

Polymorphism: (Many forms) Overload/override a method so that all objects can be used the same way. (e.g. a render method over-rided for all types of HTML objects).

## Design Patterns

Singleton: a class that only has one instance, not matter how many times it is instantiated you get the same instance. A hack in python is to share the state of all instances so that it behaves like a singleton:

```
class Singleton:
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state
```

Factory: classes get instantiated through a function or another object. For example, if we wanted to create shape objects given a string input, we could create a function that would create the object using a case statement.

```
def create_shape(shape_type, val):
    class Triangle:
        def __init__(self, arg):
            self.val = arg
    class Circle:
        def __init__(self, arg):
            self.val = arg
    if shape_type == 'triangle':
        return Triangle(val)
    elif shape_type == 'circle':
        return Circle(val)
    else:
        raise
```

## Operating Systems

Multi-tasking on CPU cores occurs with context-switching: CPU receives interrupt  on a regular basis so that the scheduler can select which process to run next. Processes share the system memory. The OS is responsible for allocating system memory. Processes can invoke OS routines via system calls (syscall instructions).

Each process uses memory for the call stack (variables and functions), text (code itself), and heap (everything else). In common use-cases, the stack is stored at the top of a program's address space, the code is stored at the bottom, and the heap storage is stored in the middle. The OS allocates/de-allocates chunks of the heap space (called pages). To free out RAM, portions of the heap may be stored in the hard-drive, and they are marked as "swapped".

IPC (Interprocess Communications): files, pipes, sockets, signals, etc.



### Parallelism and Concurrency

Parallelism is simultaneous execution of multiple processes, concurrency is the composition of independently executing processes (e.g. threads, multiple actors and shared resources). Threads run in the same process  in a shared memory space, while processes run in separate memory spaces.

Race Condition: getting different values depending on which code executes first. This occurs when there is no lock around a shared resource.

Locks: block other threads trying to access same data at the same time to avoid race conditions. Mutual exclusion (mutex) means that only one thread can access the critical code/data at a time.

Semaphores: higher level synchronization tool compared to locks. It is a counter manipulated atomically through a signal and wait operation. A semaphore with count 1 is similar to a mutex lock (called a binary semaphore). With count > 1, the semaphore allows multiple threads to hold the semaphore. Useful for Producer/Consumer systems.

Deadlock: All threads are blocked, waiting for each other to release locks. There is a circular dependency of processes on each other. When thread A acquires lock A and then waits on lock B, and thread B acquires lock B and waits on lock A, we have a deadlock. Instead, both A and B should acquire lock A then B in that order.

