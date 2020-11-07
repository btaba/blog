---
layout: post
title:  "Sinkhorn Knopp"
date:   2016-04-03 20:00:00
categories: projects
tags: projects
comments: True
---

Do you need a non-negative square matrix converted to a doubly stochastic matrix? That is, you want all rows and columns to sum to one? Well here's a package just for that! I had the function lying around for a project I was working on at Columbia, and I thought it'd be a great opportunity to learn how to publish to PyPi! 

It uses the Sinkhorn-Knopp algorithm, which iteratively normalizes the rows and columns of a matrix to 1, until the matrix is doubly stochastic ([Sinkhorn, Knopp 1967][sinkhorn_knopp_ref]). It is guaranteed to converge for a non-negative square matrix $A$ if $A \neq 0$, and if $A$ has total support. Matrix $A$ has total support if every positive element of $A$ lies on a positive diagonal. And a positive diagonal of a matrix is defined as, for any permutation of $\sigma = \\{1,\dots,N\\}$, the sequence $$\{ a_{1,\sigma(1)},\dots, a_{N,\sigma(N)} \}$$ where all elements are positive (non-zero in this case). 

Just ```pip install sinkhorn_knopp``` and you're good to go. Here's a quick demo:

{% highlight python %}
import numpy as np
from sinkhorn_knopp import sinkhorn_knopp as skp
sk = skp.SinkhornKnopp()
P = [[.011, .15], [1.71, .1]]
P_ds = sk.fit(P)
print P_ds
    [[ 0.06102561  0.93897439]
    [ 0.93809928  0.06190072]]
print np.sum(P_ds, axis=0)
    [ 0.99912489  1.00087511]
print np.sum(P_ds, axis=1)
    [ 1.,  1.]
{% endhighlight %}


[Check it out on github][github], and feel free to add on!


[github]: https://github.com/btaba/sinkhorn_knopp
[sinkhorn_knopp_ref]: http://msp.org/pjm/1967/21-2/pjm-v21-n2-p14-s.pdf