class Solution:
    def numSubArrayProductLessThanK(self, nums:list[int], k:int) -> int:
        res, l = 0, 0
        product = 1
        for r in range(len(nums)):
            product *= nums[r]
            while product >= k:
                product //= nums[l]
                l += 1
            res += (r - l + 1)
        return res
sol = Solution()
nums = [10,5,2,6]
print(sol.numSubArrayProductLessThanK(nums,100))