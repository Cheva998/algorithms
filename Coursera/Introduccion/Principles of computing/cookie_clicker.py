#http://www.codeskulptor.org/#user40_albvgGoH33_8.py

"""
Cookie Clicker Simulator
"""

import simpleplot
import math
# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0
#SIM_TIME = 1000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    def __init__(self):
        self._total_produced = 0.0
        self._current_cookies = 0.0
        self._time = 0.0
        self._cps = 1.0 #Cookies per second
        self._history = [(self._time, None, 0.0, self._total_produced)]
        self._copy_his = list()
        self._printable_state = ""

    def __str__(self):
        """
        Return human readable state
        """
        self._printable_state = "Produced: " + str(self._total_produced) + "\n"
        self._printable_state += "Current cookies: " + str(self._current_cookies) + "\n"
        self._printable_state += "Time: " + str(self._time) + "\n"
        self._printable_state += "Cookies per second: " + str(self._cps)
        return self._printable_state

    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_cookies

    def get_cps(self):
        """
        Get current CPS
        Should return a float
        """
        return self._cps

    def get_time(self):
        """
        Get current time
        Should return a float
        """
        return self._time

    def get_history(self):
        """
        Return history list
        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)
        For example: [(0.0, None, 0.0, 0.0)]
        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        self._copy_his = list(self._history)
        return self._copy_his

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)
        Should return a float with no fractional part
        """
        cookies_left = cookies - self._current_cookies
        if cookies_left > 0:
            time_left = math.ceil(float(cookies_left) / self._cps)
        else:
            time_left = 0.0
        return time_left

    def wait(self, time):
        """
        Wait for given amount of time and update state
        Should do nothing if time <= 0.0
        """
        if time > 0.0:
            self._time += time
            self._current_cookies += time * self._cps
            self._total_produced += time * self._cps

    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state
        Should do nothing if you cannot afford the item
        """
        if cost <= self._current_cookies:
            self._current_cookies -= cost
            self._cps += additional_cps
            self._history.append((self._time, item_name, cost, self._total_produced))

def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    clone_info = build_info.clone()
    clicky = ClickerState()
    while clicky.get_time() <= duration:
        item = strategy(clicky.get_cookies(), clicky.get_cps(), clicky.get_history(), 
                        duration - clicky.get_time(), clone_info)
        if item == None:
            clicky.wait(duration - clicky.get_time())
            break
        cost = clone_info.get_cost(item)
        add_cps = clone_info.get_cps(item)
        time_until = clicky.time_until(cost)
        if time_until + clicky.get_time() > duration:
            clicky.wait(duration - clicky.get_time())
            break
        else:
            clicky.wait(time_until)
        clicky.buy_item(item, cost, add_cps)
        clone_info.update_item(item)
    return clicky

def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!
    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None
    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    item_list = build_info.build_items()
    prices = [build_info.get_cost(each) for each in item_list]
    cheap_item = []
    while len(cheap_item) == 0:
        min_price = min(prices)
        pos = prices.index(min_price)
        min_price = prices.pop(pos)
        time_for = math.ceil((min_price - cookies) / cps)
        if time_for <= time_left:
            cheap_item = item_list.pop(pos)
        else:
            item_list.pop(pos)
        if len(item_list) == 0 and len(cheap_item) == 0:
            cheap_item = None
            break
    print cheap_item
    return cheap_item

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    item_list = build_info.build_items()
    prices = [build_info.get_cost(each) for each in item_list]
    expen_item = []
    while len(expen_item) == 0:
        max_price = max(prices)
        pos = prices.index(max_price)
        print item_list, prices, max_price
        max_price = prices.pop(pos)
        print max_price
        time_for = math.ceil((max_price - cookies) / cps)
        print time_for, time_left
        print time_for <= time_left
        if time_for <= time_left:
            expen_item = item_list.pop(pos)
        else:
            item_list.pop(pos)
        if len(item_list) == 0 and len(expen_item) == 0:
            expen_item = None
            break
    print expen_item
    return expen_item

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    item_list = build_info.build_items()
    prices = [build_info.get_cost(each) for each in item_list]
    time_rel = [build_info.get_cps(each) / (build_info.get_cost(each) / cps) 
              for each in item_list]
#    add_cpss = [build_info.get_cps(idx) for idx in item_list]
#    periods = [time_left - math.ceil((price - cookies) / cps) for price in prices] 
#    exp_cookies = [prices[idx] * (1 + add_cpss[idx] / prices[idx]) ** (periods[idx])
#                   for idx in range(len(item_list))]
#    time_rel = list(exp_cookies)
    best_item = []
    while len(best_item) == 0:
        max_time_rel = max(time_rel)
        pos = time_rel.index(max_time_rel)
        max_price = prices.pop(pos)
        time_rel.pop(pos)
        time_for = math.ceil((max_price - cookies) / cps)
        if time_for <= time_left:
            best_item = item_list.pop(pos)
        else:
            item_list.pop(pos)
        if len(item_list) == 0 and len(best_item) == 0:
            best_item = None
            break
    return best_item

def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    history = state.get_history()
    history = [(item[0], item[3]) for item in history]
    simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
#    run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
#    run_strategy("Cheap", SIM_TIME, strategy_cheap)
#    run_strategy("Expensive", SIM_TIME, strategy_expensive)
    run_strategy("Best", SIM_TIME, strategy_best)

run()
#strategy_cheap(2.0, 1.0, [(0.0, None, 0.0, 0.0)], 1.0, provided.BuildInfo({'A': [5.0, 1.0], 'C': [50000.0, 3.0], 'B': [500.0, 2.0]}, 1.15)) 
#strategy_cheap(500000.0, 1.0, [(0.0, None, 0.0, 0.0)], 5.0, provided.BuildInfo({'A': [5.0, 1.0], 'C': [50000.0, 3.0], 'B': [500.0, 2.0]}, 1.15))

#strategy_expensive(1.0, 3.0, [(0.0, None, 0.0, 0.0)], 17.0, provided.BuildInfo({'A': [5.0, 1.0], 'C': [50000.0, 3.0], 'B': [500.0, 2.0]}, 1.15))