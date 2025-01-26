class Solution:
    def findleaders(self,arr):
        n = len(arr)
        max_from_right = arr[n-1]
        leaders = [max_from_right]

        # Now traverse the element from right side of the array
        for i in range(n-2, -1, -1): # Start,stop & step
            if arr[i] >= max_from_right:
                max_from_right = arr[i]
                leaders.append(arr[i])
        # Now since the list is in reverse order as per our coding logic
        # so we will reverse again in order to get the correct list
        return leaders[::-1]
sol = Solution()
arr = [61,61,17]
print(f"leaders of the array are elements in the array: {sol.findleaders(arr)}")
