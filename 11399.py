import sys

sys.stdin.readline()
times = list(map(int,sys.stdin.readline().split()))
times.sort()
sum = 0
for x in range(0,len(times)):
    for x in range(0, x+1):
       sum += times[x]
print(sum)