import itertools


def primes_up_to_good(n: int) -> [int]:
    seive = [False, False] + [True] * (n - 1)
    for k in range(2, int(n ** 0.5 + 1.5)):
        if seive[k]:
            seive[k * 2::k] = [False] * ((n - k) // k)
    return [x for x in range(n + 1) if seive[x]]


def solution(nums):
    answer = 0
    numbers_sum = sum(nums)
    good = primes_up_to_good(numbers_sum)
    my_set = set()

    combinations = list(itertools.combinations(nums, 3))
    for combination in combinations:

        combination_sum = sum(combination)
        if combination_sum in good:
            answer += 1
    return answer


print(
    solution(
        [1, 2, 3, 4]
    )
)
print(
    solution(
        [1, 2, 7, 6, 4]
    )
)
