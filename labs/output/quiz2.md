# Quiz 2
```python
import numpy as np import matplotlib.pyplot as plt
```

# Array
```python
data1 = \[85, 62, 78, 64, 25, 12, 74, 96, 63, 45, 78, 20, 5, 30, 45, 78,
45, 96, 65, 45, 12, 74, 78, 23, 8\]
```
# Statistical Summary
```python
print("Quiz 2 - Statistical Summary Overview:")

max = np.max(data1) print("Max:{0:d}".format(max))

min = np.min(data1) print("Min:{0:d}".format(min))

mean = np.mean(data1) print("Mean:{0:8.4f}".format(mean))

variance = np.var(data1) print("Variance: {0:8.4f}".format(variance))

standarddev = np.std(data1) print("STD: {0:8.4f}".format(standarddev))

median = np.median(data1) print("Median: {0:8.4f}".format(median))

# Data visualizations

hist1, edges1 = np.histogram(data1) plt.bar(edges1\[:-1\], hist1, width
= edges1\[1:\] - edges1\[:-1\], edgecolor = 'k') plt.title("Data Array")
plt.show()
```
# References:
```python
"""
- Grok 2
"""
```
