from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for val in nums:
            dict[val] = dict.get(val, 0) + 1

        sorted_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)

        return sorted_dict[0][0]

if __name__ == "__main__":
    test = Solution()
    test.majorityElement([3,2,3])
