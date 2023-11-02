from my_src.maze import Maze
from my_src.maze_viz import Visualizer
from my_uniform_cost_search import MyUniformCostSearch
from my_a_star_search import MYAStarSearch
import copy

class MazeManager(object):

    def __init__(self):                                                 #initialize variable
        self.mazes = []
        self.media_name = ""
        self.quiet_mode = False

    def add_maze(self, row, col, id=0):                                 #Add new maze inside manager object
        if id is not 0:
            self.mazes.append(Maze(row, col, id))
        else:
            if len(self.mazes) < 1:
                self.mazes.append(Maze(row, col, 0))
            else:
                self.mazes.append(Maze(row, col, len(self.mazes) + 1))

        return self.mazes[-1]

    def add_existing_maze(self, maze, override=True):                   #Add an already existing maze to the manager.
                                                                        # Check if there is a maze with the same id. If there is a conflict, return False
        # if self.check_matching_id(maze.id) is None:
        #     if override:
        #         if len(self.mazes) < 1:
        #             maze.id = 0
        #         else:
        #             maze.id = self.mazes.__len__()+1
        # else:
        #     return False
        
        ''' change code form here in order to deepcopy maze object'''
        copiedMaze = copy.deepcopy(maze)                                      #deep copying a maze in order to save diffent cost and path
        self.mazes.append(copiedMaze)                 
        return copiedMaze

    def get_maze(self, id):                                             #getting a maze variable inside manager object
        for maze in self.mazes:
            if maze.id == id:
                return maze
        print("Unable to locate maze")
        return None


    def solve_maze(self, maze_id, method, neighbor_method="brute-force"):   #solve the maze by using two algorithm
        maze = self.get_maze(maze_id)                                       #1. uniform cost search
                                                                            #2. a* search
        if method == "perfrom_uniform_cost_search":                        
            myUniformCostSearch = MyUniformCostSearch(maze)                              #solve the maze by uniform cost search
            maze.cost, maze.time, maze.path = myUniformCostSearch.uniform_cost_search()             #saving the cost and path by solving the maze
        elif method == "perfrom_a_star_search":
            myAStarSearch = MYAStarSearch(maze)                                    #solve the maze by a* search
            maze.cost, maze.time, maze.path = myAStarSearch.a_star_search()                   #saving the cost and path by solving the maze

    def show_maze(self, id, cell_size=1):                                   #show the maze created
        """Just show the generation animation and maze"""
        vis = Visualizer(self.get_maze(id), cell_size, self.media_name)
        vis.show_maze()

    # def show_generation_animation(self, id, cell_size=1):
    #     vis = Visualizer(self.get_maze(id), cell_size, self.media_name)
    #     vis.show_generation_animation()

    def show_solution(self, id, cell_size=1):                               #visualize the solution path
        vis = Visualizer(self.get_maze(id), cell_size, self.media_name)
        vis.show_maze_solution()

    def show_solution_animation(self, id, cell_size =1):                    #visualize the animation of searching process
        vis = Visualizer(self.get_maze(id), cell_size, self.media_name)
        vis.animate_maze_solution()
