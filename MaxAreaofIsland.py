#695. Max Area of Island
#Author: Ana Luisa Mata

#Given a non-empty 2D array grid of 0's and 1's, 
#an island is a group of 1's (representing land) 
#connected 4-directionally (horizontal or vertical.) 
#You may assume all four edges of the grid are surrounded by water.
#Find the maximum area of an island in the given 2D array. 
#(If there is no island, the maximum area is 0.)

#Runtime: Runtime: 132 ms, faster than 92.11% of Python3 online submissions for Max Area of Island.
#Memory Usage: Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Max Area of Island.
#Time complexity: O(nm)
#Space complexity: O(1)

class Solution:
    def islandTraveler(self,node, grid):
        stacky = [node]
        count = 0
        grid[node[0]][node[1]]=0
        while len(stacky)>0:
            curr = stacky.pop()
            if curr[0]-1>=0 and curr[0]-1<len(grid) and grid[curr[0]-1][curr[1]]==1:
                stacky.append([curr[0]-1,curr[1]])
                grid[curr[0]-1][curr[1]]=0
            if curr[1]-1>=0 and curr[1]-1<len(grid[0]) and grid[curr[0]][curr[1]-1]==1:
                stacky.append([curr[0],curr[1]-1])
                grid[curr[0]][curr[1]-1]=0
            if curr[1]+1>=0 and curr[1]+1<len(grid[0]) and grid[curr[0]][curr[1]+1]==1:
                stacky.append([curr[0],curr[1]+1])
                grid[curr[0]][curr[1]+1]=0
            if curr[0]+1>=0 and curr[0]+1<len(grid) and grid[curr[0]+1][curr[1]]==1:
                stacky.append([curr[0]+1,curr[1]])
                grid[curr[0]+1][curr[1]]=0
            count+=1
        return count
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxIsland = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] is 1:
                    curr = self.islandTraveler([i,j], grid)
                    if curr>maxIsland:
                      maxIsland = curr
        return maxIsland
