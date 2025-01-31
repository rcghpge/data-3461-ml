# ML Lab - Quiz #1

# Question 1
# For Loop Statement:
```python
print("DATA-3461 ML Lab - Quiz #1 Solutions:")
print("For Loop run:")
for x in range(1, 6):
    print(x)

print("\n")
```
# While Loop Statement:
```python
print("While Loop run:")
a, b = 1, 5
while (a <=b):
    print(a)
    a += 1

print("\n")
```
# Question 2
# Range Function:
```python
print("Range Function Output:")
range(1, 14, 4)
print(list(range(1, 14, 4)))
print("\n")
```
# Question 3
# Math library:
```python
import math

print("Square Root Function from Math Library:")
x = math.sqrt(123)
print(x)
print("\n")
```
# Question 4
# Sin, Cos, and Pi from Math Library
```python
from math import sin, cos, pi

print("Sin, Cos, and Pi from Math Library:")
print(sin(1/2))
print(cos(pi/2))
print("\n")
```
# Question 5
# Writing Custom Functions in Python
```python
def cube(x):
    y = x*x*x
    return y

print("Cube Function:")
z = cube(5)
print(z)
print("\n")
```
# Question 6 (Optional - Bonus Question)
# Calculate the area of a rectangle
```python
print("Area of a Rectangle:")
def rect_area(p, q):
    r = p*q
    return r

a = rect_area(5, 6)
print(a)
```
