---
layout: post
title:  "mac build updates"
date:   2017-10-13 00:00:00
categories: projects
tags: hardware
comments: True
---

*OS X 10.12.6 was working great for me...until I wanted to run tensorflow on GPU. OS X 10.13 didn't help.*

Unfortunately tensorflow isn't Mac friendly, because ["As of version 1.2, TensorFlow no longer provides GPU support on Mac OS X."](https://www.tensorflow.org/install/install_mac). I don't even understand what that means since you can always build from source assuming NVIDIA provides CUDA support for Mac. But I did get a working build with tensorflow 1.1 running with CUDA 8 on my GTX 1080 GPU (and Xcode 7.3).

**However**, running GPU intensive programs would occasionally **crash** my computer! After spending hours trying to extract some crash logs (they were not in Console), I found that I was getting a kernel panic, and I couldn't figure out how to fix it.

So I naively decided to update my Hackintosh to OS X 10.13 High Sierra, hoping to find more stable GPU performance. I followed [this tutorial](https://www.tonymacx86.com/threads/the-perfect-customac-pro-macos-high-sierra-10-13-on-x99-full-success.227001/#post-1542618) to update from 10.12.6 (thanks kgp); the biggest snag was that `KernelPM` in `Kernel and Kext Patches` should've been set to true, and the `Install USB` would not boot from the USB 3.0 port! It only worked in the USB 2.0 port...

In any case, NVIDIA released [driver 378.10.10.10.15.117](http://www.nvidia.com/download/driverResults.aspx/125512/en-us) for OS X 10.13 as of October 9th, with no support for the CUDA Toolkit. I quote, "A CUDA driver which supports macOS High Sierra 10.13 will be available at a later date." So I can't even use tensorflow with GPU on Mac. Apple, please get your act together.

So my solution to not being able to run tensorflow GPU on a Mac:

- Dual boot:
	- Hackintosh OS X 10.13
	- Ubuntu 16.0 on an [NVMe - M.2 Internal SSD](https://www.amazon.com/Samsung-960-EVO-Internal-MZ-V6E250BW/dp/B01LYFKX41/ref=sr_1_4?ie=UTF8&qid=1508390220&sr=8-4&keywords=samsung+nvme+ssd)
		- CUDA 8.0
		- cuDNN 6
		- tensorflow 1.4

It's a pretty sweet build!


---

If you're interested, here are some read/write stats on the NVMe using this [tutorial](https://www.shellhacks.com/disk-speed-test-read-write-hdd-ssd-perfomance-linux/):

```
> sync; dd if=/dev/zero of=tempfile bs=1M count=1024; sync
1024+0 records in
1024+0 records out
1073741824 bytes (1.1 GB, 1.0 GiB) copied, 0.446358 s, 2.4 GB/s

> dd if=tempfile of=/dev/null bs=1M count=1024
1024+0 records in
1024+0 records out
1073741824 bytes (1.1 GB, 1.0 GiB) copied, 0.375208 s, 2.9 GB/s
```

Now that's pretty fast!

Some other niceties I set up:

- [`rclone`](https://github.com/btaba/dotfiles/blob/master/cron/sudo-cron#L6) backups to my Google Drive account
- Time Machine backups to an internal 1TB HDD
