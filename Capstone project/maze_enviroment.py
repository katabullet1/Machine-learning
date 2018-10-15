#importing modules
from Tkinter import *
import turtle

#setting up the platform 
launch = Tk()
launch.title("THE MYSTERIOUS ISLAND") 
launch.iconbitmap(default='img/Robotic_pet.ico')

#defining variables

actions = ["up", "down", "left", "right"]
Width = 40
b_border=40
a=15
b=15
(x, y) = (a, b)
board = Canvas(launch, width=x*b_border, height=y*b_border,   bg=None)
player = (0, y-1)
score = 1
restart = False
walk_reward = -0.02

winning = [(7, 7, 2)]
#setting up walls
walls = [(1, 1), (1, 2),(1,5), (1,12),(1,13), (4,13), (4,12), (7,13), (1,1), (1,2), (9,0), (8,2), (7,2),(9,1),(9,2),(9,12), ( 9,11), (11,11), (13,12), (13,11),(13,10), (13,9),  (12,9),(11,9),(10,9),(9,9), (9,10),(6, 8),(7, 8), (8,8), (9,8), (6,6),(6,7),(7,4) ,(8,4),(9,7),(4,4),(3,4),(3,5),(3,6),(3,7),(3,8), (1,7),(2,7), (2,10),(3,10),(4,10),(4,11), (5,11),(6,11),(11,5),(11,6), (7,14),(11,3),(12,3),(13,3),(14,3), (5,1),(5,2),(5,3),(5,4),(5,5),(12,8),(14,7), (14,6,), (12,0), (12,1),(11,1),(11,12),(9,6)]


cell_scores = {}
 
board.pack() 

#defines randm moves
agent = board.create_oval(player[0]*Width+Width*2/10, player[1]*Width+Width*2/10,
                            player[0]*Width+Width*8/10, player[1]*Width+Width*8/10, fill="blue", width=1, tag="nini")    
    
#design goal box
board.pack(expand=YES, fill=BOTH)
win_box = PhotoImage(file='img/trophy.gif')
show=board.create_image(290,285, image=win_box, anchor=NW)





#setting up the visual display of polygons on the maze board
#as define above 15 by 15
    
def render_grid():
    global winning, walls, Width, x, y, player
    for i in range(x):
        for j in range(y):
            board.create_rectangle(i*Width, j*Width, (i+1)*Width, (j+1)*Width, width=1)
            temp = {}
            
            cell_scores[(i,j)] = temp
    for (x_axis, y_axis,   reward) in winning:
        board.create_rectangle(x_axis*Width, y_axis*Width, (x_axis+1)*Width, (y_axis+1)*Width,  width=1)
    for (i, j) in walls:
        board.create_rectangle(i*Width, j*Width, (i+1)*Width, (j+1)*Width, fill="black", width=1)

render_grid()

 

# accumulating the moves from agent initial position to the goal
def try_move(dx, dy):
    global player, x, y, score, walk_reward, me, restart
    if restart == True:
        restart_game()
    new_x = player[0] + dx
    new_y = player[1] + dy
    score += walk_reward
    if (new_x >= 0) and (new_x < x) and (new_y >= 0) and (new_y < y) and not ((new_x, new_y) in walls):
        board.coords(agent, new_x*Width+Width*2/10, new_y*Width+Width*2/10, new_x*Width+Width*8/10, new_y*Width+Width*8/10)
        player = (new_x, new_y)
        
    for (x_axis_goal, y_axis_goal,   reward) in winning:
        if new_x == x_axis_goal and new_y == y_axis_goal:
            score -= walk_reward
            score += reward
            if score > 0 and score <2.45:
                print "Success! score: ", score
            
            elif score>=2.44:
                print "bingo!" , score
                
            else:
                print "Fail! score: ", score
            restart = True
            return
    #print "score: ", score


    
#functions that defines the actions taking from each states ( up, down, left, right)    
def call_up(event):
    try_move(0, -1)

def call_down(event):
    try_move(0, 1)

def call_left(event):
    try_move(-1, 0)

def call_right(event):
    try_move(1, 0)

#after reaching the goal, go for next episode    
def restart_game():
    global player, score, me, restart
    player = (0, y-1)
    score = 1
    restart = False
    board.coords(agent, player[0]*Width+Width*2/10, player[1]*Width+Width*2/10, player[0]*Width+Width*8/10, player[1]*Width+Width*8/10)
     
       
        
def has_restarted():
    return restart
 


board.grid(row=0, column=0)


def start_game():
    launch.mainloop()
 