def solution(lottos, win_nums):
    win_num_set = set(win_nums)
    blank_count = 0
    correct_count = 0
    result_hash = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6,
    }
    for lotto in lottos:
        if lotto == 0:
            blank_count += 1
        elif lotto in win_num_set:
            correct_count += 1

    answer = [result_hash[correct_count + blank_count], result_hash[correct_count]]
    return answer
