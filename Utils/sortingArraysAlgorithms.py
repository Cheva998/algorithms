import math

def quadraticSort(array):
    n = len(array)
    for idx in range(0, n-1):
        for jdx in range(idx, n):
            if array[idx] > array[jdx]:
                lower = array[idx]
                upper = array[jdx]
                array[idx] = upper
                array[jdx] = lower
    
    return array


def binarySearch(array, value):
    n = len(array) - 1
    iterations = math.ceil(math.log(6, 2)) + 1
    lower = 0
    upper = n
    #print(f'-----------\nvalue: {value}')
    if value < array[lower]:
        return lower
    if value > array[upper]:
        return upper + 1
    for idx in range(0, iterations):
        index = ((upper - lower) // 2) + lower
        #print(f'upp: {upper} - low: {lower}')
        #print(f'{idx} index: {index}')
        if array[index] == value:
            return index
        elif (upper - lower) <= 1:
            return index + 1

        if value < array[index]:
            upper = index
        elif value > array[index]:
            lower = index

def binarySort(array):
    new_array = [array[0]]
    for array_id in range(1, len(array)):
        value = array[array_id]
        bin_index = binarySearch(new_array, value)
        new_array = new_array[:bin_index] + [value] + new_array[bin_index:]
    return new_array


def testSortingFunctions(function_to_test):
    array1 = [2, 4, 2, 1]
    array2 = [3, 2, 1]
    array3 = [2, 3, 4]
    assert function_to_test(array1) == [1, 2, 2, 4]
    assert function_to_test(array2) == [1, 2, 3]
    assert function_to_test(array3) == array3


def testSearch(function_to_test):
    array1 = [1, 2, 3, 5, 7, 9, 12]
    assert function_to_test(array1, 0) == 0
    assert function_to_test(array1, 1) == 0
    assert function_to_test(array1, 2) == 1
    assert function_to_test(array1, 6) == 4
    assert function_to_test(array1, 12) == 6
    assert function_to_test(array1, 13) == 7

testSortingFunctions(quadraticSort)
testSortingFunctions(binarySort)
testSearch(binarySearch)

print('all good')
