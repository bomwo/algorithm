from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 첫번째 풀이
        # result = ""
        # for value in zip(*strs):
        #     # print(set(value))
        #     if len(set(value)) == 1:
        #        result += set(value).pop(0)
        # return result
        # ["car", "cir"] 를 만족 못하는 케이스

        # result = ""
        # last_index = 0
        # for index, value in enumerate(zip(*strs)):
        #     if len(set(value)) == 1:
        #         if index == 0 or last_index == index - 1:
        #             last_index = index
        #             result += set(value).pop()
        # return result
        # ["babb","caa"] 케이스를 확인 못함 return ""

        result = ""
        for value in zip(*strs):
            # print(set(value))
            if len(set(value)) == 1:
               result += set(value).pop(0)
            else: # 첫번째 케이스에서 else 만 추가하면됨 왜냐하면 연속적인 값이어야하는데 1이 아니면 바로 중단하면되기때문
                break
        return result





if __name__ == "__main__":
    test = Solution()
    print(test.longestCommonPrefix(["babb","caa"]))