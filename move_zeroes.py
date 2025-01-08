class MoveZeros:
    def __init__(self,nums):
        self.nums = nums
    def move_zeros(self):
        l, r = 0, 0
        while r < len(self.nums):
            if self.nums[r] != 0:
                self.nums[l], self.nums[r] = self.nums[r], self.nums[l]
                l += 1
            r += 1
        return self.nums
if __name__ == '__main__':
    nums = [0,1,0,3,12]
    move_zeros = MoveZeros(nums)
    print(move_zeros.move_zeros())