from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for value in range(nums.count(val)):
            nums.remove(val)

        return len(nums)
        #

if __name__ == "__main__":
    test = Solution()
    print(test.removeElement([3, 2, 2, 3], 2))