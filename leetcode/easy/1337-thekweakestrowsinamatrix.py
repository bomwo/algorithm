from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dict = {}
        list = []
        for index, value in enumerate(mat):
            dict[index] = value.count(1)

        # print(dict)
        test_dict = sorted(dict.items(), key=lambda item: item[1])
        for a,v in test_dict[:k]:
            list.append(a)
        # list 필요없을듯
        return list


if __name__ == "__main__":
    test = Solution()
    mat = [[1,1,0,0,0],
         [1,1,1,1,0],
         [1,0,0,0,0],
         [1,1,0,0,0],
         [1,1,1,1,1]]
    k = 3
    test.kWeakestRows(mat,k)