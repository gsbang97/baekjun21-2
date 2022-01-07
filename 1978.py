import sys

def isPrime(num):
    if(num!=1):
        i = True
        for y in range(2,num//2):
            if(num%y == 0):
                i=False
                break 
            if(y*y>num):break
        if (i&(num!=4)): return i
sum = 0
i = sys.stdin.readline()
num = list(map(int,sys.stdin.readline().split(" ")))
for x in num:
    if(isPrime(x)):sum+=1
print(sum)