from math import sqrt

pointA = [0, 0]
pointB = [3, 4]

def calc(x, y):
    z = [y[0] - x[0], y[1] - x[1]] # y - x
    length = abs(sqrt(z[0]**2 + z[1]**2)) 
    return length

print(calc(pointA, pointB))