nums=list(map(int,input().split(',')))
target=int((input()))
a=[0,1]
for i in range(0,len(nums)-1):
    print(i)
    for j in range(i+1,len(nums)):
        print("       ",j)
        if nums[i]+nums[j]==target:
            a[0]=i
            a[1]=j
            print(a)
            break

