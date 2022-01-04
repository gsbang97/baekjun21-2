import sys

num1 = sys.stdin.readline().split(" ")
for x in range(int(num1[0]),int(num1[1])+1):
    if(x!=1):
        i = True
        for y in range(2,x//2):
            if(x%y == 0):
                i=False
                break 
            if(y*y>x):break
        if (i&(x!=4)): print(x)