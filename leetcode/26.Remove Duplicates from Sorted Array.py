class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
            else:
                i += 1
        return len(nums)
        

s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
result = s.removeDuplicates(nums)
print(result)