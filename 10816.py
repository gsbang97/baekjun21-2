input()
nums = [0]*20000001
for x in list(map(int, input().split())):
    nums[x+10000000] += 1
input()
nums2 = list(map(int, input().split()))
for x in nums2:
    print(nums[x+10000000],end=("\n" if x==nums2[len(nums2)-1]  else" "))