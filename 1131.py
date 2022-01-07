import sys
def value(sum,y):
    i = []
    for z in range(15):   
        for y1 in str(sum):
            y2=1
            for y3 in range(y):
                y2 *= int(y1)
            sum+=y2
        i.append(sum)
    return min(i)
sum1 = 0
num = sys.stdin.readline().split(" ")
for x in range(int(num[0]), int(num[1])):
    sum1 += value(x,int(num[2]))
    print (sum1)
print(sum1)
        
        
        

        

