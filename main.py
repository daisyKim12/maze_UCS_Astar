from maze_manager import MazeManager
import copy


if __name__ == "__main__":

    # two manager for two algorithm
    uniform_cost_manager= MazeManager()
    a_start__manager = MazeManager()

    performance = []


    for i in range(10):

        # for copying the maze I used copy.deepcopy() method in .add_existing_maze method
        maze = uniform_cost_manager.add_maze(20, 20)            # add new maze in manager
        copy_maze = a_start__manager.add_existing_maze(maze)    # copy the same maze to next manager

        # solve the maze in uniform cost search
        uniform_cost_manager.solve_maze(maze.id, "perfrom_uniform_cost_search")
        uniform_cost_manager.show_solution(maze.id)
        performance.append((i+1, "uniform_cost",maze.cost, maze.time))

        # solve the maze in a star search
        a_start__manager.solve_maze(copy_maze.id, "perfrom_a_star_search")  
        a_start__manager.show_solution(copy_maze.id)
        performance.append((" ", "a_star     ", copy_maze.cost, copy_maze.time))
    
    print("\n")
    print("Maze\tAlgorithm\tCost\tTime")
    for item in performance:
        print("{}\t{}\t{}\t{}".format(item[0], item[1], item[2], item[3]))
    print("\n")

    
    
