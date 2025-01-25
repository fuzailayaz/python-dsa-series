class Solution:
    def findleaders(self,arr):
        n = len(arr)
        leaders = []
        max_from_right = arr[-1]
        # add/append the last elements of the array to the leaders list
        leaders.append(max_from_right)

        # Now traverse the element from right side of the array
        for i in range(n-2, -1, -1): # Start,stop & step
            if arr[i] > max_from_right:
                max_from_right = arr[i]
                leaders.append(max_from_right)
        # Now since the list is in reverse order as per our
        #  coding logic so we will reverse again in order to get the correct list
        return leaders[::-1]
sol = Solution()
arr = [16,17,4,3,5,2]
print(f"leaders of the array are elements in the array: {sol.findleaders(arr)}")
