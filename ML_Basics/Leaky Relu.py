
#Leaky Relu is an activation function. x if x>0 or x*alpha if x<0 where alpha is a constant which could be 0.1 or 0.01. 
#Relu activation helps with Vanishing/exploding gradients but it creates its own problem such as dead neuron during training time
#For -ve values Leaky Relu is alpha*x. Due to this leak, the problem of dead neurons is avoided. 
#Further, a research has found that Leaky ReLU activation functions outperformed the ReLU activation function.
#Further, Leaky ReLU activation functions with a higher value of leak perform better than those with lower value of leak.
#Pros
#Performs better as compared to traditionally used activation functions such as Sigmoid and Hyperbolic-Tangent functions and even ReLU.
#It is fast and easy to calculate. The same applies to it’s derivative which is calculated during the backpropagation.
#It does not saturate for positive values of input and hence does not run into problems related to exploding/vanishing gradients during Gradient Descent.
#Does not suffer from dying ReLU problem.
#Cons
#non-differentiable at 0
#alpha has to define before training/constant.

import numpy as np
list = []
n = input()
for i in range (0,n):
  k = input()
  list.append()
arr = np.array(list)
for i in range(0,n):
  if arr[i]<x:
    arr[i]=arr[i]*alpha
for i in range (0,n):
  print(arr[i])
 
  
