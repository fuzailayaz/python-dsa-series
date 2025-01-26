class Solution:
    def rangeSumPrefix(self,arr,queries):
        n = len(arr)
        prefix = [0] * (n+1)
        # Compute prefix Sum
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + arr[i-1]

        result = []
        for l, r in queries:
            result.append(prefix[r] - prefix[l-1])
        return result
sol = Solution()
arr, queries = [2,4,6,8,10], [(2,4),(1,5)]
print(sol.rangeSumPrefix(arr,queries))