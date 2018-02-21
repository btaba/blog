---
layout: post
title:  "Atari Me - Atari You"
date:   2018-02-19 00:00:00
categories: projects
tags: regular
comments: True
---

Reinforcement Learning...is it suddenly getting hot in here?

I wanted to see if I could re-create the latest DDQN with Dueling Networks + Prioritized Replay results on Atari, a huge milestone for RL Research.

https://github.com/ppwwyyxx/tensorpack/tree/master/examples/A3C-Gym

I found several implementations, none of which worked. Luckily I had implemented a version of DQN for a CS123 homework, which actually worked. I added DDQN + Dueling + Prior. Replay to the implementation in `yarlp`. Then I ran some benchmarks.

I trained 6 Atari environments for 10M time-steps (**40M frames**), using 1 random seed, since I only have 1 GPU and limited time on this Earth. I used DDQN with dueling networks, but no prioritized replay (although it's available). I compare the final mean 100 episode raw scores for yarlp (with exploration of 0.01) with results from [Hasselt et al, 2015](https://arxiv.org/pdf/1509.06461.pdf) and [Wang et al, 2016](https://arxiv.org/pdf/1511.06581.pdf) which train for **200M frames** and evaluate on 100 episodes (exploration of 0.05).

I don't compare to OpenAI baselines because the OpenAI DDQN implementation is **not** currently able to reproduce published results as of 2018-01-20. See [this github issue](https://github.com/openai/baselines/issues/176), although I found [these benchmark plots](https://github.com/openai/baselines-results/blob/master/dqn_results.ipynb) to be pretty helpful.

|env|yarlp DUEL 40M Frames|Hasselt et al DDQN 200M Frames|Wang et al DUEL 200M Frames|
|---|---|---|---|
|BeamRider|8705|7654|12164|
|Breakout|423.5|375|345|
|Pong|20.73|21|21|
|Q*Bert|5410.75|14875|19220.3|
|Seaquest|5300.5|7995|50245.2|
|SpaceInvaders|1978.2|3154.6|6427.3|


|   |   |   |   |
|---|---|---|---|
|![BeamRiderNoFrameskip-v4](/assets/atari10m/ddqn/BeamRiderNoFrameskip-v4.png)|![BreakoutNoFrameskip-v4](/assets/atari10m/ddqn/BreakoutNoFrameskip-v4)|![PongNoFrameskip-v4](/assets/atari10m/ddqn/PongNoFrameskip-v4.png)|![QbertNoFrameskip-v4](/assets/atari10m/ddqn/QbertNoFrameskip-v4.png)|
|![SeaquestNoFrameskip-v4](/assets/atari10m/ddqn/SeaquestNoFrameskip-v4.png)|![SpaceInvadersNoFrameskip-v4](/assets/atari10m/ddqn/SpaceInvadersNoFrameskip-v4.png)||


I wanted to do an ablation experiment to see what was contributing to the learning. Surprisingly, the learning rate schedule was doing most of the gain here! Granted, I didn't run for multiple random seeds or on several environments, but this goes to show how sensitive Deep RL is to the slightest change in your algorithm...


[rllab]: https://github.com/rll/rllab
