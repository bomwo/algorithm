class Solution:
    '''
    비즈니스 로직
    로마 숫자는 왼쪽에서 오른쪽으로 갈때 큰숫자에서 작은 숫자대로 표기함
    근데 만약 아래의 예시처럼 오면 뒤에서 앞숫자를 빼기가 된다.
    ex ) I 뒤에 V(5) , X(10)이오면 4, 9 빼기가 된다
         X  L(50) , C(100) 이오면 40, 90가 된다.

    병우 궁금중 2단계 말고 더 큰 숫자와도 빼야되나? 일단 돌려보자.
    '''

    def __init__(self):
        value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        self.value = value

    def romanToInt(self, s: str) -> int:
        prefix = s[0]
        result = self.value.get(s[0])
        for value in range(1,len(s)):
            if self.value.get(prefix) < self.value.get(s[value]):
                result += self.value.get(s[value]) - 2 * self.value.get(prefix)
                prefix = s[value]
            else:
                result += self.value.get(s[value])
                prefix = s[value]

        return result
        # 나랑 같은 방식인데 아래것이 더 깔끔한 것 같다.
        # result = 0
        # prev_value = 0
        # for letter in s:
        #     value = roman_to_int[letter]
        #     result += value
        #     if value > prev_value:
        #         # preceding roman nummber is smaller
        #         # we need to undo the previous addition
        #         # and substract the preceding roman char
        #         # from the current one, i.e. we need to
        #         # substract twice the previous roman char
        #         result -= 2 * prev_value
        #     prev_value = value
        # return result


        # 다시 풀기 오늘 배운점 비교 대상을 변수로 나두고 변경하면 좋을듯


if __name__ == "__main__":
    test = Solution()
    print(test.romanToInt('LVIII'))
