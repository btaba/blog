---
layout: post
title:  "No Free Lunch - Except at Tech Companies"
date:   2018-07-20 00:00:00
categories: projects
tags: projects
comments: True
---

I was recently asked a question about the "No Free Lunch Theorem". I've heard of it in passing, but I never really read much into it. After reading the [wikipedia](https://en.wikipedia.org/wiki/No_free_lunch_theorem) more thoroughly, I found it pretty hard to reconcile implications of the theorem. Should I stop fitting models on things because fancy black-box optimization is no better than random search? Does cross-validation really work for generalization? What is the meaning of life? I will now seek to answer these questions!

## What is the No Free Lunch Theorem?

The No Free Lunch Theorem was posited by [David Wolpert](https://en.wikipedia.org/wiki/David_Wolpert) and William Macready, which first appeared in the paper ["No Free Lunch Theorems of Optimization"](https://ti.arc.nasa.gov/m/profile/dhw/papers/78.pdf) in 1997.

The abstract says: 

> "for any algorithm, any elevated performance over one class of problems is offset by performance over another class"

If you take this statement at face value, the implication is that no algorithm can solve all problems better than any other algorithm. Take cross-validation for example. Cross-validation is used to test performance of a model on future out-of-sample data by splitting training data into train/validation sets. Let's say we come up with a new algorithm called anti-cross validation, which picks the model with the worst performance on the validation set instead of the best. The implication of No Free Lunch is that cross-validation will do no better than anti-cross validation on unseen data averaged over all possible data generating functions.

So is seeking algorithms for problems a useless endeavor? How do we make sure our algorithms are generalizable?

## Caveat

To spare you from existential crisis, Wolpert et. al. also mention in the introduction that:

> "an algorithm’s average performance is determined by how 'aligned' it is with the underlying probability distribution over optimization problems on which it is run"

This is why some black-box optimization algorithms work better than others on certain problems in practice.

## First, some notation

Let's define the notation for the combinatorial optimization problem as done in the paper [1]. If you find this part a bit dense, feel free to skip to the [Conclusion](#conclusion)!

The search space is $X$ and the cost values are $Y$, both finite, with sizes $\|X\|$ and $\|Y\|$. An optimization problem $f$ is a mapping $f: X \rightarrow Y$. The goal is to find the value in $X$ with the lowest cost $Y$ by querying $f$ as little as possible. The space of all possible problems is of size $\|Y\|^{\|X\|}$.

When assessing the performance of algorithms, the authors compare only the distinct number of calls made to $f$. The sample of points queried is of size $m$ and is denoted as $d_m \equiv {(d_m^x(1), d_m^y(1)), ..., (d_m^x(m), d_m^y(m)) }$, ordered by the time at which they were generated. For example, $d_m^x(i)$ is the $X$ value of the ith element and $d_m^y(i) = f(y_i)$ is the resulting cost of the $i$th element.

The space of all data samples $m$ that we visit is $D_m = (X \times Y)^m$. And the set of all possible samples of arbitrary size is the union $D \equiv \cup_{m \geq 0} D_m $.

#### An algorithm

A search algorithm maps a set of previous visited points to a new one that we want to visit next, formally $a : d \in D \rightarrow \{x \| x \not\in d^x\}$. The $x \not\in d^x$ is there since we aren't counting revisits to elements of $X$.


#### Algorithm performance

The performance of an algorithm after $m$ steps is a function of the cost we've observed up to that point in time, which they call $\Phi(d_m^y)$. If we are doing minimzation, $\Phi$ would give us the minimum cost that we've observed up to that point in time.

#### Prior on class of problems

The authors then introduce a probability over the set of functions or optimization problems at hand, $P(f)$ defined over $F$, for $f \in F$. Put simply, $P(f)$ is the prior over the class of optimization problems we are trying to solve with an algorithm $a$.

#### Computing the cost of an algorithm

We can now compute the performance $\Phi(d_m^y)$ of an algorithm on a set of problems in $F$ by using $P(d_m^y \| f, m, a)$, the probability of getting a sample $d_m^y$ given the problem $f$ and algorithm $a$.

## No Free Lunch Theorem For Search

Let's say we have a pair of algorithms $a_1$ and $a_2$. We seek to find the algorithm that performs best on all classes of problems. The No Free Lunch Theorem states that $\sum_f P(d_m^y \| f, m, a_1) = \sum_f  P(d_m^y \| f, m, a_2)$. This means that $P(d_m^y \| f, m, a)$ is independent of $a$ when averaged over all cost functions!

In other words, there is no algorithm $a$ that performs better than any other over all cost functions for combinatorial optimization!



The proof for the first theorem is done with a proof by induction. The base case is for $m=1$, where we obtain the first data sample $d_1 = \\{ d_1^x, f(d_1^x) \\}$. The only possible value for $d_1^y$ is $f(d_1^x)$ since we only have one data point. So we have:

$$ \sum_f P(d_1^y | f, m=1, a)  = \sum_f \delta(d_1^y, f(d_1^x)) = |Y|^{|X| - 1}$$

where $\delta$ is the Kronecker delta function. The sum equals $\|Y\|^{\|X\| - 1}$ since $\delta(d_1^y, f(d_1^x)) = 1$ only when $d_1^y = f(d_1^x)$ which occurs for every $f$ with $m=1$ data point. The sum is thus $\sum_f 1$ which is $\|Y\|^{\|X\| - 1}$ after excluding the first value in $X$. The result is independent of $a$. To finish the proof, they show that if $\sum_f P(d_m^y \| f, m, a)$ is independent of $a$, then $\sum_f P(d_{m+1}^y \| f, m+1, a)$ is also independent of $a$. You can refer to Appendix A in the [original paper]((https://ti.arc.nasa.gov/m/profile/dhw/papers/78.pdf)) for the rest of the proof.


### Implications for Search

The No Free Lunch Theorem says that one algorithm is no better than any other on all classes of problems $f$ where $f$ is not fixed and $P(f) = 1 / \|F\|$ (uniform prior on class of problems).

If $P(f)$ is non-uniform, and knowledge of $P(f)$ is not incorporated in $a$, then there can be no assurances that $a$ will be more effective than any other algorithm. On the other hand, if we incorporate knowledge of $P(f)$ in $a$, we can have assurance that our algorithm will on average perform better than random.

To see this, we write the probability of obtaining some $d_m^y$ as $ P(d_m^y \| m, a) = \sum_f P(d_m^y \| f, m, a) P(f)$. The sum can be seen as an inner product between $P(d_m^y \| f, m, a)$ and $P(f)$. If $P(f)$ is non-uniform, we can always choose an $a$ so that the inner product is larger compared to a different $a$.


## No Free Lunch Theorem for Supervised Learning

How does the above relate to machine learning and cross validation? Luckily, Wolpert has another paper called [The Supervised Learning No Free Lunch Theorems](http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=8A9E4406154A4F0BF1D056AE403F17D6?doi=10.1.1.99.133&rep=rep1&type=pdf).

The overall objective of machine learning is to learn how to predict on samples that are not yet seen given samples of data that are seen. In other words, the overall goal is *generalizability* on a test-set given a training set of data.


### Notation for Supervised Learning

Just like for search, we have an input space $X$, an output space $Y$, and a function $f$ mapping $X$ to $Y$ on a dataset on $(x, y)$ pairs. As opposed to search, we are not iterating through the data to find the $x$ that minimizes $f(x)$. Instead we are trying to estimate $f$ given the entire dataset. The accuracy is measured on an *unseen* test dataset $X_t$ where $x \not\in X_t$ for $x \in X$.

A few new notations are added here: $h$ is the output/hypothesis of our model (i.e. the $x$-conditioned probability of an output $y$). $C$ is the loss of our algorithm on unseen test data. The generalization error is thus $E(C \| f, h, d)$, where $d$ is the train data.

A crucial assumption here is that the output of the learning algorithm $h$ only depends on the training data $d$, or $P(h \| f, d) = P(h \| d)$. If $d$ is fixed and $f$ changes, the learning learning algorithm behaves the same, which is often the case unless we make assumptions about $f$ when we choose $h$.

### No Free Lunch Theorems for Supervised Learning


The first theorem states that:

$$ E(C | d) = \sum_{h, f} Er(h ,f ,d) P(h | d) P(f | d)  $$

where $Er(h ,f ,d)$ is the test misclassification error. In simple terms, how well you generalize is determined by how aligned $h$ is with $f$. Unfortunately, unless you can somehow prove that your data was generated from $f$, you will not be able to find an algorithm $h$ that generalizes!

The second theorem states that, if $E_i$ is the expected cost of algorithm $i$, then for any two algorithms $P(h_1 \| d)$ and $P(h_2 \| d)$ averaged over uniform $f$:

$$E_1(C | f, d) = E_2(C | f, d)$$

and averaged uniformly over $P(f)$:

$$E_1(C | d) = E_2(C | d)$$

Therefore by any measure or cost function, no learning algorithm is better than any other if we don't know anything about $f$. Any heuristic we come up with to prevent overfitting or to prefer simpler models over more complex models are moot (i.e. cross-validation or [Occam's razor](https://en.wikipedia.org/wiki/Occam%27s_razor)).


### Implications for Machine Learning

The implications for Machine Learning are pretty much the same as for Search. If we can't make assumptions about $f$, then we cannot find a model that generalizes.

## Conclusion

Implications of the No Free Lunch theorem go well beyond search or machine learning. They relate to science in general. We can think of $X$ as a set of conditions for any experiment and $Y$ the associated measurements. $f$ is the physical law that generated $Y$. We then come up with some hypothesis $h$ for $f$. If we don't know $P(f)$ or $f$, which we often like in Physics, then we cannot have any guarantees that our hypothesis $h$ generalizes to any number of unseen experiments.

Does this mean that the scientific method is no better than random search or that cross-validating machine learning algorithms is useless? Well, we know in practice that many hypotheses and algorithms actually generalize well for the set of problems $f$ that we face in this universe. We can empirically test our hypotheses on unseen experiments (e.g. Einstein's general theory of relativity leading to detection of gravitational waves at [LIGO](https://en.wikipedia.org/wiki/LIGO) or particle physics predicting the existence of the [Higgs Boson](https://en.wikipedia.org/wiki/Higgs_boson) or AB tests for ML). Our hypotheses are still falsifiable, but they are useful and incredibly accurate nonetheless! So practically speaking, there are many problems $f$ that we don't care about, and we can find hypotheses that work well for the $f$ that we do.

No Free Lunch still makes you wonder how useful it is to push accuracies ad-infinitum on datasets like [ImageNet](https://en.wikipedia.org/wiki/ImageNet). Nevertheless, features and networks obtained from ImageNet tasks do seem to generalize well on other datasets/tasks (see [4]) so ¯\\_(ツ)_/¯. Crisis averted! ... practically speaking.

## References

1. ["No Free Lunch Theorems of Optimization"](https://ti.arc.nasa.gov/m/profile/dhw/papers/78.pdf)

2. [The Supervised Learning No Free Lunch Theorems](http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=8A9E4406154A4F0BF1D056AE403F17D6?doi=10.1.1.99.133&rep=rep1&type=pdf)

3. [What the No Free Lunch Theorems Really Mean; How to Improve Search Algorithms](https://sfi-edu.s3.amazonaws.com/sfi-edu/production/uploads/sfi-com/dev/uploads/filer/33/44/33440e97-fe46-4827-a1eb-a27196e1c49a/12-10-017.pdf)
 
4. [Do Better ImageNet Models Transfer Better?](https://arxiv.org/pdf/1805.08974.pdf)
