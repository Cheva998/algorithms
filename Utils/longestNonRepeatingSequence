


def getLargestSequenceIndex(array):
    left = 0
    last_seen = {}
    best_left = 0
    best_right = 0

    for idx in range(len(array)):
        value = array[idx]
        if (value in last_seen) and (last_seen[value] >= left):
            left = last_seen[value] + 1
        if ((idx - left) >= (best_right - best_left)):
            best_left = left
            best_right = idx
        last_seen[value] = idx
    if (len(array) - left) > (best_right - best_left):
        best_left = left
        best_right = len(array)
    return best_left, best_right


def largestSequence(array):
    if len(array) <= 1:
        return array
    best_left, best_right = getLargestSequenceIndex(array)
    return array[best_left: best_right]


def testLargestSequence(func_to_test):
    array1 = [2, 3, 5, 3, 4, 7, 5, 8]
    expected1 = [3, 4, 7, 5, 8]
    assert func_to_test(array1) == expected1

    array2 = [1 ,2]
    expected2 = [1, 2]
    assert func_to_test(array2) == expected2

    array3 = [1, 1]
    expected3 = [1]
    assert func_to_test(array3) == expected3

    array4 = [1, 2, 3, 2, 4, 5]
    expected4 = [3, 2 , 4, 5]
    assert func_to_test(array4) == expected4

    array5 = [1,2,3,1,4,3,1,2,3,4,5]
    expected5 = [1,2,3,4,5]
    assert func_to_test(array5) == expected5


testLargestSequence(largestSequence)
print('all good')
