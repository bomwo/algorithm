

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # x 가 양수면 0보다 크고 and 문자열 뒤집었을때 같아야함
        # 다만 >로 썼었는데 0일때 케이스는 생각하지 못했음.
        if x >= 0 and str(x) == str(x)[::-1]:
            return True
        else:
            return False
        # x 가 음수면 대칭이 될 수 없다.


if __name__ == "__main__":
    test = Solution()
    print(test.isPalindrome(0))