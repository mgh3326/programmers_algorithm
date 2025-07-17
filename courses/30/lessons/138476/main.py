from collections import Counter


def solution(k, tangerine):
    tangerine_counter = Counter(tangerine)
    answer = 0
    for count in sorted(tangerine_counter.values(), reverse=True):
        k -= count
        answer += 1
        if k <= 0:
            break
    return answer
