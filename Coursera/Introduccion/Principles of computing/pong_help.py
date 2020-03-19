#http://www.codeskulptor.org/#user39_BDasGPXfl5_3.py

# Ball motion with an implicit timer

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [0, 1] # pixels per update (1/60 seconds)

# define event handlers
def draw(canvas):
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]

    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

# create frame
frame = simplegui.create_frame("Motion", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()




####################################################################################################
############ Control de velocidad con aceleración ###################
####################################################################################################


import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [1, 2]  # pixels per tick
vel_max = [3, 3]
accel = .5
time = 0

# define event handlers
def tick():
    global time
    time = time + 1

def draw(canvas):
    # create a list to hold ball position
    global ball_pos

    # calculate ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    if ball_pos[0] < 0:
        ball_pos[0] = (ball_pos[0] - WIDTH) % WIDTH
    elif ball_pos[0] > WIDTH:
        ball_pos[0] = ball_pos[0] % WIDTH
    if ball_pos[1] < 0:
        ball_pos[1] = (ball_pos[1] - HEIGHT) % HEIGHT
    elif ball_pos[1] > HEIGHT:
         ball_pos[1] = ball_pos[1] % HEIGHT
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
#    velo_str = str(vel)
    canvas.draw_text("vel"+str(vel), (20, 20), 12, 'Yellow')
    canvas.draw_text("pos"+str(ball_pos), (20, 40), 12, 'Yellow')
    
def keydown(key):
    global vel
    if key == simplegui.KEY_MAP["left"]:
        vel[0] -= accel 
        if vel[0] < -vel_max[0]:
            vel[0] = -vel_max[0]
    elif key == simplegui.KEY_MAP["right"]:
        vel[0] += accel
        if vel[0] > vel_max[0]:
            vel[0] = vel_max[0]
    elif key == simplegui.KEY_MAP["down"]:
        vel[1] += accel 
        if vel[1] > vel_max[1]:
            vel[1] = vel_max[1]
    elif key == simplegui.KEY_MAP["up"]:
        vel[1] -= accel 
        if vel[1] < -vel_max[1]:
            vel[1] = -vel_max[1]
    
        
# create frame
frame = simplegui.create_frame("Motion", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

timer = simplegui.create_timer(100, tick)
frame.set_keydown_handler(keydown)

# start frame
frame.start()
timer.start()
