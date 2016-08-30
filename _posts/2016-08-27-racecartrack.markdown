---
layout: post
title:  "RL Race Car"
date:   2016-08-27 20:00:00
categories: projects
tags: regular
comments: True
---


Check out this 2D race car learning to drive through a track by using On-Policy Monte Carlo control. The car doesn't know anything about the track; it only sees its current location, velocity, and rewards it gets while driving. The car can choose to change it's velocity by 1 unit in x and/or y during each time step, and it eventually learns how to get to the finish line! 

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ovn8IkiiBkQ" frameborder="0" allowfullscreen></iframe>

Check out this other windy one:

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZC1I8qa-ycE" frameborder="0" allowfullscreen></iframe>


The problem was taken from 5.6 of <a href="https://webdocs.cs.ualberta.ca/~sutton/book/ebook/node56.html" target="_blank">Sutton and Barto’s Intro to Reinforcement Learning</a> (with modified rewards to get both right and left turns). I highly recommend the book! 


If you're also learning Reinforcement Learning, please contribute to my <a href="https://github.com/btaba/intro-to-rl" target="_blank">attempt at solutions to Intro to RL</a>. Thanks to my co-workers Abhi and Chuck for helping code up the OG algo and environment for 5.4.