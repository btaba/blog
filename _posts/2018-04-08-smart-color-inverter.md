---
layout: post
title:  "Inverting Color on a Display"
date:   2018-04-08 00:00:00
categories: projects
tags: projects
comments: True
---

Staring at displays is easier on the eyes with apps like [f.lux](https://justgetflux.com) and [iris](https://iristech.co), which apply color filters to our displays to reduce the amount of blue light our eyes consume.

If your screen has mostly white colors and you use *f.lux*, the display is still sometimes too bright. This is why many apps also have color inverters, which flip the colors of all pixels on your display. The effect looks something like this:

|   |   |
|---|---|
|![Before Inversion](/assets/article_images/2018-04-08-smart-color-inverter/light_screen.png)|![After Inversion](/assets/article_images/2018-04-08-smart-color-inverter/light_screen_simple_invert.png)|

and the function applied is pretty simple:

```python

from PIL import Image
import numpy as np

image = np.array(Image.open('./dark_screen.png', mode='r'))
color_inverted_image = 1 - image[:, :, :3] / 255.

```


I always get **really annoyed** though, when most of my screen is already a dark color. The inverted colors then get all messed up:

|   |   |
|---|---|
|![Before Inversion](/assets/article_images/2018-04-08-smart-color-inverter/dark_screen.png)|![After Inversion](/assets/article_images/2018-04-08-smart-color-inverter/dark_screen_simple_invert.png)|


I wanted to see if there was a smarter way to pick which colors to invert in an image.

### Smart invert

To illustrate the basic idea of a smarter inversion algorithm, we'll start with this image and its simple color inversion (which doesn't look too good):

|   |   |
|---|---|
|![Base Image](/assets/article_images/2018-04-08-smart-color-inverter/hayden.png)|![Simple Inversion - looks like shit](/assets/article_images/2018-04-08-smart-color-inverter/hayden_simple_invert.png)|


The basic idea of the algorithm is to find regions of the image to invert if they are bright, and regions of the image to keep the same if they are already dark.

To do this, first convert the image to black and white, and then get all the [connected components](https://en.wikipedia.org/wiki/Connected_component_(graph_theory)) of the black and white image:

|   |   |
|---|---|
|![Black and White Image](/assets/article_images/2018-04-08-smart-color-inverter/hayden_bw.png)|![Connected Components](/assets/article_images/2018-04-08-smart-color-inverter/hayden_connected_components.png)|


Then take the top 1% (or any other threshold) of the largest bright connected components. In this case, there are only 2:

![Contour of large white connected components](/assets/article_images/2018-04-08-smart-color-inverter/hayden_contour.png)


Finally, we invert the large white connected components only:

![Smart color invert](/assets/article_images/2018-04-08-smart-color-inverter/hayden_smart_invert_more.png)

Notice that the white regions are now dark and all the dark regions remain the same since they're already dark! The image in the middle also has inverted portions. If you want less regions to be dark, you can change the threshold to invert less of the bright connected components:

![Smart color invert less regions](/assets/article_images/2018-04-08-smart-color-inverter/hayden_smart_invert.png)

Notice that the image in the middle is now left untouched as well.

And finally let's compare our original problem image using smart invert versus vanilla invert:

|||
|--|--|
|![Smart Invert](/assets/article_images/2018-04-08-smart-color-inverter/dark_screen_converted.png)|![Simple Invert](/assets/article_images/2018-04-08-smart-color-inverter/dark_screen_simple_invert.png)|

Smart invert looks pretty good to me! Only the top application bar is inverted with the smart invert, whereas the simple inversion inverts everything.

##### [Check out the code gist](https://gist.github.com/btaba/99b95b36bd2e26e80406c5262b6a889b)

### Edge cases

There are some edges however. For example take the following image with it's simple inversion and it's smart inversion:

||||
|--|--|--|
|![Image](/assets/article_images/2018-04-08-smart-color-inverter/edge_case.png)|![Simple Invert](/assets/article_images/2018-04-08-smart-color-inverter/edge_case_simple_invert.png)|![Smart Invert](/assets/article_images/2018-04-08-smart-color-inverter/edge_case_smart_invert.png)|

Notice that the smart inversion makes the whole image black, which is not very helpful. This can be fixed by adding contours around the connected components like so, which keeps most of the image dark but still helps us distinguish what's in the image:

![Smart Invert with Contours](/assets/article_images/2018-04-08-smart-color-inverter/edge_case_smart_invert_fix.png)


### Is it practical for real-time apps?

I'm not sure. The implementation I made runs anywhere from 100 to 300ms, which is far too slow for a 60fps display. The algorithm could potentially be sped up with simpler code that is also GPU optimized.

Poking around a bit to see how hard this would be, I couldn't find connected components algorithms in [Apple's Image Unit Kernels](https://developer.apple.com/library/content/documentation/GraphicsImaging/Conceptual/ImageUnitTutorial/WritingKernels/WritingKernels.html#//apple_ref/doc/uid/TP40004531-CH3-SW1). Applying the pixel inversions with [Quartz](https://developer.apple.com/documentation/coregraphics/quartz_display_services) and [OpenCV](https://opencv.org) might be just as inefficient as the plain python implementation (since I also use OpenCV). If you successfully implement this as a real-time mac app, please let me know! I will download.

For now I guess I'm stuck with simple color inversion to get my screen darker.
