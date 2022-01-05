import sys
i = sys.stdin.readline()
numbers = [False]*2001
for x in sys.stdin.readline().split(" "):
    if not numbers[int(x)+1000]: numbers[int(x)+1000] = True
isFirst = True
for x in range(2001):
    if(numbers[x]):
      if(isFirst):
        print(x-1000,end="")
      else:
        print(" "+str(x-1000),end="")
      isFirst = False