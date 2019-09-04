import heapq


# TODO 스택을 이용하면 아주 효율적으로 문제를 풀수 있다.
def solution(number, k):
    answer = ''
    stack = [number[0]]
    number_str = str(number)
    my_number_list = list(number_str)

    my_number_dict = {'0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': []}
    # 맨 앞자리 부터 최솟값을 제거해주는 방향으로 가면 좋을 것 같다.
    remove_list = []
    current_index = 0
    is_end = False
    for idx, my_number in enumerate(my_number_list):
        if is_end == True:
            break
        for my_number_dict_key in my_number_dict.keys():
            if is_end == True:
                break
            if my_number_dict_key < my_number:
                while True:
                    if len(my_number_dict[my_number_dict_key]) == 0:
                        break
                    pop = my_number_dict[my_number_dict_key].pop()
                    remove_list.append((pop, my_number_dict_key))
                    # heapq.heappush(remove_list, (pop, my_number_dict_key))
                    if len(remove_list) >= k:
                        is_end = True
                        break
                # my_number_dict.pop(my_number_dict_key)
        if my_number not in my_number_dict:
            my_number_dict[my_number] = []
        my_number_dict[my_number].append(idx)
    remove_save_list = []
    for i in range(k):
        if len(remove_list) == 0:
            break

        else:
            heappop = remove_list.pop(0)
            # heappop = heapq.heappop(remove_list)
            heapq.heappush(remove_save_list, heappop[0])
    current_index = 0
    heapq_heappop = 0
    while True:
        if len(remove_save_list) == 0:
            break
        heapq_heappop = heapq.heappop(remove_save_list)
        while True:
            if current_index != heapq_heappop:
                answer += number_str[current_index]
                current_index += 1
            else:
                current_index += 1
                break
    if current_index == 0 and heapq_heappop == 0:
        answer += number_str[:len(number_str) - k]
    else:
        answer += number_str[heapq_heappop + 1:heapq_heappop + 1 + len(number_str) - k]
    return answer


# # # 94
print(
    solution(
        9111, 2
    )
)
# 3234
print(
    solution(
        4177252841, 4

    )
)
# 775841
