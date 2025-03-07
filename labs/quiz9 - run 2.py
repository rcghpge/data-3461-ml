# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 11:58:43 2025

@author: PC
"""

"""
Robert Cocker
DATA 3461
Dr. Jawad
3/7/2025
Quiz #9 - Example 2
"""

# Example 2 - run 2 (Model 2)
# Import required libraries
import numpy as np

# Given data
x = np.array([2, 4, 5])
y = np.array([1.2, 2.8, 5.3])

# Initialize parameters (b0 = theta_0, b1 = theta_1)
b0 = 0
b1 = 1

# Learning rate and number of iterations
learning_rate = 0.01
iterations = 10000

# Number of data points
m = len(x)

# Run first 10 iterations and print all
print("First 10 Iterations:")
for i in range(10):
    # Hypothesis: y_pred = b0 + b1 * x
    y_pred = b0 + b1 * x
    
    # Calculate the cost (Mean Squared Error)
    cost = (1/m) * np.sum((y_pred - y) ** 2)
    
    # Calculate gradients
    d_b0 = (2/m) * np.sum(y_pred - y)
    d_b1 = (2/m) * np.sum((y_pred - y) * x)
    
    # Update parameters
    b0 -= learning_rate * d_b0
    b1 -= learning_rate * d_b1

    # Print for each of the first 10 iterations
    print(f"Iteration {i+1}: Cost = {cost:.6f}, b0 = {b0:.6f}, b1 = {b1:.6f}")

# Continue training for the remaining iterations (up to 10,000)
print("\nIterations at Every 1000 Steps(epochs):")
for i in range(10, iterations):
    # Hypothesis
    y_pred = b0 + b1 * x
    cost = (1/m) * np.sum((y_pred - y) ** 2)

    # Gradients
    d_b0 = (2/m) * np.sum(y_pred - y)
    d_b1 = (2/m) * np.sum((y_pred - y) * x)

    # Update parameters
    b0 -= learning_rate * d_b0
    b1 -= learning_rate * d_b1

    # Print every 1000 iterations
    if (i+1) % 1000 == 0:
        print(f"Iteration {i+1}: Cost = {cost:.6f}, b0 = {b0:.6f}, b1 = {b1:.6f}")

# Print final results
print(f"\nFinal parameters: b0 = {b0:.6f}, b1 = {b1:.6f}")

# Questions - Inference
"""
Lecture (class) initial b0, b1 values and equation:
b0 = -0.0113
b1 = 0.9677
y-hat = 0.9677*x_i - 0.0113

a.) Ran the first 10 iterations and output results. See output after running the code (this model).

b.) Ran 10,000 iterations and optimized output of results to show 10 iterations at every 1,000 step (epoch).
"""

"""
References
- Lecture, lab, course materials
- ChatGPT
- Google
"""