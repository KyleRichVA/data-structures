# -*- coding: utf-8 -*-
"""Insertion sort module."""
import time
from random import randint
from collections import deque


def sort(lst):
    """Merge sort function."""
    if len(lst) == 1:
        return lst
    if len(lst):
        indx = len(lst) >> 1
    left_lst = lst[:indx]
    right_lst = lst[indx:]
    # Spilt
    if len(left_lst) > 1:
        left_q = deque(sort(left_lst))
    else:
        left_q = deque(left_lst)
    if len(right_lst) > 1:
        right_q = deque(sort(right_lst))
    else:
        right_q = deque(right_lst)
    # Merge
    merged_list = []
    while len(left_q) or len(right_q):
        if len(left_q) and len(right_q):
            # put int mereged_List smallest item from qs
            if left_q[0] <= right_q[0]:
                merged_list.append(left_q.popleft())
            else:
                merged_list.append(right_q.popleft())
        elif len(left_q):  # Only left queue remaining
            merged_list.append(left_q.popleft())
        else:  # Only right queue remaining
            merged_list.append(right_q.popleft())
    return merged_list


if __name__ == "__main__":
    print("Merge sort will split up the list into single parts and merge together in order")
    print("For example, if given [3, 1, 4, 2] the expected output will be [1, 2, 3, 4]")
    print("Best case scenario (pre-sorted) [1, 2, 3, 4] the efficiency will be O(n)")
    print("Worst case scenario (reverse-sorted) [4, 3, 2, 1] the efficiency will be O(n log n)")

    print("Best Case Test:  list over range of 1-1000")
    lst_best = list(range(1000))
    start_best = time.time()
    sort(lst_best)
    end_best = time.time()
    diff_best = end_best - start_best
    print("Elapse time:  {} seconds".format(diff_best))

    print("Average Case Test:  list over range of 1-1000 with random order of values")
    lst_ave = [randint(0, 1000) for i in range(1000)]
    start_ave = time.time()
    sort(lst_ave)
    end_ave = time.time()
    diff_ave = end_ave - start_ave
    print("Elapse time:  {} seconds".format(diff_ave))

    print("Worst Case Test:  list over range of 1-1000 in reverse order (100-1)")
    lst_worst = list(range(1000))[::-1]
    start_worst = time.time()
    sort(lst_worst)
    end_worst = time.time()
    diff_worst = end_worst - start_worst
    print("Elapse time:  {} seconds".format(diff_worst))
