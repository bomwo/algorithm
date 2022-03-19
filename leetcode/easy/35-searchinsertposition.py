from typing import List


class Solution:
    def searchInsert(self, num: List[int], target: int):
        start, end = 0, len(num) - 1
        while start <= end:
            mid = (start + end) // 2

            if target <= num[mid]:
                end = mid - 1
            elif target == num[mid]:
                return mid
            elif target >= num[mid]:
                start = mid + 1

        return start
        #
        # return mid

test = Solution()
print(test.searchInsert([1,3,5,7], 1))
