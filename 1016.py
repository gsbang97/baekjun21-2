import sys
import math
def Prime(a,b):
    num = list()
    for x in range(a,b+1):
        if(isPrime(x)):
            num.append(int(x))
    return num
def isPrime(num):
    if(num!=1):
        i = True
        for y in range(2,num//2):
            if(num%y == 0):
                i=False
                break 
            if(y*y>num):break
        if (i&(num!=4)): return i
sum=1
# i = sys.stdin.readline().split()
# print(i)
# max=2
# if(int(i[0])>4):
#     for x in range(int(int(i[0])/2),0,-1):
#         if(isPrime(x)):
#             print(x)
#             max=x
#             break
n=2
while(sum<1000):
    if(isPrime(n)):sum = sum* n
    n += 1
print(n)
# prime = Prime(2,int(i[0]))
# print(prime)
# for x in range(int(i[0]),int(i[1])+1):
#     if(isPrime(x)): prime.append(x)
#     p=True
#     for y in prime:
#         j = (math.pow(y,2))
#         if(j>x):
#             break
#         elif(x%int(j) == 0):
#             p=False
#             break
#     if(p):
#         sum+=1
# print(sum)

