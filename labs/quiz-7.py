# -*- coding: utf-8 -*-
"""
Robert Cocker
DATA 3461 
Dr. Jawad
2/28/2025
Quiz 7
"""

# Quiz 7
from fpdf import FPDF
import numpy as np
from sklearn import datasets, linear_model

# Load data
diabetes_x, diabetes_y = datasets.load_diabetes(return_X_y=True)

# Verify datasets
print("Input Data Shape:")
print(diabetes_x.shape, diabetes_y.shape)
print()

# Features
diabetes_x = diabetes_x[:, np.newaxis, 2]

# Generat LR object
regr_linear = linear_model.LinearRegression()
regr_lasso = linear_model.Lasso(alpha=0.1)
regr_ridge = linear_model.Ridge(alpha=0.1)

# Train models
lr = regr_linear.fit(diabetes_x, diabetes_y)
lasso = regr_lasso.fit(diabetes_x, diabetes_y)
ridge = regr_ridge.fit(diabetes_x, diabetes_y)

# Linear coefficients
print("Regression Model Summary and Results:\n")
print("Linear Coefficient:\n", lr.coef_, "\n")
print("Lasso Coefficient:\n", lasso.coef_, "\n")
print("Ridge Coefficient:\n", ridge.coef_)

# Create PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

# Write results
pdf.cell(200, 10, "Regression Model Summary and Result Coefficients", ln=True, align="C")
pdf.ln(10)
pdf.multi_cell(0, 10, f"Linear Coefficients: {lr.coef_}")
pdf.multi_cell(0, 10, f"Lasso Coefficients: {lasso.coef_}")
pdf.multi_cell(0, 10, f"Ridge Coefficients: {ridge.coef_}")

# Save PDF
pdf.output("quiz-7.pdf")

print("Results saved to pdf output file")

