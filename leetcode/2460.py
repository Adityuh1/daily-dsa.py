class Solution(object):
    def applyOperations(self, nums):
        n = len(nums)
        zero_pointer = 0
        for i in range(n):
            if i < n-1 and nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            if nums[i] != 0:
                nums[zero_pointer] , nums[i] = nums[i] , nums[zero_pointer]
                zero_pointer += 1
        return nums

s = Solution()

nums = [1,2,2,1,1,0]
result = s.applyOperations(nums)
print(result)