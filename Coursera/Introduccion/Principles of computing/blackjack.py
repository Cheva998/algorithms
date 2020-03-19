#http://www.codeskulptor.org/#user39_GwriAQelevjC5OY_10.py

# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('T', 'P', 'C', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

HARD_TOT = {"21-17":["A-2", "S"], "16-13":["AKQJT987", "H", "65432", "S"],
            "12-12":["AKQJT987", "H", "654", "S", "32", "H"], "11-5":["A2", "H"]}

SOFT_TOT = {"10-8":["A-2", "S"], "7-7":["AKQJT9", "H", "8765432", "S"], "6-2":["A-2","H"]}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.cards = list()
        

    def __str__(self):
        # return a string representation of a hand
        ha = ""
        for card in self.cards:
            ha += card.get_suit() + card.get_rank() + " "
        return ha

    def add_card(self, card):
        # add a card object to a hand
        self.cards.append(card)
        
    def choose_card(self, pos_card):
        #Pick one card from the hand
        return self.cards[pos_card]
    
    def whos_there(self):
        # Who's there??!!
        values = []
        pintas = []
        for card in self.cards:
            values.append(card.get_rank())
            pintas.append(card.get_suit())
        return values, pintas

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0
        flag = False
        if len(self.cards) > 0:
            for card in self.cards:
                rank = card.get_rank()
                value += VALUES[rank]
                if rank == "A":
                    flag = True
            if flag and value <= 11:
                value += 10
        return value
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        if len(self.cards) > 0:
            for card in self.cards:
                card.draw(canvas, [pos[0], pos[1]])
                pos[0] += CARD_SIZE[0] + 5
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for su in SUITS:
            for ra in RANKS:
                self.cards.append(Card(su,ra))

    def __str__(self):
        # return a string representing the deck
        de = ""
        count = 0
        n = 1
        for card in self.cards:
            if count == 13 * n :
                de += "\n"
                n += 1
            de += card.get_suit() + card.get_rank() + " "
            count += 1
        return de
    
    def shuffle(self):
        # shuffle the deck 
        rev = random.shuffle(self.cards)  # use random.shuffle()
        return rev   

    def deal_card(self):
        # deal a card object from the deck
        dealt = self.cards.pop(0)
        return dealt
    
#Function for giving hints to the player
def hint():
    global hint_message, mes
    car_casa = casa.choose_card(1)
    rank = car_casa.get_rank()
    values, pintas = mano.whos_there()
    hard = mano.get_value()
#    hard = 0
#    for v in values:
#        hard += VALUES[v]
    soft = 0
    flag = False
    for v in values:
        if v != "A" or flag:
            soft += VALUES[v]
        else:
            flag = True
#    mes = " soft"+str(soft)+str(values)+" Hard" + str(hard)#+str(ind)+str(an)
    mes = "You got: " + str(hard)
    if "A" in values and soft < 11:
#        print "nie"
        if soft <= 10 and soft >= 8:
            hint = "S"
        elif soft == 7:
            if rank in SOFT_TOT["7-7"][0]:
                hint = "H"
            else:
                hint = "S"
        else:
            hint = "H"
        
    else:
#        print "hooooo"
        if hard <= 21 and hard >= 17:
            hint = "S"
        elif hard <= 16 and hard >= 13:
            if rank in HARD_TOT["16-13"][0]:
                hint = "H"
            else:
                hint = "S"
        elif hard == 12:
            if rank in HARD_TOT["12-12"][0]:
                hint = "H"
            elif rank in HARD_TOT["12-12"][2]:
                hint = "S"
            elif rank in HARD_TOT["12-12"][4]:
                hint = "H"
        else:
            hint = "H"
        
    if hint == "H":
        hint_message = "You should hit"
    elif hint == "S":
        hint_message = "You should stand"
        
#define event handlers for buttons
def deal():
    global outcome, in_play, dec, mano, casa, score
    outcome = ""
    dec = Deck()
    dec.shuffle()
    mano = Hand()
    casa = Hand()
    for i in range(2):
        mano.add_card(dec.deal_card())
        casa.add_card(dec.deal_card())
#    mano.add_card(dec.deal_card())
#    mano.add_card(Card("T","A"))
    in_play = True
    hint()

def hit():
    # if the hand is in play, hit the player
    global outcome, in_play, score
    if in_play:
        mano.add_card(dec.deal_card())
        hint()
   
    # if busted, assign a message to outcome, update in_play and score
    if mano.get_value() > 21 and in_play:
        outcome = "Busted! .... House wins"
        score -= 1
        in_play = False


def stand():
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    global outcome, in_play, score
    if in_play:
        while casa.get_value() < 17 :
            casa.add_card(dec.deal_card())
        if casa.get_value() <= 21:
            if casa.get_value() >= mano.get_value():
                outcome = "House wins"
                score -= 1
            else:
                outcome = "You win!!!"
                score += 1
        else:
            outcome = "You win!!! House is busted"
            score += 1
    # assign a message to outcome, update in_play and score
    in_play = False

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    pos_casa = [100, 250]
    pos_mano = [100, 400]
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [pos_casa[0] + CARD_CENTER[0], pos_casa[1] + CARD_CENTER[1]], CARD_BACK_SIZE)
        sec_card = casa.choose_card(1)
        sec_card.draw(canvas, [pos_casa[0]+CARD_SIZE[0]+5, pos_casa[1]])
        canvas.draw_text("Choose: Hit or Stand", (370, 200), 20, 'Black')
        canvas.draw_text(hint_message, (390, 520), 20, 'Black')
    else:
        casa.draw(canvas, pos_casa)
        canvas.draw_text("Deal again", (370, 200), 20, 'Black')
    mano.draw(canvas, pos_mano)
    canvas.draw_text(outcome, (80, 100), 26, 'Black')
    canvas.draw_text("Score: " + str(score), (370, 150), 50, 'Black')
    canvas.draw_text("House", (30, 280), 20, 'Black')
    canvas.draw_text("You", (30, 430), 20, 'Black')
    
    canvas.draw_text(mes, (100, 540), 20, 'Black')


##################PRUEBA#####################
#dec = Deck()
#dec.shuffle()
#print dec
#mano = Hand()
#for c in range(2):
#    mano.add_card(dec.deal_card())
#    print mano, "\n", mano.get_value()
#print dec
#for game in range(300):
#	 deal()
#    print "mano", mano,mano.get_value(), "\n","casa", casa, casa.get_value(), "\n"
#    while mano.get_value() < 17:
#        hit()
#
#    stand()
#    print "mano", mano,mano.get_value(), "\n","casa", casa, casa.get_value(), "\n", outcome, score, "\n\n"
############################################
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit", hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()

# remember to review the gradic rubric