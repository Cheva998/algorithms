# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_vel = 0
paddle2_vel = 0
pad1_x = HALF_PAD_WIDTH
pad2_x = WIDTH - HALF_PAD_WIDTH
paddle1_pos = HEIGHT / 2 - HALF_PAD_HEIGHT
paddle2_pos = HEIGHT / 2 - HALF_PAD_HEIGHT
pad_vel = 10
ball_pos = [WIDTH / 2, HEIGHT / 2]    



# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [0, 0]
    if direction == "left":
        ball_vel[0] = -3 + random.random() * 1.5
    elif direction == "right":
        ball_vel[0] = 3 + random.random() * 1.5
    ball_vel[1] = -(2 + random.random() * 1.5)


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2, direction, x  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = HEIGHT / 2 - HALF_PAD_HEIGHT
    paddle2_pos = HEIGHT / 2 - HALF_PAD_HEIGHT
    dire = random.randrange(0,2)
    if dire == 0:
        direction = "right" 
    else:
        direction = "left"
    x = 1
    spawn_ball(direction)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel, paddle2_vel, direction, pad_vel, x, y, b, m
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
                
            
    if ball_pos[1] < 0 + BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] > HEIGHT - BALL_RADIUS:
         ball_vel[1] = -ball_vel[1]        
 

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    # Computer player !!!!!
    if ball_vel[0] < 0:
        m = ball_vel[1]/ball_vel[0]
        x = ball_pos[0]
        y = ball_pos[1]
        b = y - m * x
#        if b < 0:
#            x = -b / m
#            m = -m
#            b = 0 - m / x
#        elif b > HEIGHT:
#            x = HEIGHT - b / m
#            m = -m
#            b = HEIGHT - m / x
            
        
            
        if b >= paddle1_pos - 10 and b <= paddle1_pos + PAD_HEIGHT - 10:
            paddle1_vel = 0
        elif b < paddle1_pos:
            paddle1_vel = -pad_vel
        elif b > paddle1_pos + PAD_HEIGHT:
            paddle1_vel = pad_vel
    else:
        if paddle1_pos + HALF_PAD_HEIGHT < HEIGHT / 2:
            paddle1_vel = pad_vel
        elif paddle1_pos + HALF_PAD_HEIGHT > HEIGHT / 2:
            paddle1_vel = -pad_vel
        else:
            paddle1_vel = 0
                
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    # Keep paddle 1 on screen
    if paddle1_pos <= 0:
        paddle1_pos = 0
    elif paddle1_pos >= HEIGHT - PAD_HEIGHT:
        paddle1_pos = HEIGHT - PAD_HEIGHT
    # Keep paddle 2 on screen    
    if paddle2_pos <= 0:
        paddle2_pos = 0
    elif paddle2_pos >= HEIGHT - PAD_HEIGHT:
        paddle2_pos = HEIGHT - PAD_HEIGHT

        # draw paddles
    canvas.draw_line([pad1_x, paddle1_pos],[pad1_x, paddle1_pos + PAD_HEIGHT], PAD_WIDTH, "White")
    canvas.draw_line([pad2_x, paddle2_pos],[pad2_x, paddle2_pos + PAD_HEIGHT], PAD_WIDTH, "White")
    
    # determine whether paddle and ball collide    
    if ball_pos[0] - BALL_RADIUS <= PAD_WIDTH:
        if ball_pos[1] >= paddle1_pos and ball_pos[1] <= paddle1_pos + PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0] * 1.1
            ball_vel[1] = ball_vel[1] * 1.1
        else:
            score2 += 1
            direction = "right"
            spawn_ball(direction)
    if ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH:
        if ball_pos[1] >= paddle2_pos and ball_pos[1] <= paddle2_pos + PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0] * 1.1
            ball_vel[1] = ball_vel[1] * 1.1
        else:
            score1 += 1
            direction = "left"
            spawn_ball(direction)

    # draw scores
    canvas.draw_text(str(score1), [WIDTH / 2 - PAD_HEIGHT, PAD_HEIGHT], 24, "White")
    canvas.draw_text(str(score2), [WIDTH / 2 + PAD_HEIGHT, PAD_HEIGHT], 24, "White")
    
def keydown(key):
    global paddle1_vel, paddle2_vel, pad_vel, direction
#    if key == simplegui.KEY_MAP["w"]:
#        paddle1_vel = -pad_vel
#    elif key == simplegui.KEY_MAP["s"]:
#        paddle1_vel = pad_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -pad_vel
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = pad_vel

    
def keyup(key):
    global paddle1_vel, paddle2_vel
#    if key == simplegui.KEY_MAP["w"]:
#        paddle1_vel = 0
#    elif key == simplegui.KEY_MAP["s"]:
#        paddle1_vel = 0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
boton = frame.add_button("Restart", new_game)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
