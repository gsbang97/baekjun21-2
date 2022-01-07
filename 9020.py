import sys

def isPrime(num):
    if(num==2): return True
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
primes = Prime(1,10000)
inp = int(sys.stdin.readline())
exp = list()
for x in range(0,inp):
    num = int(sys.stdin.readline())
    is_finish = False
    prime = 0
    m = 0
    while(not is_finish):
        for x in range(num//2,1,-1):
            if(isPrime(x)):
                m=primes.index(x)
                break
        for y in range(m,-1,-1):
            if isPrime(num - primes[y]):
                is_finish = True
                prime = primes[y]
                break
    exp.append([num, prime])
for x in exp:
    print(str(x[1])+" "+str(x[0]-x[1]))
