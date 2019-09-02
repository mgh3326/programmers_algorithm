import itertools


def primes_up_to_good(n: int) -> [int]:
    seive = [False, False] + [True] * (n - 1)
    for k in range(2, int(n ** 0.5 + 1.5)):
        if seive[k]:
            seive[k * 2::k] = [False] * ((n - k) // k)
    return [x for x in range(n + 1) if seive[x]]


def solution(numbers):
    my_set = set()
    for i in range(1, len(numbers) + 1):
        for permutation in itertools.permutations(numbers, i):
            my_set.add(int(''.join(permutation)))
    good = primes_up_to_good(max(my_set))
    answer = 0
    for i in my_set:
        if i in good:
            answer += 1
    return answer


print(
    solution(
        "17"
    )
)
# 3
print(
    solution(
        "011"
    )
)
# 2
