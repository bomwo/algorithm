class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for a in s[::-1].split(" "):
            if a in '':
                pass
            else:
                return len(a)

# 그냥 순회하려다가 문자열을 뒤집어서 공백이 있으면 pass 아니면 바로 return 하게 했다
# 답은 맞을 것 같은데 뒤에 공백이 엄청 많은 문자열에서는 효율적이지 않을 듯
# 엇 그냥 split() 쓰면될듯 한줄로도 됨 위에꺼는 37ms 아래 코드는 23ms

    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


if __name__ == "__main__":
    test = Solution()
    print(test.lengthOfLastWord("luffy is still joyboy"))