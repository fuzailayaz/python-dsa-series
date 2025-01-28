class Solution:
    def countFreq(self, arr, target):
        left, right, result = 0, len(arr) - 1, -1
        # result is used to store the last index at which target is found
        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                result = mid
                left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if result == -1:
            return 0
        
        first = result # first is used to store the index of 
        # the first occurance at which target is found

        #  to check the the remaining left portion after the first occurance 
        while first > 0 and arr[first - 1] == target:
            first -= 1
        return result - first + 1

sol = Solution()
arr, target = [1,1,2,2,2,3,4,4,4,4], 4
print(sol.countFreq(arr, target))            