#importing modules
import maze_enviroment
import threading
import time

#change the value to determin how fast/slow you want the agent to move
set_speed=0.06

#setting up discounting factor
discount = 0.7
#calling actions from module maze enviroment
actions = maze_enviroment.actions
#initializing states parameter or situtation
states = []
Q = {}
#updaating our Q-matix for every action taken
for i in range(maze_enviroment.x):
    for j in range(maze_enviroment.y):
        states.append((i, j))

for state in states:
    temp = {}
    for action in actions:
        temp[action] = 0.1
       
    Q[state] = temp

for (x, y,  reward) in maze_enviroment.winning:
    for action in actions:
        Q[(i, j)][action] = reward
         
 
#trigers the agent to move on any possible way
#eg:if an action up is activated from a state, provoks the funtion to a move of 0 x-axis and -1 y-axis 
def do_action(action):
    state = maze_enviroment.player
    r = -maze_enviroment.score
    if action == actions[0]:
        maze_enviroment.try_move(0, -1)
    elif action == actions[1]:
        maze_enviroment.try_move(0, 1)
    elif action == actions[2]:
        maze_enviroment.try_move(-1, 0)
    elif action == actions[3]:
        maze_enviroment.try_move(1, 0)
    else:
        return
    next_state = maze_enviroment.player
    r += maze_enviroment.score
    return state, action, r, next_state



#search across all possible actions, calculating the Q-value for each to find the highest
def max_Q(s):
    val = None
    act = None
    for a, q in Q[s].items():
        if val is None or (q > val):
            val = q
            act = a
    return act, val
def inc_Q(s, a, alpha, inc):
    Q[s][a] *= 1 - alpha
    Q[s][a] += alpha * inc
    
#pathway
def run():
    global discount
    time.sleep(1)
    alpha = 1
    t = 1
    while True:
        # Pick the right action
        s = maze_enviroment.player
        max_act, max_val = max_Q(s)
        (s, a, r, s2) = do_action(max_act)

        # Update Q
        max_act, max_val = max_Q(s2)
        inc_Q(s, a, alpha, r + discount * max_val)

        # Check if the game has restarted
        t += 1.0
        if maze_enviroment.has_restarted():
            maze_enviroment.restart_game()
            time.sleep(0.01)
            t = 1.0

        # Update the learning rate
        alpha = pow(t, -0.1)

         
        time.sleep(set_speed)


t = threading.Thread(target=run)
t.daemon = True
t.start()
maze_enviroment.start_game()
