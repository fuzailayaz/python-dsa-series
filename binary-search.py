class BinarySearch:
    def search(self, arr, target):
        '''
            Binary Search works on sorted arrays,   
        Paramenters:
            arr -> Sorted List in ascending order
            target -> Element which needs to be find/seached in the array
        Returns:
            Target Index else ->  -1
        '''
        left = 0
        right = len(arr) - 1

        while left <= right:
            # First Calculate mid # In order to avoid overflow condition
            mid = left + (right - left) // 2 
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                left =  mid + 1 # Target is in right - half
            else:
                right = mid - 1 # Target is in left - half
        return -1
sol = BinarySearch()
arr, target = [2,4,6,8,10,12,14], 4
print(sol.search(arr,target))