import time
from queue import PriorityQueue

''' this class contains uniform cost function
as making a MyUniformCostSearch object Maze variable is initialized '''
class MyUniformCostSearch():

    '''intialize maze to search solution'''
    def __init__(self, maze):                                              
        self.maze = maze                                                # maze to solve
        self.path = list()                                              # current path as algorithm is searching 
        self.total_spead = 0                                            # total searching time
        self.total_cost = 0                                             # total searching cost

    def uniform_cost_search(self):
        '''use priority queue to sort path by cost
        as we use only cost for sorting the structure inside a qeueu is a form of(cost, path)'''
        queue = PriorityQueue()                                             #using priority queue                                                  
        queue.put((0, self.maze.entry_coor))                            #initial queue must be (cost = 0, path=entry)


        start= time.perf_counter()                           #starting time of searching
        print("\nSolving the maze with uniform_cost_search...")
        
        '''algorithm starts with a two infinity loop until solution is found or search failier  loop cotinues'''
        while True:                                                         # infinity loop until solution is found and break
            while queue:                                                       # infinity loop until no possible way of expansion

                '''when expandsion cost and postion must be saved in a queue'''
                cost, (x, y) = queue.get()                        # Search one cell on the current level
                self.maze.grid[x][y].visited = True                    # check that the position is visited
                self.path.append(((x, y), False))                      # add current position to total search path

                '''when current position is exit return solution'''
                if (x, y) == self.maze.exit_coor:                     
                    end = time.perf_counter()
                    self.total_spead = end - start                     # save the total cost
                    self.total_cost = len(self.path)                   # save the total time
                    print("Number of moves performed: {}".format(self.total_cost))
                    print("Execution time for algorithm: {:.4f}".format(self.total_spead))
                    return self.total_cost, self.total_spead, self.path                                  #return length of the path found and cost

                '''from current position search neighbour position and find if there is a new position to expand'''
                exapand_xy = self.maze.find_neighbours(x, y)  
                exapand_xy = self.maze.validate_neighbours_solve(exapand_xy, x, y, self.maze.exit_coor[0],
                                                                  self.maze.exit_coor[1], "brute-force")
                
                '''where there is a room to exapansion expand and add it to the queue with cost+1'''
                if exapand_xy is not None:
                    for xy in exapand_xy:
                        queue.put((cost+1,xy))
