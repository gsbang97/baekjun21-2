from sys import stdin
N = int(stdin.readline())
dp = [-1 for x in range(N+1)]
for i in range(1,N+1):
    dp[i] = dp[i-1]+1
    if(i%3 == 0):
        dp[i] = min(dp[i],dp[i//3]+1)
    if(i%2 == 0):
        dp[i] = min(dp[i],dp[i//2]+1)
print(dp[N])