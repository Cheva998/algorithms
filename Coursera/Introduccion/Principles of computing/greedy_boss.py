#http://www.codeskulptor.org/#user40_MLA7y9BFEg_5.py

"""
Simulator for greedy boss scenario
"""

import simpleplot
import math
import codeskulptor
import poc_simpletest as test
codeskulptor.set_timeout(1)

STANDARD = True
LOGLOG = False

# constants for simulation
INITIAL_SALARY = 100
SALARY_INCREMENT = 100
INITIAL_BRIBE_COST = 1000


def greedy_boss(days_in_simulation, bribe_cost_increment, plot_type = STANDARD):
    """
    Simulation of greedy boss
    """
    
    # initialize necessary local variables
    bank = 0
    tot_earn = 0
    bribe_money = False
    current_bribe_cost = INITIAL_BRIBE_COST
    salary = INITIAL_SALARY
    current_day = 0
    saved = 0
    days = 0
    # initialize list consisting of days vs. total salary earned for analysis
    days_vs_earnings = [(0, 0)]

    # Each iteration of this while loop simulates one bribe
    while current_day <= days_in_simulation:
        
        # check whether we have enough savings to bribe without waiting
        saving_days = int(math.ceil(float(current_bribe_cost - saved) / salary)) 
        days = int(math.ceil(float(current_bribe_cost) / salary))
        if saving_days < days:
        # advance current_day to day of next bribe (DO NOT INCREMENT BY ONE DAY)
            current_day += saving_days
            saved = salary * saving_days + saved - current_bribe_cost
            bank = salary * saving_days
        else:
            current_day += days
            bank = salary * (current_day - days_vs_earnings[-1][0])
            saved += salary * days - current_bribe_cost
         
        # update state of simulation to reflect bribe
        salary += SALARY_INCREMENT
        tot_earn += bank
        current_bribe_cost += bribe_cost_increment

        # update list with days vs total salary earned for most recent bribe
        # use plot_type to control whether regular or log/log plot
        if plot_type == STANDARD:
            days_vs_earnings.append((current_day, tot_earn))
        elif plot_type == LOGLOG:
            log_earn = math.log(tot_earn, 10)
            days_vs_earnings.append((current_day, log_earn))
    return days_vs_earnings


def run_simulations():
    """
    Run simulations for several possible bribe increments
    """
    plot_type = STANDARD
    plot_type = LOGLOG
    days = 70
    inc_0 = greedy_boss(days, 0, plot_type)
    inc_500 = greedy_boss(days, 500, plot_type)
    inc_1000 = greedy_boss(days, 1000, plot_type)
    inc_2000 = greedy_boss(days, 2000, plot_type)
    simpleplot.plot_lines("Greedy boss", 600, 600, "days", "total earnings", 
                          [inc_0, inc_500, inc_1000, inc_2000], False,
                         ["Bribe increment = 0", "Bribe increment = 500",
                          "Bribe increment = 1000", "Bribe increment = 2000"])

run_simulations()
greed = test.TestSuite()
greed.run_test(greedy_boss(35, 100), [(0, 0), (10, 1000), (16, 2200), (20, 3400), (23, 4600), (26, 6100), (29, 7900), (31, 9300), (33, 10900), (35, 12700), (37, 14700)])
greed.run_test(greedy_boss(35,0), [(0, 0), (10, 1000), (15, 2000), (19, 3200), (21, 4000), (23, 5000), (25, 6200), (27, 7600), (28, 8400), (29, 9300), (30, 10300), (31, 11400), (32, 12600), (33, 13900), (34, 15300), (34, 15300), (35, 16900), (36, 18600)])
greed.report_results()

#print greedy_boss(35, 100)
# should print [(0, 0), (10, 1000), (16, 2200), (20, 3400), (23, 4600), (26, 6100), (29, 7900), (31, 9300), (33, 10900), (35, 12700), (37, 14700)]


#print greedy_boss(35, 0)
# should print [(0, 0), (10, 1000), (15, 2000), (19, 3200), (21, 4000), (23, 5000), (25, 6200), (27, 7600), (28, 8400), (29, 9300), (30, 10300), (31, 11400), (32, 12600), (33, 13900), (34, 15300), (34, 15300), (35, 16900), (36, 18600)]
