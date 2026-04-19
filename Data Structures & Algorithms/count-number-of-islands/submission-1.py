class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        input: grid

        output: number of islands in the grid 
        variables: 
        island int 
        set to keepof visited islands



        Loop over the the grid 

         check if the current number is 1:
          If it a 1:
         if it one we ahve to check if we have already been to that island before
         if we havent been to that island: 
            add it to our visited islands
            increse the island by 1 
        
        
        Check its neighbors to see if it connected to ohter ones in the islad
        bfs serch to find its neighobor on each level
        set ot keep trac of cells visited
        queue to handle wchich node we can check next

        as long as the queue is not empty: 
            pop from the queue 
            check if we ahve seen that cell before:
                if we have seen that cell we skip
            else if we ahvent seen taht cell:
                we add it to the queue to process its neihbors 

            
            vertically and horizotally i amthing we can ehck level by level to see if there are other conected ones

        if it is not one, we check the remaning elements in the grid or continue

        return the number of islands




        """

        islands = 0 
        row, col = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
    
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))

            directions = [(1, 0), (-1,0), (0, 1), (0,-1)]
            while q:
                curr_r, curr_c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + curr_r, dc + curr_c
                    if (0 <= nr < row and 
                    0 <= nc < col and 
                    grid[nr][nc] == "1" and 
                    (nr, nc) not in visited):
                        q.append((nr,nc))
                        visited.add((nr,nc))

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1
                    bfs(r, c)

        return islands

    

        