def mySqrt(self, x: int) -> int:

    start, end = 0, x

    while start <= end:
        mid = (start + end) // 2

        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif x < mid * mid:
            end = mid - 1
        else:
            start = mid + 1

        return mid


if __name__ == "__main__":
    print(mySqrt(16))