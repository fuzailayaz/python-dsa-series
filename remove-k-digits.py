class Solution:
    def removekdigits(self, num: str, k:int) -> int:
        stack = []
        for c in num:
            while k > 0 and stack and stack[-1] > c:
                k -= 1
                stack.pop()
            stack.append(c)
        stack = stack[:len(stack) - k]
        res = "".join(stack)
        return str(int(res)) if res else '0'
sol = Solution()
num = "1432219"
print(sol.removekdigits(num,3))