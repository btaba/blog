---
layout: post
title:  "Tensorflow in Docker"
date:   2018-09-07 00:00:00
categories: projects
tags: projects
image: /assets/article_images/2018-09-07-tf-kube/cover.png
comments: True
---

Here are some snags I found when running [Tensorflow](https://www.tensorflow.org/) models on [Docker](https://www.docker.com/) that can increase memory usage up to ~7x and increase inference time up to ~30x running on CPU.

### 1. CPU issues

When running tensorflow in docker, tensorflow thinks that it owns all the resources on the machine that docker is running on. For example, if you run a docker container on a kubernetes node with 128 cores, tensorflow  thinks it can use all 128 cores. This causes inference time to increase up to 30x depending on the network architecture.

##### Why?

When scheduling docker containers on kubernetes nodes, resources are limited per container using [cgroups](https://engineering.squarespace.com/blog/2017/understanding-linux-container-scheduling). Tensorflow in docker doesn't care about cgroups and thinks it can use all resources on the host. For example, tensorflow will set `inter_op_parallelism_threads` and `intra_op_parallelism_threads` to 128 by default in the config on a 128 core node. In reality, you may have set the limit to 8 cores per container in the kubernetes deployment! Bad things ensue.

##### How to fix?

Simply set the tensorflow config with the actual resources allocated to that container. To get CPU resources allocated in a docker container, you can use something like the following:

```python
import math
from pathlib import Path


def get_cpu_quota_within_docker():
    cpu_cores = None

    cfs_period = Path("/sys/fs/cgroup/cpu/cpu.cfs_period_us")
    cfs_quota = Path("/sys/fs/cgroup/cpu/cpu.cfs_quota_us")

    if cfs_period.exists() and cfs_quota.exists():
        # we are in a linux container with cpu quotas!
        with cfs_period.open('rb') as p, cfs_quota.open('rb') as q:
            p, q = int(p.read()), int(q.read())

            # get the cores allocated by dividing the quota
            # in microseconds by the period in microseconds
            cpu_cores = math.ceil(q / p) if q > 0 and p > 0 else None

    return cpu_cores
```

To set the `tf.ConfigProto`, you might do something like this:

```python
import tensorflow as tf
import multiprocessing

cpu_cores = get_cpu_quota_within_docker() or multiprocessing.cpu_count()

config = tf.ConfigProto(
    inter_op_parallelism_threads=cpu_cores,
    intra_op_parallelism_threads=cpu_cores)
```

And if you use [keras](https://keras.io/), you could just set the default tensorflow session using the above `tf.ConfigProto` like so:

```python
import keras.backend as K
K.set_session(tf.Session(config=config))
```

### 2. Memory issues

If you run tensorflow in docker with the default tensorflow config or the one above, you might notice your memory usage increasing on every inference call up to a certain point (for TF 1.10.1 on Ubuntu 16).

InceptionV3 should load in RAM using just ~600MB, but will then take up to ~4GB after ~100 inference calls depending on the hardware and `tf.ConfigProto`. I filed a bug in this [tensorflow issue](https://github.com/
tensorflow/tensorflow/issues/22098), where you can find code to reproduce.

##### Why?

No clue, but I'm hoping to gain some insight once this [tensorflow issue](https://github.com/
tensorflow/tensorflow/issues/22098) is resolved.


##### How to fix?

After many painful days, I discovered that memory stays flat if you set `inter_op_parallelism_threads=1`.


###### Another minor detail

Setting `inter_op_parallelism_threads=1` sped up inference calls from 3s to 700ms for a saliency model I was working on, but slowed down InceptionV3 by 50ms on average.


---

In conclusion, good luck. I hope this post saves someone some time.
