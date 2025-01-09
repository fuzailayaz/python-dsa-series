class Solution:
    def checkSubArraySum(self,nums:list[int],k:int) -> bool:
        remainder = {0: -1}
        total = 0
        for i,n in enumerate(nums):
            total += n
            r = total % k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True
        return False
sol = Solution()
result = sol.checkSubArraySum([23,2,6,4,7],6)
print(result)