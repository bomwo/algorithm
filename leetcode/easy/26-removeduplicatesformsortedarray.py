from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicate = 0

        for val in range(1, len(nums)):
            if nums[val] == nums[val - 1]:
                duplicate += 1
            else:
                nums[val - duplicate] = nums[val]

        return len(nums) - duplicate
