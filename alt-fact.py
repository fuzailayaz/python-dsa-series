
class Solution:
    def factorial(self,n) -> int:
        # custom multiplication function (addition-based logic)
        def multiply(a,b):
            result = 0
            for _ in range(b): # Add 'a' exactly 'b' times.
                result += a
            return result
        fact = 1    # Start from initial factorial value -> 1
        for i in range(1, n+1): # Loop through '1' to - > 'n'
            fact = multiply(fact,i) # Multiply fact with i using 
                                    # custom multiplication function.
        return fact
sol = Solution()
print(f'Factorial of {5} is: {sol.factorial(5)}')
