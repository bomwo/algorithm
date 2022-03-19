class Solution:
    def climbStairs(self, n: int) -> int:
        start, end = 0, 1
        for value in range(n):
            start,end = end, end+start

        return end
    # 이거 DP 문제인데 그냥 피보나치로 풀면되는 문제

if __name__ == "__main__":
    test = Solution()
    print(test.climbStairs(10))
