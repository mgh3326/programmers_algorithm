from math import ceil


def solution(enroll, referral, seller, amount):
    tree = {}
    enroll_index_hash = {}
    profits = [0] * len(enroll)
    for i, e in enumerate(enroll):
        enroll_index_hash[e] = i

    for i, r in enumerate(referral):
        if r == '-':
            continue
        tree[i] = enroll_index_hash[r]
    for s, a in (zip(seller, amount)):
        profit = a * 100
        enroll_index = enroll_index_hash[s]
        while True:
            current_profit = ceil(profit * 0.9)
            profits[enroll_index] += current_profit
            profit -= current_profit
            if profit == 0:
                break
            if enroll_index not in tree:
                break
            enroll_index = tree[enroll_index]
    return profits
