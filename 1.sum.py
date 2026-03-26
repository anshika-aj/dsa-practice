class Solution(object):
    def twoSum(self, nums, target):
        for n in range(len(nums)):
            for m in range(n+1,len(nums)):
                temp=nums[n]+ nums[m]
                if temp==target :   
                   return [n,m]

obj=Solution()
arr=[2,3,4,5]
solution= obj.twoSum(arr,9)
print(solution)