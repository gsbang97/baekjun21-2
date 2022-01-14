import sys
num = int(sys.stdin.readline())
def fib(n):
    fibList=[1, 1]
    if n==1 or n==2:
        return 1
    for i in range(2,n):
        fibList.append( fibList[i-1] + fibList[i-2] )
    return fibList
if(num == 0):
    print(0)
elif num==1 or num==2:
    print(1)
else:
    print(fib(num)[num-1])