class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        last_org= 0
        leng=len(nums)
        for i in range(1,leng):
            if nums[last_org]!=nums[i]:
                last_org+=1
                nums[last_org] = nums[i]
        return last_org+1