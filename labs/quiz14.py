# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 11:01:34 2025

@author: rc
"""

"""
Robert Cocker
DATA 3461
Dr. Jawad
Quiz #14
3/28/2025
"""

# Quiz #14
import numpy as np

# AND gate inputs and outputs 
x = np.array([[0,0],[0,1],[1,0],[1,1]])

# Outputs
y = np.array([0,0,0,1])

# Initialize weights
weights = np.array([1.2,0.6])

# Hyperparamters
threshold = 1.0
learning_rate = 0.5
epochs = 2

# Activation function (Stepwise function with threshold)
def step_function(weighted_sum):
    return 1 if weighted_sum >= threshold else 0

# Training
for epoch in range(epochs):
    print(f"Epoch {epoch+1}")
    for i in range(len(x)):
        
        # Weighted sum (no bias term)
        weighted_sum = np.dot(x[i],weights)
        
        # Activation
        prediction = step_function(weighted_sum)
        
        # Error
        error = y[i] - prediction
        
        # Weight update
        weights += learning_rate * error * x[i]
        print(f"Inputs: x[i], Prediction: {prediction}, Error: {error}, Updated weights: {weights}, Weighted sum: {weighted_sum}")
        print("-------------------")
        
# Print final weights
print(f"Trained weights: {weights}")

# Testing the trained perceptron
print("\nTesting after training:")
for i in range(len(x)):
    weighted_sum = np.dot(x[i], weights)
    prediction = step_function(weighted_sum)
    print(f"Input: {x[i]} -> prediction: {prediction}")


# Console output
"""
%runfile C:/Users/rcock/Desktop/mini-project3.py --wdir
Epoch 1
Inputs: x[i], Prediction: 0, Error: 0, Updated weights: [1.2 0.6], Weighted sum: 0.0
-------------------
Inputs: x[i], Prediction: 0, Error: 0, Updated weights: [1.2 0.6], Weighted sum: 0.6
-------------------
Inputs: x[i], Prediction: 1, Error: -1, Updated weights: [0.7 0.6], Weighted sum: 1.2
-------------------
Inputs: x[i], Prediction: 1, Error: 0, Updated weights: [0.7 0.6], Weighted sum: 1.2999999999999998
-------------------
Epoch 2
Inputs: x[i], Prediction: 0, Error: 0, Updated weights: [0.7 0.6], Weighted sum: 0.0
-------------------
Inputs: x[i], Prediction: 0, Error: 0, Updated weights: [0.7 0.6], Weighted sum: 0.6
-------------------
Inputs: x[i], Prediction: 0, Error: 0, Updated weights: [0.7 0.6], Weighted sum: 0.7
-------------------
Inputs: x[i], Prediction: 1, Error: 0, Updated weights: [0.7 0.6], Weighted sum: 1.2999999999999998
-------------------
Trained weights: [0.7 0.6]

Testing after training:
Input: [0 0] -> prediction: 0
Input: [0 1] -> prediction: 0
Input: [1 0] -> prediction: 0
Input: [1 1] -> prediction: 1

File naming conventions were renamed during submission. This is a quiz and not a mini-project. 
"""
