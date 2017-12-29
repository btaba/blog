---
layout: post
title:  "yarlp benchmarks"
date:   2017-12-27 00:00:00
categories: projects
tags: regular
comments: True
---

There are a lot of RL packages out there, [`tensorforce`](tensorforce), [`rllab`](rllab), [`openai-lab`](openailab), [`baselines`](baselines), and the list goes on. It's hard to know however, how any of those implementations stack up to published state-of-the-art results. There are several reasons, some are: 

1. The standard RL tasks (Mujoco & Atari) are extremely sensitive to not only model hyper-parameters but even **random seeds** ([Islam et al](islametal)).
2. Even researchers implementing the same algorithm in two different code-bases have failed to produce consistent results given the same model parameters (described in [Henderson et al](hendersonetal), e.g. Figure 6).
3. It takes time to build reproducible experimentation code.

I've been building [`yarlp`](yarlp) for educational purposes, and I wanted to make sure my implementations matched baselines. OpenAI seems to have created something akin to [tensorflow models](tensorflowmodels) in terms of reproducibility for RL, so a natural step was to benchmark against OpenAI [`baselines`](baselines). Nevertheless, I found it quite difficult to match their results because of:

1. environment wrappers and how environment observations were normalized
2. simple tweaks to model hyper-parameters
3. the choice of baseline model
4. and yes, **random seeds**!


Here are my results on Mujoco1M after painstakingly hashing out minor differences in OpenAI's implementation of TRPO compared to mine (which are now virtually identical 😂). I averaged over 5 random seeds using [this script](baselinesscript) in `baselines`, and using the `run_benchmark` cli script in `yarlp`, which run all environments in parallel. The results match, but clearly even 5 random seeds is not enough.

|   |   |   |   |
|---|---|---|---|
|![Hopper-v1]({{ site.url }}/assets/article_images/2017-12-27-yarlp-bench/Hopper-v1.png)|![HalfCheetah-v1]({{ site.url }}/assets/article_images/2017-12-27-yarlp-bench/HalfCheetah-v1.png)|![Reacher-v1]({{ site.url }}/assets/article_images/2017-12-27-yarlp-bench/Reacher-v1.png)|![Swimmer-v1]({{ site.url }}/assets/article_images/2017-12-27-yarlp-bench/Swimmer-v1.png)|
|![InvertedDoublePendulum-v1]({{ site.url }}/assets/article_images/2017-12-27-yarlp-bench/InvertedDoublePendulum-v1.png)|![Walker2d-v1]({{ site.url }}/assets/article_images/2017-12-27-yarlp-bench/Walker2d-v1.png)|![InvertedPendulum-v1]({{ site.url }}/assets/article_images/2017-12-27-yarlp-bench/InvertedPendulum-v1.png)|


---

To demonstrate some of the difficulty in reproducibility, here is the same exact algorithm averaged over 2 randomly chosen sets of 3 random seeds on Swimmer-v1 (95th percentile CI):

![`baselines` run on two randomly chosen sets of random seeds, similar to Figure 10 in Henderson et al]({{ site.url }}/assets/article_images/2017-12-27-yarlp-bench/Swimmer-v1-baselines-diff-seeds.png)

And this is what happens when I use a value function implementation from [`rllab`](rllab) compared to the one used in OpenAI [`baselines`](baselines) on Swimmer-v1 averaged over 3 random seeds:

![`rllab` (green) value function vs `baselines` (blue) value function]({{ site.url }}/assets/article_images/2017-12-27-yarlp-bench/Swimmer-v1-rllab-vs-baselines.png)

And this is what happens when observations are not normalized on the Mujoco1M benchmark (Walker2d and HalfCheetah perform noticeably worse):

|   |   |   |   |
|---|---|---|---|
|![Hopper-v1]({{ site.url }}/assets/article_images/2017-12-27-yarlp-bench/Hopper-v1_no_norm.png)|![HalfCheetah-v1]({{ site.url }}/assets/article_images/2017-12-27-yarlp-bench/HalfCheetah-v1_no_norm.png)|![Reacher-v1]({{ site.url }}/assets/article_images/2017-12-27-yarlp-bench/Reacher-v1_no_norm.png)|![Swimmer-v1]({{ site.url }}/assets/article_images/2017-12-27-yarlp-bench/Swimmer-v1_no_norm.png)|
|![InvertedDoublePendulum-v1]({{ site.url }}/assets/article_images/2017-12-27-yarlp-bench/InvertedDoublePendulum-v1_no_norm.png)|![Walker2d-v1]({{ site.url }}/assets/article_images/2017-12-27-yarlp-bench/Walker2d-v1_no_norm.png)|![InvertedPendulum-v1]({{ site.url }}/assets/article_images/2017-12-27-yarlp-bench/InvertedPendulum-v1_no_norm.png)|

One can easily produce these kinds of results for other environments, as seen in [Henderson et al](hendersonetal).

RL is fun, but it's a bit concerning how unstable these algorithms and environments can be.


[hendersonetal]: https://arxiv.org/pdf/1709.06560.pdf 
[islametal]: https://arxiv.org/pdf/1708.04133.pdf
[tensorforce]: https://github.com/reinforceio/tensorforce
[openai_lab]: https://github.com/kengz/openai_lab
[tensorflowmodels]: https://github.com/tensorflow/models
[yarlp]: https://github.com/btaba/yarlp
[tensorforce]: https://github.com/reinforceio/tensorforce
[baselines]: https://github.com/openai/baselines
[openailab]: https://github.com/kengz/openai_lab
[rllab]: https://github.com/rll/rllab
[baselinesscript]: https://github.com/btaba/baselines/blob/master/baselines/trpo_mpi/run_trpo_experiment.py
