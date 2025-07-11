def solution(want, number, discount):
    answer = 0
    want_count_hash = {}

    for i in range(len(want)):
        want_count_hash[want[i]] = number[i]
    current_index = 0
    size = 10
    while True:
        if size + current_index > len(discount):
            break
        discount_hash = {}
        for value in discount[current_index:size + current_index]:
            discount_hash[value] = discount_hash.get(value, 0) + 1
        r = False
        keys = list(want_count_hash.keys())
        for i in range(len(keys)):
            key = keys[i]
            if want_count_hash[key] != discount_hash.get(key, 0):
                break
            if i == len(keys) - 1:
                r = True
        if r == True:
            answer += 1
        current_index += 1
    return answer
