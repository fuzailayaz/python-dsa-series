class Solution:
    def subArraySum(self, nums:list[int], k:int) -> int:
        res, curSum = 0, 0
        prefixSum = {0: 1}
        for n in nums:
            curSum += 1
            diff = curSum - k

            res += prefixSum.get(diff,0)
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)
        return res
sol = Solution()
nums = [1,1,1]
print(sol.subArraySum(nums,2))