import sys
a= 9999
primes=list(range(0,a+1))
p = list()
for x in range(2,a+1):
    if(x*x>a):break
    if(primes[x]==x):
        for y in range(x,a+1,x):
            primes[y] = x
for x in range(0,1000):
    primes[x] = -1
for x in range(2,a+1):
    if(x == primes[x]):
        p.append(x)
# i = int(sys.stdin.readline())
# prime_1, prime_2 = map(int,sys.stdin.readline().split())
def prime_able(prime):
    ables = list()
    for x in range(1,10):
        prime_s = prime-(prime%10) +x
        if(primes[prime_s]==prime_s and prime_s!=prime) : ables.append(prime_s)
    for x in range(0,10):
        prime_s = prime-((prime//10)%10)*10 +x*10
        if(primes[prime_s]==prime_s and prime_s!=prime) : ables.append(prime_s)
    for x in range(0,10):
        prime_s = prime-(prime//100)%10*100 +x*100
        if(primes[prime_s]==prime_s and prime_s!=prime) : ables.append(prime_s)
    for x in range(1,10):
        prime_s = prime-(prime//1000)*1000 +x*1000
        if(primes[prime_s]==prime_s and prime_s!=prime) : ables.append(prime_s)
    
    return ables
print(prime_able(1033))
print(prime_able(8179))
# # #while(True):
# for num in range(6,1000000,2):
# #    num = int(sys.stdin.readline())
#     if(num==0) : break
#     for y in p:
#         if primes[num-y]== num-y:
#             print(str(num)+" = "+str(y)+" + "+str(num-y))
#             break
# # print(s)
# # # for x in exp:
# # #     print(x)
