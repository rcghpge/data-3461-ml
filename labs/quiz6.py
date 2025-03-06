"""
Robert Cocker - 1441
DATA 3461 - Machine Learning
Dr. Jawad
2/21/2025
Quiz 6
"""
# Quiz 6
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import subprocess

# Load input data
df = pd.read_csv("C:/Users/Robert/Desktop/College/UT Arlington/DATA 3461 - Machine Learning/longley.csv", index_col=0)

x = df[["Employed"]]  # Ensure x is a DataFrame
y = df["GNP"]  # Target variable

x = sm.add_constant(x) # adds constant term to predictor

# Linear Regression Model
lr_model = sm.OLS(y,x).fit()

# We pick 100 points equally spaced from the min to the max
x_prime = np.linspace(x["Employed"].min(), x["Employed"].max(), 100)
x_prime = sm.add_constant(x_prime)  # Add constant for prediction


# We calculate the predicted value
y_hat = lr_model.predict(x_prime)

# Plot data
plt.figure()
plt.scatter(df["Employed"], df["GNP"], label="Actual Data")
plt.xlabel("Total Employment")
plt.ylabel("Gross National Product")
plt.plot(x_prime[:, 1], y_hat, color="red", alpha=0.9, label="Regression Line")
plt.legend()
plt.show()


# Save script and results into Markdown file
md_file = "C:/Users/Robert/Desktop/College/UT Arlington/DATA 3461 - Machine Learning/quiz6.md"

# Convert Markdown to PDF using Pandoc
pdf_file = "C:/Users/Robert/Desktop/College/UT Arlington/DATA 3461 - Machine Learning/quiz6.pdf"
command = ["pandoc", md_file, "-o", pdf_file, "--pdf-engine=xelatex"]

try:
    subprocess.run(command, check=True)
    print(f"PDF successfully generated: {pdf_file}")
except subprocess.CalledProcessError as e:
    print("Error:", e.stderr)
    
"""
# References
- Lecture, lab, and course materials
- ChatGPT
- Google
"""
