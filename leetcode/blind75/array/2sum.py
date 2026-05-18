class Solution(object):
    def twoSum(self, nums , target):
        n = len(nums)
        for i in range(0 , n -1):
            for j in range(i+1 , n-1):
                if nums[i] + nums[j] == target:
                    return True , i , j
                
        
s = Solution()
N =5
nums = [2,6,5,8,11]
target = 14
result = s.twoSum(nums , target)
print(result)