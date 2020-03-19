#http://www.codeskulptor.org/#user40_DrnSJND5AH_19.py

"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set

def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    scores = [0 for dummy in range(max(hand))]
    for indx in hand:
        scores[indx - 1] += indx
    max_score = max(scores)
    return max_score

def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    outcomes = range(1,num_die_sides+1)
    all_outcomes = gen_all_sequences(outcomes, num_free_dice) 
    num_outcomes = float(len(all_outcomes))
    value = 0
    hand = list(held_dice)
    lon = len(held_dice)
#    print num_free_dice + len(held_dice), "dices in play"
    for outcome in all_outcomes:
        hand[lon:] = list(outcome)
        roll_value = score(tuple(hand))
        value += float(roll_value) / num_outcomes
    return value

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    held_dice = set([()])
    temp_held = set(held_dice)
    temp_it = set(temp_held)
    for dummy in range(len(hand)):
        temp_set = set()
        for partial_held in temp_held:
            for item in hand:
                temp_it = list(partial_held)
                temp_it.append(item)
                temp_it.sort()
                if temp_it.count(item) <= hand.count(item):
                    temp_set.add(tuple(temp_it))
        temp_held = set(temp_set)
        for item2 in temp_held:
            held_dice.add(tuple(item2))
#        held_dice.add(tuple(list(temp_held)))
    return held_dice

def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    dice_hold = gen_all_holds(hand)
    value = 0
    for dices in dice_hold:
        new_value = expected_value(dices, num_die_sides, len(hand)-len(dices))
        if new_value > value:
            value = new_value
            dices_to_hold = dices
    return (value, dices_to_hold)

def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    

run_example()

#import poc_simpletest
#import poc_holds_testsuite as holds
#Test score function
#hands = poc_simpletest.TestSuite()
#hands.run_test(score((1,2,5,6,4)), 6, "Test 1")
#hands.run_test(score((1,5,5,6,6)), 12, "Test 2")
#hands.run_test(score((6,6,6,6,6)), 30, "Test 3")
#hands.run_test(score((2,5,4,3,3)), 6, "Test 4")
#hands.run_test(score((5,5,5,3,3)), 15, "Test 5")
#hands.report_results()

#Test expected value
#expec = poc_simpletest.TestSuite()
#expec.run_test(round(expected_value((2,2), 6 , 1),4), 4.8333)
#expec.run_test(round(expected_value((2,2), 6 , 2),4), 5.8333)
#expec.run_test(round(expected_value((3, 3), 8, 5),4), 11.3590)
#expec.report_results()

#Test gen_all_holds
#print gen_all_holds((1,1,3))
#holds.run_suite(gen_all_holds)

#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       
   