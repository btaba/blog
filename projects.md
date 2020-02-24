---
layout: page
title: Random Projects
permalink: /projects/
---


> [**Handwritten generation**](https://github.com/btaba/handwriting-generation){:target="_blank"}


![Correct Prediction for the 2018 World Cup!](/assets/article_images/projects/handwritten-gen.png){:target="_blank"}


> [**yarlp (yet another reinforcement learning package)**](https://github.com/btaba/yarlp){:target="_blank"}


Implementations of A2C, DDQN, PG, CEM.

||||
|---|---|---|
|![BeamRider](https://github.com/btaba/yarlp/raw/master/assets/atari10m/ddqn/beamrider.gif)|![Breakout](https://github.com/btaba/yarlp/raw/master/assets/atari10m/ddqn/breakout.gif)|![Pong](https://github.com/btaba/yarlp/raw/master/assets/atari10m/ddqn/pong.gif)|
|![QBert](https://github.com/btaba/yarlp/raw/master/assets/atari10m/ddqn/qbert.gif)|![Seaquest](https://github.com/btaba/yarlp/raw/master/assets/atari10m/ddqn/seaquest.gif)|![SpaceInvaders](https://github.com/btaba/yarlp/raw/master/assets/atari10m/ddqn/spaceinvaders.gif)|


> [**joint image-text embeddings using Canonical Correlations Analysis**](https://github.com/btaba/text-image-embedding){:target="_blank"}


> [**Introduction to Reinforcement Learning by Sutton & Barto, Solutions to 1st Edition**](https://github.com/btaba/intro-to-rl){:target="_blank"}


Solutions to the 1st edition. Race car problem:

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZC1I8qa-ycE" frameborder="0" allowfullscreen></iframe>

<br>

> [**Sinkhorn Knopp**](https://github.com/btaba/sinkhorn_knopp){:target="_blank"}

Convert non-negative square matrices with total support into doubly stochastic matrices.


```python
>> import numpy as np
>> from sinkhorn_knopp import sinkhorn_knopp as skp
>> sk = skp.SinkhornKnopp()
>> P = [[.011, .15], [1.71, .1]]
>> P_ds = sk.fit(P)
>> print P_ds
    [[ 0.06102561  0.93897439]
    [ 0.93809928  0.06190072]]
>> print np.sum(P_ds, axis=0)
    [ 0.99912489  1.00087511]
>> print np.sum(P_ds, axis=1)
    [ 1.,  1.]
```

> [**Climate Change Chatbot**](https://github.com/innainu/climatechangebot){:target="_blank"}


<iframe width="560" height="315" src="https://www.youtube.com/embed/6_xskuYT0Ws" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

---

[**Kimchi Ventures**](https://kimchiventures.com){:target="_blank"}

[kimchi making experiences](https://www.airbnb.com/experiences/216272) in NYC

![Delicious!](https://static1.squarespace.com/static/5ae3edcefcf7fd2d87436ffc/5ae401b6d274cb3bcc106a4c/5ae401b6ed62fe3847c9d2c5/1524892087589/?format=1500w)

---

Music

<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/users/305949662&color=%2300aabb&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe>

