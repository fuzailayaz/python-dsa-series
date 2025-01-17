from collections import defaultdict
class Solution:
    def subArrraysWithKdistinct(self, nums:list[int],k:int) -> int:
        def atmost(k):
            count = defaultdict(int)
            subarrays = []
            left, result = 0, 0
            for right in range(len(nums)):
                if count[nums[right]] == 0:
                    k -= 1
                count[nums[right]] += 1
                
                while k < 0:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        k += 1
                    left += 1
                
                for i in range(left, right + 1):
                    subarrays.append(nums[i:right + 1])

                result += right - left + 1
            return result, subarrays
        atmost_k, subarrays_k = atmost(k)
        atmost_k_minus1, _ = atmost(k - 1)
        subarrays_exact_k = [sub for sub in subarrays_k if len(set(sub)) == k]
        print("SubArrays with exactly {} distinct integers".format(k))
        for subarray in subarrays_exact_k:
            print(subarray)
        return atmost_k - atmost_k_minus1
sol = Solution()
nums = [1,2,1,2,3]
print(sol.subArrraysWithKdistinct(nums,2))