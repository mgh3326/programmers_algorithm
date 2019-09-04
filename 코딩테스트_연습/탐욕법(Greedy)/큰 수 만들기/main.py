import heapq


def solution(number, k):
    answer = ''
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
            heapq.heappush(remove_save_list, 1)

        else:
            heappop = remove_list.pop(0)
            # heappop = heapq.heappop(remove_list)
            heapq.heappush(remove_save_list, -1 * heappop[0])
    while True:
        if len(remove_save_list) == 0:
            break
        heapq_heappop = heapq.heappop(remove_save_list) * -1
        if heapq_heappop == -1:
            my_number_list.pop()
        else:
            my_number_list.pop(heapq_heappop)
    answer = ''.join(my_number_list)
    return answer


# # # 94
# print(
#     solution(
#         1231234, 5
#     )
# )
# 3234
print(
    solution(
        4177252841, 4

    )
)
# 775841
