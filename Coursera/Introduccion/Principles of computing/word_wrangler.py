#http://www.codeskulptor.org/#user42_jQoCDEnmAU_22.py


"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    list2 = []
    for idx in list1:
        if idx not in list2:
            list2.append(idx)
    return list2

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    list3 = []
    for idx in list1:
        for idy in list2:
            if idx == idy:
                list3.append(idx)
    return list3

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """   
#    list3 = list1 + list2
#    list3 = merge_sort(list3)
#    list3 = remove_duplicates(list3)
    list3 = list(list1)
    list4 = list(list2)
    count = 0
    for idx in list2:
        dim = len(list3)
        for idy in range(count,dim):
            if idx < list3[idy]:
                list3.insert(idy, idx)
                list4.remove(idx)
                count += 1
                break
    if len(list4) > 0:
        for idx in list4:
            list3.append(idx)
    return list3
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    dim = len(list1)
    
    if dim <= 1:
        return list1
    else:
        half = dim // 2
        first = merge_sort(list1[:half])
        last = merge_sort(list1[half:])
        return merge(first, last)
                           
        
# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word) == 0:
        return [""]
    else:
        first = word[0]
        last = word[1:]
        rest_strings = gen_all_strings(last)
        rest_string1 = []
        for idx in rest_strings:
            for idy in range(len(idx) + 1):

                if idy == 0:
                    string1 = first + idx
                elif idy <= len(idx):
                    string1 = idx[:idy] + first + idx[idy:]
                else:
                    string1 = idx + first
                rest_string1.append(string1)

        rest_strings.extend(rest_string1)
    return rest_strings

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    
    full_text = urllib2.urlopen(codeskulptor.file2url(filename))
#    data = full_text.read()
    all_words = []
    for idx in full_text.readlines():
        all_words.append(idx[:-1])
#        print idx[:-1]
    return all_words

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
run()
###Test remove_duplicates
#print remove_duplicates(["a", "c", "b", 'b', '1', 'a'])
#print remove_duplicates([0, 1, 2, 3, 4]) 

###Test intersect
#print intersect(["a", "b"], ["c", "a", "a"])

###Test merge
#print merge(["c", "d"], ["a", "b"])
#print merge(["a", "b" , "c"], ["a" ,"c", "d"])
#print merge([], ["a", "b"])
#print merge(["a", "b"], [])

###Test merge_sort
#print merge_sort(["", "z", 'b', 'a', "e", 't', 'b'])

###Test gen_all_strings
#print gen_all_strings("aab")

###Test load_words
#print load_words(WORDFILE)