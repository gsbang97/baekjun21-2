import sys

count = [0] * (10000)
i = 0
for x in range(int(sys.stdin.readline())):
    j = int(sys.stdin.readline())
    if i < j: i=j
    count[j-1] += 1

for j in range(i):
    for k in range(count[j]):
        print(j+1)