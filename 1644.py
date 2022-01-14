import sys
a= 5000000
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
num = int(sys.stdin.readline())
s=0
index = 0
leng = len(p)
temp_num=num
temp_index = 0
while(num>= p[index]):
    for x in range(index, 300000):
        temp_num -= p[x]
        if(temp_num<0) : 
            temp_num += p[x]+p[temp_index] 
            temp_index+=1   
            index = x
            break
        elif(temp_num==0) : 
            temp_num += p[temp_index]
            temp_index+=1   
            index = x+1
            s+=1
            break
print(s)
