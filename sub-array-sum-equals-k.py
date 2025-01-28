class Solution:
    def subArraySum(self, nums:list[int], k:int) -> int:
        '''
        Variables:-
            res -> used to store how many subarrays are there whose 
                   sum is = k
            curSum -> count the sum of particular usb-array
            prefixSum -> A Dictionary used to store the freq. of each unique
                        element and tell it's count/freq.
            diff -> Tells/ Calculate that if there exists 
                    any subarray whose sum is equals to k
        '''
        res, curSum = 0, 0
        prefixSum = {0: 1}
        for n in nums:
            curSum += 1
            diff = curSum - k

            res += prefixSum.get(diff,0)
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)
        return res
sol = Solution()
nums = [1,1,1]
print(sol.subArraySum(nums,2))