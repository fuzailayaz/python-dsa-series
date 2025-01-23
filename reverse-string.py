class Solution:
    def reverse_string(self,s) -> str:
        stack = []
        # Push all the charecters to the stack 
        for char in s:
            stack.append(char)
        reversed_str = ''
        # Pop all the charecter's from the stack
        while stack:
            reversed_str += stack.pop()
        return reversed_str
sol = Solution()
s = "hello world"
print(sol.reverse_string(s))

# or more enhanced manner
class Solution:
    def reverse_string(self,s):
        return ''.join(reversed(s))
s = Solution()
st = 'hello'
print(s.reverse_string(st))