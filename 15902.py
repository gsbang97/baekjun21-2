import sys
import itertools

leng = int(sys.stdin.readline())
sys.stdin.readline()
line_1 = list()
for x in map(int,sys.stdin.readline().split()):
    if(x==1) : line_1.append(1)
    else :
        line_1.append(0)
        line_1.append(1)
line_2 = list()
sys.stdin.readline()
for x in map(int,sys.stdin.readline().split()):
    if(x==1) : line_2.append(1)
    else :
        line_2.append(0)
        line_2.append(1)
sp = 0
line = list()
for x in range(0,leng):
    if(line_2[x]==line_1[x]):
        line.append(line_1[sp:x])
        sp = x+1

print(line_1)
print(line_2)
print(line)
for x in line:
    sum = 0
    if x:
        line_x=itertools.permutations((range(1,len(x))))
        
        for y in line_x:
            a = list()
            b = True
            for z in y:
                if(z%2 == 0):
                    if(line_x.index(z-1)>z and line_x.index(z+1)>z):
                        b = False
                        break
            if(b): sum+=1
    print(sum)
        
                        
                




# deposition = 0
# for x in range(0,leng):
#     if((line_1[x]!=line_2[x] )and (line_1[x]==2)):
#         deposition+=1
#         line_1[x]=1
#         line_1[x+1]=1
# merge = 0
# for x in range(0,leng):
#     if((line_1[x]!=line_2[x]) and (line_2[x]==2)):
#         merge+=1
#         line_1[x]=2
#         line_1[x+1]=0
# mini = deposition+merge
# num = (factorial_for(deposition)+factorial_for(merge))%1000000007
