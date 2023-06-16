# 해결안 (Dictionary와 in 연산자 사용필요)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict = {}
        for i in nums:
            dict[i] = True
        for v in nums:
            n = target - v
            if n in dict:
                return True
        return False

nums = [4,1,9,7,5,3,16]
target = 4
i = Solution
i.twoSum(i,nums,target)