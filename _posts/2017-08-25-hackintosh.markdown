---
layout: post
title:  "mac it"
date:   2017-08-25 00:00:00
categories: projects
tags: regular
comments: True
---

After building a [desktop]({{ site.url }}/projects/2016/12/10/computer-build.html) a few months ago, I left it running on Linux. It wasn't all that bad, as long as I didn't need to use any applications with a real GUI 😂.

This left me in a state of dismay, not using my new build as much as I wanted to! I didn't really want Windows, but didn't really like using Linux as a personal OS either. And a few months went by...🤦🏽‍♂️

---

I was editing an image with GIMP a few days ago and I kept getting bugs with the distortion filter. So I updated to the latest version only to find more bugs! After an hour of dealing with this nonsense I realized that I just wanted shit to work! I'm editing an image, why does it need to be so difficult?

So I made the leap into the Hackintosh community at [tonymacx86](https://www.tonymacx86.com). It was a bit scary, but I've come out the other end very happy!

After 3 evenings of configuration, I now have Sierra running on my build with an ASUS X99 AII motherboard, i7 6800K CPU, 32GB RAM, 1TB SSD, GTX 1080 and with Xnu CPU power management. A big thanks to kgp for writing this [amazing tutorial](https://www.tonymacx86.com/threads/the-perfect-customac-pro-x99-a-ii-i7-6950x-128gb-g-skill-tridentz-aorus-gtx-1080-ti-xtreme.211621/), and to Pike R. Alpha, RehabMan, and tons of others for their hacks.

Here are some benchmarks with Cinebench:

![GPU]({{ site.url }}/assets/article_images/2017-08-25-hackintosh/cinebench_gpu.png)
![CPU]({{ site.url }}/assets/article_images/2017-08-25-hackintosh/cinebench_cpu.png)

And the CPU power management in action:

![Intel Power Gadget]({{ site.url }}/assets/article_images/2017-08-25-hackintosh/intel_cpu_bench.png)

The only real snag I faced was not being able to configure my ASUS PCE-AC56 Wifi network card, which is now for sale! I bought this [hackintosh wifi card](http://www.osxwifi.com/apple-broadcom-bcm94360cd-802-11-a-b-g-n-ac-bluetooth-4-0-with-adapter-for-pc-hackintosh) instead which works great out-of-box as suggested by kgp.

Now on to finding some image editing software!
