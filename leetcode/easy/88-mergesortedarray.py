from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m -1] > nums2[n -1]:
                nums1[m+n-1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n - 1]
                n -= 1
        while n > 0:
            nums1[n-1] = nums2[n-1]
            n -= 1

        return nums1


if __name__ == "__main__":
    test = Solution()
    print(test.merge([4,5,6,0,0,0],3,[1,2,3],3))
