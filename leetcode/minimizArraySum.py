class Solution(object):
    def minArraySum(self, nums):
        # n = len(nums)
        # # print(n)
        # for num in nums:
            
        #     if num > 3:
        #         a = nums.index(num)
        #         b = nums.index(num) + 1
        #         # print(a ,b)            
        #     else:
        #         a = 1
        #         b = 2
        #     if nums[a] % nums[b] == 0:
        #         nums[a] = nums[b]
        #     result = sum(nums)
        #     return result
            #########################
        for num in nums:
            if num > 3:
                a = nums.index(num)
                b = nums.index(num) + 1
                print(a ,b)     
                if nums[a] % nums[b] == 0:
                    nums[a] = nums[b]
                
            else:
                a = 0
                b = 1
                if nums[a] % nums[b] == 0:
                    nums[a] = nums[b]
        result = sum(nums)
        return result
            
            
            
            
s = Solution()
nums = [4,2,8,3]
# nums = [3,6,2]
result = s.minArraySum(nums)
print(result)