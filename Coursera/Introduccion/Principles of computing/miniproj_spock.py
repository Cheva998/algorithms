# Rock-paper-scissors-lizard-Spock program


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
   # Function to convert name to number using if/elif/else
    if name == 'rock':
        num=0
    elif name == 'Spock':
        num=1
    elif name == 'paper':
        num=2
    elif name == 'lizard':
        num=3
    elif name == 'scissors':
        num=4
    return num


def number_to_name(number):
    # Function to convert number to a name using
    if number == 0:
        name= 'rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    return name


def rpsls(player_choice): 
    
    # print a blank line to separate consecutive games
    print ('')

    # print out the message for the player's choice
    print ('Player chooses: ', player_choice)
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    import random
    comp_number=random.randrange(0,4)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_name=number_to_name(comp_number)
    
    # print out the message for computer's choice
    print ('Computer chooses: ', comp_name)

    # compute difference of comp_number and player_number modulo five
    diff=(comp_number-player_number)
    if diff <0:
        diff=diff % 5
    
    # use if/elif/else to determine winner, print winner message
    if diff == 0:
        print ("Player and computer tie!")
    elif diff <= 2:
        print ('Computer wins!')
    else:
        print('Player wins!')
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


