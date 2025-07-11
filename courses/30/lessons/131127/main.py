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
        for key, value in want_count_hash.items():
            if value != discount_hash.get(key, 0):
                break
        else:
            answer += 1
        current_index += 1
    return answer
