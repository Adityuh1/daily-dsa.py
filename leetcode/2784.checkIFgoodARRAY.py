class Solution(object):
    def isGood(self, nums):
        max_ele = 0
        n = len(nums)
        
        nums.sort()
        for i in range(n-1):
            print(nums[i])
            if nums[i] != i + 1:
                return False
        for i in nums:
            if i > max_ele:
                max_ele = i
            else:
                print(max_ele)
        if nums[n-2] == max_ele and nums[n-1] == max_ele - 1:
            return True
        else:
            return False
        
        
s = Solution()
# nums = [1,2,2,1]
# nums = [1,2,3,1]
nums = [9,9]


result = s.isGood(nums)
print(result)