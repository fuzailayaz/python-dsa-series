class MoveZeros:
    def move_zeros(self, nums):
        l, r = 0, 0
        while r < len(nums):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
        return nums
nums = [0, 1, 0, 3, 12]
sol = MoveZeros()
print(sol.move_zeros(nums))
