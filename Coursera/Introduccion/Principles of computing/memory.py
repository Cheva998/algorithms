##memory
#http://www.codeskulptor.org/#user39_sq2wPiMpWcoSAIJ.py

# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global state, cartas, n, turn
    turn = 0
    n = 16
    state = 0
    cartas = dict()
    pares = range(n / 2) * 2
    for ind in range(n):
        escog = random.choice(pares)
        cartas["carta"+str(ind)] = [pares.pop(pares.index(escog)), "Cerrado"]


### define event handlers
def mouseclick(pos):
    global state, turn, num1, num2, num3
    ejx = pos[0] / 50
    if state == 0:
        if cartas["carta"+str(ejx)][1] == "Cerrado":
            state = 1
            cartas["carta"+str(ejx)][1] = "Abierto"
            num1 = ("carta"+str(ejx), cartas["carta"+str(ejx)][0])
            num2 = num1
            num3 = num1
            
    elif state == 1:
        if cartas["carta"+str(ejx)][1] == "Cerrado":
            state = 2
            cartas["carta"+str(ejx)][1] = "Abierto"
            
            if num1[1] != num2[1]:
                cartas[num1[0]][1] = "Cerrado"
                cartas[num2[0]][1] = "Cerrado"
            num1 = num3
            num2 = ("carta"+str(ejx), cartas["carta"+str(ejx)][0])
            turn += 1
            if num1[1] == num2[1]:
                cartas[num1[0]][1] = "Pareja"
                cartas[num2[0]][1] = "Pareja"
    else:
        if cartas["carta"+str(ejx)][1] == "Cerrado":
            state = 1
            cartas["carta"+str(ejx)][1] = "Abierto"
            if num1[1] != num2[1]:
                cartas[num1[0]][1] = "Cerrado"
                cartas[num2[0]][1] = "Cerrado"
            num3 = ("carta"+str(ejx), cartas["carta"+str(ejx)][0])
    

    

# cards are logically 50x100 pixels in size    
def draw(canvas):
    for ind in range(n):
        canvas.draw_line((50 * (1+ind), 0), (50 * (1+ind), 100), 1, 'White')
        dispt = str(cartas["carta"+str(ind)][0])
        canvas.draw_text(dispt, (50 * ind + 20, 60), 34, 'Red')
        label.set_text("Turns = "+str(turn))
        if cartas["carta"+str(ind)][1] == "Cerrado":
            canvas.draw_image(image, (200/2,277/2), (200,277), (50 * ind + 25, 50), (50, 100))



# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
image = simplegui.load_image('https://dl.dropboxusercontent.com/u/64561039/Imagenes/Memory/magic_back.jpg')
new_game()
label = frame.add_label("Turns = "+str(turn))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric