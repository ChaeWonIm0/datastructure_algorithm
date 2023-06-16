# 해결책
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest = 0
        dict = {}
        for num in nums:
            dict[num] = True
        for num in dict:
            if num -1 not in dict:
                count = 1
                target = num +1
                while target in dict:
                    target += 1
                    count += 1
                longest = max(longest, count)
        return longest
nums2 = [0,3,7,2,5,8,4,6,0,1, 101, 102, 103,81,104, 105,19 ,106, 107, 108, 109, 110, 111]
output2 = 11
i = Solution
i.longestConsecutive(i, nums2)