class Solution:
    def findMax(self,nums:list[int]) -> int:
        max_sum = float('-inf')
        for n in nums:
            if n > max_sum:
                max_sum = n
        return max_sum
s = Solution()
nums = [1,2,3,4,5,6,7,8,9,10]
print(s.findMax(nums))

''' or simply 
    def findMax(self,nums):
        return max(nums)
'''