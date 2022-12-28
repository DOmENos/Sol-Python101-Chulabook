import math
x1,y1,x2,y2 = [float(i) for i in input().split()]
distance = math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2))

print(distance)
