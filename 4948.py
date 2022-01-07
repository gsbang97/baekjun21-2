import sys
import math
def isPrime(num):
    if(num!=1):
        i = True
        for y in range(2,num//2):
            if(num%y == 0):
                i=False
                break 
            if(y*y>num):break
        if (i&(num!=4)): return i

def Prime(a,b):
    num = list()
    for x in range(a,b+1):
        if(isPrime(x)):
            num.append(int(x))
    return num
primes = Prime(2,123456*2)
sums = list()
while(True):
     max = 0
     min = 0
     i = int(sys.stdin.readline())
     if(i==0) : break;
     else:
        for x in range(i+1,i*2+1):
            if(isPrime(x)):
                min=primes.index(x)
                break
        for x in range(i*2,1,-1):
            if(isPrime(x)):
                max=primes.index(x)
                break
        sums.append(max-min+1)
for x in sums:
     print(x)    