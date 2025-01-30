class Solution:
    def maxSubArraySum(self, arr):
        max_so_far = float('-inf')
        max_ending_here = 0

        for num in arr:
            max_ending_here += num

            if max_ending_here > max_so_far:
                max_so_far = max_ending_here

            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far
    
sol = Solution()
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sol.maxSubArraySum(arr))