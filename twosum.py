'''famous two sumproblem
Problem:
You are given an array of integers and a target integer. Your task is to find two indices such that the sum of the numbers at those indices equals the target.

Input Format:
nums: An array of integers seperated by commas
target: An integer representing the target sum.
Output Format:
Return the indices of the two numbers such that they add up to the target. You can assume there is exactly one solution, and you may not use the same element twice.
'''
nums=list(map(int,input().split(',')))
target=int((input()))
a=[0,1]
for i in range(0,len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            a[0]=i
            a[1]=j
            break

print(a)
