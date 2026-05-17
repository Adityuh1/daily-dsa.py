class Solution(object):
    def removeElement(self, nums, val):
        n = len(nums)
        # print(n)
        k = 0
        for i in range(n):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
                    
s = Solution()
nums = [3,2,2,3]
val = 3
result = s.removeElement(nums, val)
print(result)            