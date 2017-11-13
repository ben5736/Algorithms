class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        h = len(grid)
        w = len(grid[0])
        
        ret = 0
        
        for i in range(h):
            for j in range(w):
                if grid[i][j]:
                    edges = 0
                    if i == 0 or grid[i - 1][j]:
                        edges += 1
                    if j == 0 or grid[i][j - 1]:
                        edges += 1
                    if i + 1 == h or grid[i + 1][j]:
                        edges += 1
                    if j + 1 == w or grid[i][j + 1]:
                        edges += 1
                    print i, j, edges
                    ret += edges

        return ret