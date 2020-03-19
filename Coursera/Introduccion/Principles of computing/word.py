def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    list2 = []
    count = 0
    for idx in list1:
        is_same = False
        for idy in list1[count:]:
            if idx == idy:
                is_same = True
                continue
            else:
                is_same = False
        if not is_same and idx not in list2:
            list2.append(idx)
        count += 1
    return list2

print remove_duplicates([0, 1, 2, 3, 4]) 
