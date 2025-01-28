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
        ans, count = -1,0

        for n in nums:
            if count == 0:
                ans = n
            count += (1 if n == ans else -1)
        if nums.count(ans) > len(nums) // 2:
            return ans
        return -1
    
sol = Solution()
nums = [2,2,1,1,1,2,2]
nums1 = [61,13]
print(sol.majorityElement(nums1))