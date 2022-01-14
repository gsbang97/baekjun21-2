
from sys import stdin
zeros=[0 for x in range(41)]
ones=[0 for x in range(41)]
for x in range(0,41):
    if(x == 0):
        zeros[x] = 1
        ones[x] = 0
    elif(x==1):
        zeros[x] = 0
        ones[x] = 1
    else:
        zeros[x] = zeros[x-1]+zeros[x-2]
        ones[x] = ones[x-1]+ones[x-2]
T = int(stdin.readline())
s = ""
for x in range(T):
    N = int(stdin.readline())
    s += str(zeros[N])+" "+str(ones[N])+"\n"
print(s)
