import sys

i = int(sys.stdin.readline())
numbers = list()
for x in range(i):
    numbers.append(list(map(int,sys.stdin.readline().split())))
numbers.sort(key= lambda x:(x[0],x[1]))
for x in numbers:
    print(str(x[0])+" "+str(x[1]))
