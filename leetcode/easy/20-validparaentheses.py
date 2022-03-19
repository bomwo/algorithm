class Solution:
    def __init__(self):
        self.value = {
            '{': '}',
            '[': ']',
            '(': ')',
        }

    def isValid(self, s: str) -> bool:
        stack = list()
        if len(s) % 2 == 0:
            for value in s:
                if value in self.value.keys():
                    stack.append(value)
                elif value in self.value.values():
                    if stack == [] or self.value[stack.pop()] != value:
                        return False
                else:
                    return False
            return stack == []
        else:
            return False

if __name__ == "__main__":
    test = Solution()
    print(test.isValid('{{[(}}'))