from collections import Counter


def solution(k, tangerine):
    answer = 0
    tangerine_counter = Counter()
    tangerine_counter.update(tangerine)
    for value in sorted(tangerine_counter.values(), reverse=True):
        k -= value
        answer+=1
        if k <= 0:
            break

    return answer
