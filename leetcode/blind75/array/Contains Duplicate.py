class Solution(object):
    def containsDuplicate(self, nums ):
        n = len(nums)
        nums.sort()
        for i in range(0 , n -1):
            if nums[i] == nums[i + 1]:
                return True
                
        
s = Solution()
nums = [1, 2, 3, 1]
print(True if s.containsDuplicate(nums) else False)