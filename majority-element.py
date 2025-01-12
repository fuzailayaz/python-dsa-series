'''class Solution:
    def majorityElement(self,nums:list[int]) -> int:
        ans,count  = -1,0
        for num in nums:
            if count == 0:
                ans = num
            if ans == count:
                count -= 1
            else:
                count += 1
        return ans
sol = Solution()
nums = [2,2,1,1,1,2,2]
print(sol.majorityElement(nums)) '''

class Solution:
    def majorityElement(self,nums:list[int]) -> int:
        res, count = 0,0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res
sol = Solution()
nums = [2,2,1,1,1,2,2]
print(sol.majorityElement(nums))