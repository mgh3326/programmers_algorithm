import itertools
from collections import Counter


def solution(orders, course):
    answer = []
    for course_value in course:
        comb_counter = Counter()
        for order in orders:
            combs = (itertools.combinations(sorted(order), course_value))
            comb_counter.update(combs)
        if comb_counter:
            max_order_count = max(comb_counter.values())
            if max_order_count >= 2:
                for order, count in comb_counter.items():
                    if count == max_order_count:
                        answer.append("".join(order))
    return sorted(answer)
