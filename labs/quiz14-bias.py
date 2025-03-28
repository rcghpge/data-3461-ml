# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 11:37:37 2025

@author: rc
"""
"""
Robert Cocker
DATA 3461
Dr. Jawad
Quiz #14
3/28/2025
"""

# Quiz #14 + bias
import numpy as np

# AND gate inputs and outputs
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Outputs
y = np.array([0, 0, 0, 1])

# Add bias input of 1 to each input set
x = np.hstack((np.ones((x.shape[0], 1)), x))

# Initialize weights (including bias weight)
weights = np.random.rand(x.shape[1])

# Hyperparameters
learning_rate = 0.5
epochs = 5 # Increased number of epochs for better training

# Activation function (Step function)
def step_function(weighted_sum):
    return 1 if weighted_sum >= 0 else 0

# Training
for epoch in range(epochs):
    print(f"Epoch {epoch+1}")
    for i in range(len(x)):
        # Weighted sum
        weighted_sum = np.dot(x[i], weights)
        
        # Activation
        prediction = step_function(weighted_sum)
        
        # Error
        error = y[i] - prediction
        
        # Weight update
        weights += learning_rate * error * x[i]
        
        print(f"Inputs: {x[i][1:]}, Prediction: {prediction}, Error: {error}, Updated weights: {weights[1:]}, Bias weight: {weights[0]}")
        print("-------------------")

# Print final weights
print(f"Trained weights: {weights[1:]}, Bias weight: {weights[0]}")

# Testing the trained perceptron
print("\nTesting after training:")
for i in range(len(x)):
    weighted_sum = np.dot(x[i], weights)
    prediction = step_function(weighted_sum)
    print(f"Input: {x[i][1:]} -> prediction: {prediction}")
