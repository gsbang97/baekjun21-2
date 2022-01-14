import sys
import math
num = int(sys.stdin.readline())
strs = [0]*26
strs_2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
m=0
for x in range(0,num):
    s = sys.stdin.readline()[:-1]
    a=1
    for y in s:
        strs[strs_2.index(y)] += int(math.pow(10,len(s)-a))
        a +=1   
sum = 0
strs.sort(reverse=True)
for x in range(10):
    sum += strs[x]*(9-x)
print(sum)

