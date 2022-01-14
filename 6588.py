import sys
a= 10000000
primes=list(range(0,a+1))
primes[0]=-1
primes[1]=-1
p = list()
for x in range(2,a+1):
    if(x*x>a):break
    if(primes[x]==x):
        for y in range(x,a+1,x):
            primes[y] = x
for x in range(2,a+1):
    if(x == primes[x]):
        p.append(x)
# #while(True):
for num in range(6,1000000,2):
#    num = int(sys.stdin.readline())
    if(num==0) : break
    for y in p:
        if primes[num-y]== num-y:
            print(str(num)+" = "+str(y)+" + "+str(num-y))
            break
# print(s)
# # for x in exp:
# #     print(x)
