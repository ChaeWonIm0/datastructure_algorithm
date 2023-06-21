# O(n^2)도 가능
# 문제에서 기본 제공
from collections import deque
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        length = len(cost)
        current_visited = 0
        q = deque()
        len_list = []
        len_list2 = []
        for v in range(length):
            if v % 2 ==1:
                len_list.append(v) # 짝수 리스트(0포함)
        for v in range(length):
            if v % 2 ==0:
                len_list2.append(v) # 홀수 리스트
        for i in cost:
            q.append(i)
        while q:
            current_visited = q.popleft()
            sumlist = []
            for i in len_list:
                for j in len_list2:
                    if cost[j] < cost[i]:
                        pass
                    if cost[i] < cost[j]:
                        current_visited = q.popleft()
                    sumlist.append(current_visited)
            return sum(sumlist)
S = Solution
cost = [10, 15, 20]
S.minCostClimbingStairs(S, cost)