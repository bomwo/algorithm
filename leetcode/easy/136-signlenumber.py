from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        test = {}
        for val in nums:
            test[val] = test.get(val, 0)+1

        for key, value in test.items():
            if value == 1:
                return key


if __name__ == "__main__":
    test = Solution()
    test.singleNumber([4,1,2,1,2])