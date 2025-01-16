from collections import defaultdict
class Solution:
    def subArrraysWithKdistinct(self, nums:list[int],k:int) -> int:
        def atmost(k):
            count = defaultdict(int)
            start, total = 0, 0
            for end in range(len(nums)):
                if count[nums[end]] == 0:
                    k -= 1
                count[nums[end]] += 1
                while k < 0:
                    nums[start] -= 1
                    if count[nums[start]] == 0:
                        k += 1
                        start += 1
                total += end - start + 1
            return total
        return atmost(k) - atmost(k-1)
sol = Solution()
nums = [1,2,1,2,3]
print(sol.subArrraysWithKdistinct(nums,2))