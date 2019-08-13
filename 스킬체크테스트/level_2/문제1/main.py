def solution(n):
    answer = ''

    temp_list = []
    if n == 1:
        return '1'


    while True:
        if n == 0:
            break
        temp = n % 3
        temp_list.append(temp)
        n = n // 3
    temp_list.reverse()
    for temp in temp_list:

        if temp == 0:
            answer += "4"
        elif temp == 1:
            answer += "1"

        elif temp == 2:
            answer += "2"

    return answer


# 전체 학생의 수
n_list = [
    3, 4, 5, 6, 7, 8, 9, 10
]

return_list = [
    4, 11, 12, 14, 21, 22, 24, 41

]
for p, _result in zip(n_list, return_list):
    print(n_list.index(p))
    result = solution(p)
    print(result)
    print(_result)
    if result == str(_result):
        print("맞음")
    else:
        print("틀림")
