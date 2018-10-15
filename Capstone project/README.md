### description
This is a driven from robotics competition where small, self-contained robots, attempt to map, then solve and navigate a previously unseen maze.
The agent is completely an autonomous robots that must find its way from a predetermined starting position to the central area of the maze unaided.
Having reached the goal (first trial), the agent will typically perform additional searches of the maze until it has found an optimal route from the start to the center
 
● Rules: The agent (beginning state) has to reach the goals to end the game (center)
● Rewards: The center gives a positive reward. Each step gives a negative reward 
● States: Each cell is a state in which the agent can be.
● Actions: There will be only 4 actions. Up, Down, Right, Left.


### Install
This project requires
-Python 2.7
-tkinter


### usage

Run `python tester.py` in terminal to see the the bot in action. It'll find the optimal strategy depending on the time regulation (constant)you can set on the variable `set_speed` in **robot.py** file


