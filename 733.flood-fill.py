# @before-stub-for-debug-begin
# @lc code=start
from collections import deque

# @before-stub-for-debug-end

#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        # q = deque()
        # visited = [[False for j in range(len(image[0]))] for i in range(len(image))]
        # startColor = image[sr][sc]
        # q.append([sr, sc])
        # while len(q) > 0:
        #     currItem = q.popleft()
        #     x = currItem[0]
        #     y = currItem[1]
        #     image[x][y] = color
        #     visited[x][y] = True
        #     neighbours = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        #     for n in neighbours:
        #         nx, ny = n[0], n[1]
        #         if nx < len(image) and nx >= 0:
        #             if ny < len(image[0]) and ny >= 0:
        #                 if image[nx][ny] == startColor and not visited[nx][ny]:
        #                     q.append([nx, ny])
        # return image

        q = deque()
        seen = set()
        startColor = image[sr][sc]
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q.append((sr, sc))
        while q:
            x, y = q.popleft()
            seen.add((x, y))
            image[x][y] = color
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < len(image)
                    and 0 <= ny < len(image[0])
                    and image[nx][ny] == startColor
                    and (nx, ny) not in seen
                ):
                    q.append((nx, ny))
        return image


# @lc code=end
