---
layout: page
title: ML Design Notes
permalink: /ml-design-notes/
---

ML Design example questions and Anki cards I made in 2019 for core ML concepts.

#### Example Questions

- Design an ad click prediction system.
- Design a homefeed/newsfeed ranking system.
- Design a translation service.
- Design and evaluate a classification and recommender system for music.

Read technical blog posts to get an idea of how to answer these questions.

#### ML Concepts

In no particular order:


- Explain the IID assumption (Independent and Identically Distributed).
- How are splits made in decision trees?
- How can probabilistic matrix factorization be implemented for collaborative filtering in code?
- How can you make splits in a decision tree for regression?
- How is batch normalization applied during test time?
- How is the result of matrix factorization for collaborative filtering used for recommending items to users?
- How many hidden layers in a deep neural network are needed to make it a universal approximator? How many layers in total?
- If a 2 layer neural network is a universal approximator, why do we use deep neural nets?
- If P(x) is the probability of seeing x, what is its entropy H? Show me the equation.
- In a binary classifier, what is precision?
- In an MLP (multi-layer perceptron), how does the variance of the output of a neuron, scale with the number of inputs N?
- In binary classication, what is recall?
- In Deep Learning, what are regularization methods commonly used to prevent overfitting?
- In deep learning, why was layer normalization proposed over batch normalization, and what does it do?
- In linear regression, we have \(y = Xw + \epsilon \) where \(\epsilon\) is our error in our predictions. What is the formula for w if we want to minimize sum of square residuals?
- How do you deal with imbalanced classes?
- How do you deal with missing values?
- How do you generally prevent overfitting (for either neural nets or classic ML models)?
- How do you know if your model is underfit?
- How do you know that you are overfitting a model?
- How do you prevent underfitting?
- What are some metrics used for ranking problems?
- What is AUC of the ROC and what is it used for? What are some values of AUC of ROC?
- What is bagging?
- What is boosting?
- What is discounted cumulative gain?
- What is generalization?
- What is precision, recall and F1?
- What is regularization?
- What is the bias-variance tradeoff?
- What is Bias and Variance?
- What is the curse of dimensionality?
- In Reinforcement Learning, explain why SARSA (on-policy) is "safer" than Q-learning (off-policy)? Take the grid-world with a cliff as an example.
- In Reinforcement Learning, is the vanilla policy gradient on-policy or off-policy?
- In Reinforcement Learning, what are actor-critic methods?
- In Reinforcement Learning, what are on-policy and off-policy methods?
- In Reinforcement Learning, what does it mean for an agent when an environment is fully observed?
- In Reinforcement Learning, what does it mean for an agent when the environment is partially observed?
- In Reinforcement Learning, what is an advantage function?
- In Reinforcement Learning, what is model-free vs model-based RL?
- In Reinforcement Learning, what is the key idea behind Double Deep Q-Learning (van Hasselt et al, 2015) that makes DDQN not overestimate Q-values in Deep Q-learning (Mnih et al, 2015)?
- In Reinforcement Learning, when doing Q-learning with function approximation, what are two classic tricks to get Q-learning to converge?
- In Reinforcement Learning, why are on-policy methods not sample efficient?
- In Reinforcement Learning, why does vanilla policy gradient perform better when updating the gradient using an advantage function as opposed to the raw rewards?
- In Reinforcement Learning, why is Q-learning an off-policy method?
- In Reinforcement Learning, why is SARSA an on-policy method?
- In Statistics, how does power relate to the Type-2 Error?
- What is power in statistics?
- In Statistics, what is a p-value in a Hypothesis test?
- In Statistics, what is bootstrap sampling?
- In Statistics, what is the Type-1 Error in a hypothesis test?
- In Statistics, what is the Type-2 Error in a Hypothesis test?
- In Statistics, what is the variance around the sample mean?
- In the fast.ai library, what does fit-one-cycle do?
- What are 3 common data preprocessing steps that are done for deep learning?
- What are 5 commonly used activation functions in neural networks and their pros/cons?
- What are a common hyperparameters to tune when training neural networks, besides the network itself?
- What are a few different algorithms for updating parameters in SGD besides vanilla SGD?
- What are assumptions and pitfalls of Principal Components Analysis?
- What are discriminative learning rates?
- What are evaluation metrics used for regression?
- What are Factorization Machines and how do they work?
- What are some common ConvNet architecture patterns in terms of Conv, Relu, Pool, Fully-Connected (FC)?
- What are some common ConvNet architectures that were trained on ImageNet? Give estimates of their top-5 error rates on ImageNet.
- What are some multi-class metrics to evaluate multi-class models?
- What are some multi-label metrics to evaluate multi-label models?
- What are some weight initialization methods for an MLP (multi-layer perceptron)?
- What are the pros/cons of minibatch stochastic gradient descent compared to gradient descent?
- What does it mean for a problem to be multi-class?
- What does it mean for a problem to be multi-label?
- What is a convolutional neural network?
- What is a false negative?
- What is a false positive?
- What is a true negative?
- What is a true positive?
- What is an embedding layer in deep learning?
- What is an estimator in statistics?
- What is an unbiased estimator, in statistics?
- What is Batch Normalization and what is it good for?
- What is bias of an estimator in statistics?
- What is catastrophic forgetting in deep learning?
- What is collaborative filtering?
- What is extrapolation error in reinforcement learning?
- What is Gini impurity and how is it used to make splits in decision trees?
- What is imitation learning?
- What is information gain and how is it used to make splits in a decision tree?
- What is inverse reinforcement learning?
- What is logistic regression?
- What is the meaning of entropy?
- What is Occam's razor?
- What is Principal Components Analysis?
- What is Simpson's Paradox?
- What is the Bayesian Personalized Ranking loss and for what task is it used?
- What is the binary hinge loss? Write it down.
- What is the central idea behind Trust-Region-Policy-Optimization (TRPO) and Proximal-Policy-Optimization (PPO) that Schulman came up with in 2015 & 2016?
- What is the chain rule in probability theory? Let's say we have a joint distribution \(P(A_n, ..., A_1)\), how can it be broken down with the chain rule?
- What is the cross-entropy loss?
- What is the difference between AUC of the Precision-Recall (PR) curve vs AUC of the ROC curve? Which is better?
- What is the formula for cosine-similarity?
- What is the Hamming Loss? What is its range?
- What is the markov property in probability theory? Can you write it down?
- What is the naive baye's model? What is naive about it?
- What is the No Free Lunch Theorem?
- What is the preferrable way to control overfitting in neural networks and why?
- What is the softmax function?
- What is the top-5 human error rate on ImageNet?
- What kind of layers are used in convolutional neural networks?
- When we say true positive or false positive or false negative, what does positive/negative mean and what does true/false mean?
- Which activation function should I use in a neural network?
- Why does L1 regularization induce sparsity?
- Write down the normal distribution.
- Write down the Pearson sample correlation coefficient. What is it's range?
- Describe how a convolutional layer works for an input of size WxHxC.
- Describe the K-Means clustering algorithm.
- Describe what the pooling layer does in a ConvNet.
