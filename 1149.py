from sys import stdin
N = int(stdin.readline())
homeRGB = [[]for x in range(N)]
for x in range(N):
    rgb = list(map(int, stdin.readline().split()))
    if x == 0 :
        homeRGB[0]=rgb
    else :
        for j in range(3):
            if j == 0:
                homeRGB[x].append(rgb[j]+min(homeRGB[x-1][1],homeRGB[x-1][2]))
            elif j == 1:
                homeRGB[x].append(rgb[j]+min(homeRGB[x-1][0],homeRGB[x-1][2]))
            elif j == 2:
                homeRGB[x].append(rgb[j]+min(homeRGB[x-1][0],homeRGB[x-1][1]))    
print(min(homeRGB[-1]))