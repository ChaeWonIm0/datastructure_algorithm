# 정답
def solution(nums, target):
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return True
    return False

print(solution(nums=[1,7,3,4], target=9))