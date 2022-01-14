N, M, V = map(int,input().split())

node = [[]]*(N+1)
for x in range(M):
    num1, num2 = map(int, input().split())
    node[num1].append(num2)
    node[num2].append(num1) 

print (node)