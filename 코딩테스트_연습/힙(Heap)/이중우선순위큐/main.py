import heapq


def solution(operations):
    answer = []
    my_list = []
    inverse_my_list = []
    for operation in operations:
        order, value = operation.split()
        value = int(value)
        if order == "I":
            heapq.heappush(my_list, value)
            heapq.heappush(inverse_my_list, -1 * value)
        else:
            if value == -1:
                if len(my_list) != 0:
                    heappop = heapq.heappop(my_list)
                    inverse_my_list.remove(heappop * -1)
            else:
                if len(inverse_my_list) != 0:
                    heappop = heapq.heappop(inverse_my_list)
                    my_list.remove(heappop * -1)
    if len(inverse_my_list) != 0:
        heappop = heapq.heappop(inverse_my_list) * -1
    else:
        heappop = 0
    answer.append(heappop)
    if len(my_list) != 0:
        heappop = heapq.heappop(my_list)
    else:
        heappop = 0
    answer.append(heappop)
    return answer


print(

    solution(
        ["I 16", "D 1"]
    )
)
#	[0,0]

print(

    solution(
        ["I 7", "I 5", "I -5", "D -1"]
    )
)
#	[0,0]
