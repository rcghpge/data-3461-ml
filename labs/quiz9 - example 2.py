# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 11:05:54 2025

@author: PC
"""

"""
Robert Cocker
DATA 3461
Dr. Jawad
3/7/2025
Quiz #9 - Example 2
"""

# Example 2 

# Import required libraries
import numpy as np

# Given data
x = np.array([2, 4, 5])
y = np.array([1.2, 2.8, 5.3])

# Initialize parameters (theta_0 and theta_1)
b0 = 0
b1 = 1

# Learning rate and number of iterations
learning_rate = 0.01
iterations = 10000

# Gradient Descent
m = len(x) # number of data points

for i in range(iterations):
    # Hypothesis: y_pred = theta_0 + theta_1 * x
    y_pred = b0 + b1 * x
    
    # Calculate the cost (Mean squared error)
    cost = (1/m) * np.sum((y_pred - y) ** 2)
    
    # Calculate gradients
    d_b0 = (2/m) * np.sum(y_pred - y)
    d_b1 = (2/m) * np.sum((y_pred - y) * x)
    
    # Update parameters
    b0 -= learning_rate * d_b0 
    b1 -= learning_rate * d_b1
    
    # Print cost every 100 iterations to track progress
    if i % 100 == 0:
        print(f"Iteration {i}: Cost = {cost}, b0 = {b0}, b1 = {b1}")
    
# Final parameters after tuning
print(f"\nFinal parameters: b0 = {b0}, b1 = {b1}")

# Final parameters after training
b0 = round(b0, 1)
b1 = round(b1, 1)

# Final parameters after training
print(f"\nFinal parameters: theta_0 = {b0}, b1 = {b1}")

# Questions - Inference
"""
Note: See run 2 submission for results (outputs)

Lecture (class) initial b0, b1 values and equation:
b0 = -0.0113
b1 = 0.9677
y-hat = 0.9677*x_i - 0.0113

a.) Ran the first 10 iterations and output results. See output after running the code (this model).

b.) Ran 10,000 iterations and optimized output of results to show 10 iterations at every 1,000 step (epoch).
"""

"""
References
- lab, lecture, course materials
- ChatGPT
- Google
"""