import sys
import math
i = int(sys.stdin.readline())
numbers = list()
q = list()
for x in range(i):
    numbers = (list(map(int,sys.stdin.readline().split())))
    abr =math.sqrt(math.pow(numbers[0]-numbers[3],2)+math.pow(numbers[1]-numbers[4],2))
    ab = numbers[2]+numbers[5]
    if(numbers[0]==numbers[3] and numbers[1]==numbers[4] and numbers[2]==numbers[5]):
        q.append(-1)
    elif(numbers[0]==numbers[3] and numbers[1]==numbers[4]):
        q.append(0)
    elif(abr==ab or abr == abs(numbers[2]-numbers[5])):
        q.append(1)
    elif(abr<ab and abr > abs(numbers[2]-numbers[5])):
        q.append(2)
    else:
        q.append(0)
for x in q:
    print(x)