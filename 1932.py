from sys import stdin
N = int(stdin.readline())
numTriangle = list()
maxTriangle = list()
for x in range(N):
    maxTriangle.append([0 for _ in range(x+1)])
    tmp = list(map(int,stdin.readline().split()))
    numTriangle.append(tmp)
maxTriangle[0][0] = numTriangle[0][0]
for x in range(1,N):
    for y in range(0,x+1):
        if y == x :
            maxTriangle[x][y] = maxTriangle[x-1][y-1]+numTriangle[x][y]
        elif y == 0 :
            maxTriangle[x][y] = maxTriangle[x-1][y]+numTriangle[x][y]
        else:
            maxTriangle[x][y] = max(maxTriangle[x-1][y-1],maxTriangle[x-1][y]) + numTriangle[x][y]

# def triangle(tmp,n,index):
#     print(tmp)
#     if n == N-1:
#         if tmp > maxTriangle[n][index]:
#             maxTriangle[n][index] = tmp    
#         return 0
    
#     if tmp >= maxTriangle[n][index]:
#         maxTriangle[n][index] = tmp
#         triangle(tmp+numTriangle[n+1][index],n+1,index)
#         triangle(tmp+numTriangle[n+1][index+1],n+1,index+1)
# triangle(numTriangle[0][0],0,0)
print(max(maxTriangle[-1]))