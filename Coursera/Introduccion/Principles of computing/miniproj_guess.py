#http://www.codeskulptor.org/#user39_vd5xbT0wApXq4HA.py

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import math
import simplegui

rango = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global rango, guesses, secret_number
    guesses = int(math.log(rango, 2) + 1)
    secret_number = random.randrange(0, rango)
    print 'New game. The range is', rango
    print 'Number of remaining guesses is', guesses, '\n'
    return


# define event handlers for control panel

def range100():
    # button that changes the rango to [0,100) and starts a new game 
    global secret_number, guesses, rango
    rango = 100
    new_game()
    return

def range1000():
    # button that changes the rango to [0,1000) and starts a new game     
    global secret_number, guesses, rango
    rango = 1000
    new_game()
    return
    
def input_guess(guess):
    # main game logic goes here
    global guesses
    guess = int(guess)
    guesses = guesses - 1
    print 'The guess was', guess
    print 'Number of remaining guesses is', guesses
    if guess > secret_number:
        print 'Lower!'
    elif guess < secret_number:
        print 'Higher!'
    else:
        print 'Correct! YEAH!', '\n'
        new_game()
    print ''
    if guesses == 0:
        print 'Game over :(', '\n'
        new_game()
    return

# create frame
f = simplegui.create_frame('Guess the number', 100, 180)

# register event handlers for control elements and start frame
ran100 = f.add_button('Range is [0 100)', range100, 150)
ran1000 = f.add_button('Range is [0 1000)', range1000, 150)
gu = f.add_input('Enter a guess', input_guess, 150)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
