class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return f"{bin(int(a,base=2) + int(b,base=2))[2:]}"


if __name__ == "__main__":
    test = Solution()
    print(test.addBinary("1010","1011"))