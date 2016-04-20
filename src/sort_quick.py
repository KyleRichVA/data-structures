# -*- coding: utf-8 -*-
"""Quick sort module."""
import time
from random import randint


def sort(lst):
    """Quick sort function."""
    if len(lst):
        Pindx = len(lst) >> 1
    # set pivot as the middle of the list
    pivot = [lst[Pindx]]
    temp_left = lst[:Pindx]
    temp_right = lst[Pindx+1:]
    sort_left = []
    sort_right = []
    while len(temp_left):
        if temp_left[-1] <= pivot[0]:
            sort_left.append(temp_left.pop())
        else:
            sort_right.append(temp_left.pop())
    while len(temp_right):
        if temp_right[-1] <= pivot[0]:
            sort_left.append(temp_right.pop())
        else:
            sort_right.append(temp_right.pop())
    if len(sort_left):
        sort_left = sort(sort_left)
    if len(sort_right):
        sort_right = sort(sort_right)
    return sort_left + pivot + sort_right


if __name__ == "__main__":
    print("Quick sort will split the list based off comparison to a pivot point into 2 lists. These lists are recursively sorted and eventually connected back to pivot.")
    print("For example, if given [3, 1, 4, 2] the expected output will be [1, 2, 3, 4]")
    print("Best case scenario (pre-sorted) [1, 2, 3, 4] the efficiency will be O(n log n)")
    print("Worst case scenario (reverse-sorted) [4, 3, 2, 1] the efficiency will be O(n)")

    print("Best Case Test:  list over range of 1-10000")
    lst_best = list(range(10000))
    start_best = time.time()
    sort(lst_best)
    end_best = time.time()
    diff_best = end_best - start_best
    print("Elapse time:  {} seconds".format(diff_best))

    print("Average Case Test:  list over range of 1-10000 with random order of values")
    lst_ave = [randint(0, 1000) for i in range(10000)]
    start_ave = time.time()
    sort(lst_ave)
    end_ave = time.time()
    diff_ave = end_ave - start_ave
    print("Elapse time:  {} seconds".format(diff_ave))

    print("Worst Case Test:  list over range of 1-10000 in reverse order (100-1)")
    lst_worst = list(range(10000))[::-1]
    start_worst = time.time()
    sort(lst_worst)
    end_worst = time.time()
    diff_worst = end_worst - start_worst
    print("Elapse time:  {} seconds".format(diff_worst))
