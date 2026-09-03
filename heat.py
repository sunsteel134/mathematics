import math
ans = 0
temp1 = 20
temp2 = 150
k = 0.007
x = 0.5
t = 200
l = 25
for i in range(2000):
    ans += ((math.sin(((x * (math.pi))/(2*l))*(2*i+1))*math.exp(-(((math.pi)**2)*((2*i+1)**2)*(k*t)/(4 * (l**2))))/(2*i+1)))
print(temp2+(ans * ((4*(temp1 - temp2))/(math.pi))))
