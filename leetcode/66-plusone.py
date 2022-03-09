from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = str()
        for value in digits:
            s += str(value)
        s = int(s) + 1
        return [a for a in str(s)]

# 근데 타입을 바꾸면서 하는건 좋지 않을 것 같은데 나중에 다시 풀기
# 일단 코드는 성공했다.
# tip : ''.join(map(str, ['1','2','3'])) <- list를 하나로 뭉칠 수 있다


if __name__ == "__main__":
    test = Solution()
    print(test.plusOne([9]))