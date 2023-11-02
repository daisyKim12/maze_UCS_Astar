# maze_UCS_Astar
Implementing python based uniform cost search and A * search, using maze codebase provide by github.com/jostbr/pymaze.

## Task
1. Implement the Uniform Cost Search algorithm by adding a new function to the existing codebase. The function should be named uniform_cost_search and should take as input a maze object and return the optimal path from the starting position to the goal position, along with its cost.
2. Implement the A* Search algorithm by adding another new function to the existing codebase. The function should be named a_star_search and should take as input a maze object and a heuristic function, and return the optimal path from the starting position to the goal position, along with its cost. Please use a Euclidian distance for its heuristic function.
3. Visualize the solutions obtained by both algorithms on 10 randomly generated 20x20 mazes. You should use the visualization functions already provided in the codebase to create a visual representation of each maze and the found paths.
4. Write a detailed report that explains your implementation of the two algorithms, including any modifications or enhancements you made to the existing codebase. Your report should also include a discussion of the strengths and weaknesses of each algorithm and their performance (e.g., the number of steps) on the mazes you used for testing.

## file discription
- maze_search_report.pdf: More sepecific description of the code and the result analysis
- main.py: main python file so in this file the algorithm is tested. In order to check the result just enter the following code in the terminal 
```python .\main.py```
- my_uniform_cost_search: this file contains a class having the variable and method to perform uniform cost search
- my_a_star_search: this file contains a class having the variable and method to perform a* search                
- maze_manager: this file contains a class that saves and manages the maze state and data

## Result

**Visulization of cost and time**   
![](x/Screenshot%202023-11-02%20at%208.50.23%20PM.png)   

**Visualication of Solution Path**  
![](x/Screenshot%202023-11-02%20at%208.51.32%20PM.png)   

**Perforamance evaluation**
1. Path length   
![](x/Screenshot%202023-11-02%20at%208.52.40%20PM.png)   

2. Total time   
![](x/Screenshot%202023-11-02%20at%208.54.36%20PM.png)