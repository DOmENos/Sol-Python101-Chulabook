import math
r,theta = [float(i) for i in input().split()]
x = r * math.cos(theta)
y = r * math.sin(theta)

print(x, y)