# http://www.codeskulptor.org/#user39_O7MBeu718q_15.py

# template for "Stopwatch: The Game"

# define global variables

import simplegui
t = 0
score = 0
attempts = 0
punt = "0/0"

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format(t):
    th_seg = t % 10
    th_seg_str = str(th_seg)
    seg = t /10 % 60
    seg_str = str(seg)
    minut = t / 10 / 60
    minut_str = str(minut)
    if seg < 10:
        seg_str = "0" + seg_str
    tiempo = minut_str + ":" + seg_str + "." + th_seg_str
    return tiempo


# define event handlers for buttons; "Start", "Stop", "Reset"
def starti():
    global t
    tim.start()
    t += 1
    tiempo = format(t)
    
def stopti():
    global score, attempts, punt
    if tim.is_running():
        attempts += 1
        punt = events()
    tim.stop()
    
def reseti():
    global t, score, attempts, punt
    if tim.is_running():
        tim.stop()
    t = 0
    score = 0
    attempts = 0
    punt = events()


# define event handler for timer with 0.1 sec interval
def events():
    global score, punt
    tiempo = t % 10
    if tiempo == 0 and t>0:
        score += 1
    punt = str(score) + "/" + str(attempts)
    return punt

# define draw handler
def draw_hndl(canvas):
    frame.set_canvas_background("Black")
    tiempo = format(t)
    canvas.draw_text(tiempo, (80, 120), 40, 'White')
    canvas.draw_text(punt, (230, 30), 24, 'Green')

    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)
frame.set_draw_handler(draw_hndl)


star_bu = frame.add_button("Start", starti, 100)
stop_bu = frame.add_button("Stop", stopti, 100)
reset_bu = frame.add_button("Reset", reseti, 100)
tim = simplegui.create_timer(100, starti)


# register event handlers


# start frame
frame.start()

# Please remember to review the grading rubric
