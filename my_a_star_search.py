import time
from queue import PriorityQueue
import numpy

'''this class contains a* search
as making a MYAStarSearch object Maze variable is initialized'''
class MYAStarSearch():

    '''intialize maze to search solution'''
    def __init__(self, maze):
        self.maze = maze                                                #maze to solve
        self.path = list()                                              #current path as algorithm is searching 
        self.total_spead = 0                                                  #total searching time
        self.total_cost = 0                                             # total searching cost


    def a_star_search(self):
        '''use priority queue to sort path by cost
    as we use only cost for sorting the structure inside a qeueu is a form of(distance, cost, path)'''
        queue = PriorityQueue()                             #using priority queue

        alpha = 0.2                                                     # value for optimizing f(x)
  

        '''in a star search g(x) and h(x) is define as cost of the path and distance between current position to goal position'''
        cost = 0
        distance2goal = numpy.linalg.norm(numpy.array(self.maze.entry_coor) 
                              - numpy.array(self.maze.exit_coor))            #use distance between goal and current position as huristic
        queue.put((cost*alpha + distance2goal*(1-alpha), cost, self.maze.entry_coor))                    #initial queue must be set (distance from here to goal, cost, path=entry)


        start= time.perf_counter()                           #starting time of searching
        print("\nSolving the maze with A_star_search...")

        '''algorithm starts with a two infinity loop until solution is found or search failier  loop cotinues'''
        while True:                                                         # infinity loop until solution is found and break
            while queue:                                           # infinity loop until no possible way of expansion
                
                '''when expandsion cost and postion must be saved in a queue'''
                cost , (x, y) = queue.get()[1:]                     # Search one cell on the current level
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
                exapand_xy = self.maze.validate_neighbours_solve(exapand_xy, x,
                                                                  y, self.maze.exit_coor[0],
                                                                  self.maze.exit_coor[1], "brute-force")

                '''where there is a room to exapansion expand then calculate the distance again and add it to the queue with cost+1'''
                if exapand_xy is not None:
                    for xy in exapand_xy:
                        distance2goal = numpy.linalg.norm(numpy.array(xy) - numpy.array(self.maze.exit_coor))      #recalculate distance
                        queue.put((cost*alpha + distance2goal*(1-alpha), cost+1, xy))                                              #add it to the queue
