import math

x = int(input("Enter the value for x : "))
y = int(input("Enter the value for y : "))
x2 = pow(x,2)
y2 = pow(y,2)
distance = math.sqrt(x2 + y2)
s = x,y
print("Euclidean Distance from",s,"to Origin(0, 0) =",round(distance,2))