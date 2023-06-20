# DFS

# 문제에서 제공
class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = []

        def dfs(current_visited):
            visited.append(current_visited)
            for next_visited in rooms[current_visited]:
                if next_visited not in visited:
                    dfs(next_visited)
        
        dfs(0)

        if len(visited) == len(rooms):
            return True
        else:
            return False
s = Solution
rooms = [[1,3], [2,4], [0], [4], [3,4]]
s.canVisitAllRooms(s, rooms)