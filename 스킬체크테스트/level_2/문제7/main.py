def solution(numbers: list):
    if numbers.count(0) == len(numbers):
        return 0

    answer = ""
    str_number_list = []
    for number in numbers:
        str_number_list.append(str(number))

    while True:
        if len(str_number_list) == 0:
            break
        temp_max = str_number_list[0]
        for str_number in (str_number_list[1:]):
            if int(str_number + temp_max) > int(temp_max + str_number):
                temp_max = str_number
        str_number_list.remove(temp_max)
        answer += temp_max
    return answer


arrangement_list = [
    [6, 10, 2],
    [3, 30, 34, 5, 9],
    [0, 0],

]
return_list = [
    "6210",
    "9534330",
    "0"

]
for _h, r in zip(arrangement_list, return_list):
    print("index : ", end="")
    print(arrangement_list.index(_h))
    result = solution(_h)
    print(result)
    print(r)
    if result == r:
        print("맞음")
    else:
        print("틀림")
