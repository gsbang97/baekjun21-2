import sys

def Prime(a,k):
    num = list(range(2,a+1))
    m=0
    i = 0
    primes = list()
    while(len(num)>0):
        m=min(num)
        primes.append(m)
        for x in range(m,a+1,m):
            if x in num:
                num.remove(x)
                i+=1
                if(i==k):
                    print(x)
            
    return primes

i = list(map(int,sys.stdin.readline().split()))
Prime(i[0],i[1])
