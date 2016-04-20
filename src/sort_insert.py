# -*- coding: utf-8 -*-
"""Insertion sort module."""
import time
from random import randint


def sort(lst):
    """Insertion sort function."""
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[j] < lst[i]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    return lst


if __name__ == "__main__":
    print("Insertion sort will iterate over a list comparatively sorting items from lowest to highest value.")
    print("For example, if given [3, 1, 4, 2] the expected output will be [1, 2, 3, 4]")
    print("Best case scenario (pre-sorted) [1, 2, 3, 4] the efficiency will be O(n)")
    print("Worst case scenario (reverse-sorted) [4, 3, 2, 1] the efficiency will be O(n^2)")

    print("Best Case Test:  list over range of 1-100")
    lst_best = list(range(1000))
    start_best = time.time()
    sort(lst_best)
    end_best = time.time()
    diff_best = end_best - start_best
    print("Elapse time:  {} seconds".format(diff_best))

    print("Average Case Test:  list over range of 1-100 with random order of values")
    lst_ave = [randint(0, 1000) for i in range(1000)]
    start_ave = time.time()
    sort(lst_ave)
    end_ave = time.time()
    diff_ave = end_ave - start_ave
    print("Elapse time:  {} seconds".format(diff_ave))

    print("Worst Case Test:  list over range of 1-100 in reverse order (100-1)")
    lst_worst = list(range(1000))[::-1]
    start_worst = time.time()
    sort(lst_worst)
    end_worst = time.time()
    diff_worst = end_worst - start_worst
    print("Elapse time:  {} seconds".format(diff_worst))
