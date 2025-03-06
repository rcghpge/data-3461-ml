# GNP vs Employed Regression Report

## Python Script

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import subprocess
import os

# Load input data
df = pd.read_csv("C:/Users/Robert/Desktop/longley.csv", index_col=0)

x = df[["Employed"]]
y = df["GNP"]

x = sm.add_constant(x)

lr_model = sm.OLS(y, x).fit()
print(lr_model.summary()) 
print(lr_model.params)

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

```

## Regression Model Summary

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                    GNP   R-squared:                       0.967
Model:                            OLS   Adj. R-squared:                  0.965
Method:                 Least Squares   F-statistic:                     415.1
Date:                Fri, 21 Feb 2025   Prob (F-statistic):           8.36e-12
Time:                        12:17:12   Log-Likelihood:                -68.391
No. Observations:                  16   AIC:                             140.8
Df Residuals:                      14   BIC:                             142.3
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const      -1430.4823     89.361    -16.008      0.000   -1622.142   -1238.822
Employed      27.8363      1.366     20.374      0.000      24.906      30.767
==============================================================================
Omnibus:                        1.033   Durbin-Watson:                   1.530
Prob(Omnibus):                  0.597   Jarque-Bera (JB):                0.836
Skew:                          -0.499   Prob(JB):                        0.658
Kurtosis:                       2.491   Cond. No.                     1.26e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.26e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
```

## Model Coefficients

```
const      -1430.482314
Employed      27.836256
dtype: float64
```

## Regression Plot

![Regression Plot](gnpemployedplot.png)
