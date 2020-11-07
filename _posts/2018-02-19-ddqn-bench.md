---
layout: post
title:  "DDQN"
date:   2018-02-19 00:00:00
categories: projects
tags: projects
comments: True
---


I wanted to re-create the latest Deep Q-Learning results on Atari, a huge milestone for AI Research in the past few years.

Apart from the [official code](https://github.com/kuz/DeepMind-Atari-Deep-Q-Learner) in Lua, I found several Python implementations on github, notably [this one from OpenAI](https://github.com/openai/baselines/tree/master/baselines/deepq) or [this one](https://github.com/ppwwyyxx/tensorpack/tree/master/examples/DeepQNetwork) among many others. Few Python implementations actually run on Atari environments though, and even less actually report benchmarks comparing to published results. I wasn't able to reproduce or even run some implementations, including the OpenAI DDQN [Atari baselines](https://github.com/openai/baselines-results/blob/master/dqn_results.ipynb) (see [github issue](https://github.com/openai/baselines/issues/176)).

After fumbling for several days with bad benchmark results on Atari, I remembered that I implemented a version of DQN for a [CS294](http://rll.berkeley.edu/deeprlcourse/) homework, which actually works. I added DDQN + Dueling + Prioritized Replay and put it in [`yarlp`](http://github.com/btaba/yarlp) (Yet Another Reinforcement Learning Package). Then I ran some more benchmarks!

I trained 6 Atari environments for 10M time-steps (**40M frames**), using 1 random seed, since I have limited time on this Earth. I used DDQN with dueling networks without prioritized replay. I compare the final mean 100 episode raw scores for yarlp (with exploration of 0.01) with results from [Hasselt et al, 2015](https://arxiv.org/pdf/1509.06461.pdf) and [Wang et al, 2016](https://arxiv.org/pdf/1511.06581.pdf) which train for **200M frames** and evaluate on 100 episodes (exploration of 0.05). I also compared visually to [the learning curves](https://github.com/openai/baselines-results/blob/master/dqn_results.ipynb) released by OpenAI.

|env|yarlp DUEL 40M Frames|Hasselt et al DDQN 200M Frames|Wang et al DUEL 200M Frames|
|---|---|---|---|
|BeamRider|8705|7654|12164|
|Breakout|423.5|375|345|
|Pong|20.73|21|21|
|QBert|5410.75|14875|19220.3|
|Seaquest|5300.5|7995|50245.2|
|SpaceInvaders|1978.2|3154.6|6427.3|


Here are the learning curves:

|   |   |   |   |
|---|---|---|---|
|![BeamRiderNoFrameskip-v4](/assets/article_images/2018-02-19-atari/BeamRiderNoFrameskip-v4.png)|![BreakoutNoFrameskip-v4](/assets/article_images/2018-02-19-atari/BreakoutNoFrameskip-v4.png)|![PongNoFrameskip-v4](/assets/article_images/2018-02-19-atari/PongNoFrameskip-v4.png)|![QbertNoFrameskip-v4](/assets/article_images/2018-02-19-atari/QbertNoFrameskip-v4.png)|
|![SeaquestNoFrameskip-v4](/assets/article_images/2018-02-19-atari/SeaquestNoFrameskip-v4.png)|![SpaceInvadersNoFrameskip-v4](/assets/article_images/2018-02-19-atari/SpaceInvadersNoFrameskip-v4.png)||


Since I ran for 1/5th of the frames, I wasn't expecting the final rewards to be close to that of the published results. But some environments are, especially the easier ones like Pong and Breakout. A notable difference between these implementations is that I use piece-wise learning rate and exploration schedules while Hasselt and Wang use linear ones. I wanted to do a mini-ablation experiment to see how these differences stack up against learned rewards. Surprisingly, the piece-wise schedules (`lr_schedule` vs `no_lr_schedule`) seemed to make the biggest gain as opposed to dueling networks or prioritized replay! Granted, I didn't run for multiple random seeds or environments or more frames, but this begs the question, can better exploration and learning rate schedules beat recent advances due to prioritized replay or dueling networks on Atari?

<center>
<img src="/assets/article_images/2018-02-19-atari/dqn_ablation_beamrider.png" width="500"/>
<figcaption>DDQN Ablation</figcaption>
</center>

Enjoy some gifs instead!

||||
|---|---|---|
|![BeamRider](/assets/article_images/2018-02-19-atari/beamrider.gif)|![Breakout](/assets/article_images/2018-02-19-atari/breakout.gif)|![Pong](/assets/article_images/2018-02-19-atari/pong.gif)|
|![QBert](/assets/article_images/2018-02-19-atari/qbert.gif)|![Seaquest](/assets/article_images/2018-02-19-atari/seaquest.gif)|![SpaceInvaders](/assets/article_images/2018-02-19-atari/spaceinvaders.gif)|

[This blog post](https://www.alexirpan.com/2018/02/14/rl-hard.html) pretty much sums up my experience with Deep RL algorithms so far.
