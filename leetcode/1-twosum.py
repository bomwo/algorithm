from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 내 생각 풀이 target - nums == nums List에 있는값과 같을 시 index return 한다.
        # for index in range(len(nums)):
        #     for target_index, value in enumerate(nums):
        #         if abs(nums[index] - target) == value:
        #             return [index, target_index]
        # 이렇게 풀면 자기 자신도 포함되서 에러가 발생함

        #아래 풀이로 변경했는데 이러면 음수 케이스에서 에러가 발생하넹
        # for target_index, value in enumerate(nums):
        #     for index in range(target_index + 1, len(nums)):
        #         if abs(value - target) == nums[index]:
        #             return target_index, index
        # 절대값 제거 성공! 근데 이 해답은 리스트를 모두 순회하기떄문에 속도가 매우 느릴것이다. O(n^2) 일듯?
        # 어떻게바꾸는게 좋을까?
        for target_index, value in enumerate(nums):
            for index in range(target_index+1,len(nums)):
                if target - value == nums[index]:
                    return target_index, index

        # dict 형을 사용하면 엄청 간편해진다. 아래 방법은 근데 중복이 있으면 문제가 있겠다
        # 왜냐하면 dict 형의 key는 고유하니까 중복값이 오면 else 부분에 에러가 날듯
        d = dict()
        for index, value in enumerate(nums):
            m = target - value
            if m in d:
                return [d[m],index]
            else:
                d[value] = index


if __name__ == "__main__":
   a = Solution()
   print(a.twoSum(nums=[2,7,11,15],target=9))
   print(a.twoSum(nums=[3,2,4], target=6))
   print(a.twoSum(nums=[3,3], target=6))
   print(a.twoSum(nums=[-1,-2,-3,-4,-5], target=-8))