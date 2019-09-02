def solution(n, lost: list, reserve: list):
    answer = n - len(lost)
    my_dict = {}
    # 한쪽에만 빌릴수 있는 애들을 먼저 빌려주도록 하자
    for i in range(n):
        if i + 1 in lost and i + 1 in reserve:
            lost.remove(i + 1)
            reserve.remove(i + 1)
            answer+=1
    while True:
        remove_lost_list = []
        for _lost in lost:
            save_list = []
            for _reserve in reserve:
                if _lost - _reserve == 1 or _lost - _reserve == -1:
                    save_list.append(_reserve)

            if len(save_list) == 1:
                reserve.remove(save_list[0])
                remove_lost_list.append(_lost)
                answer += 1
        if len(remove_lost_list) == 0:
            break
        for remove_lost in remove_lost_list:
            lost.remove(remove_lost)
    for _lost in lost:
        for _reserve in reserve:
            if _lost - _reserve == 1 or _lost - _reserve == -1:
                reserve.remove(_reserve)
                answer += 1
                break
    return answer


# 전체 학생의 수
n_list = [
    5, 5, 3
]

# 도난 당한 학생의 배열
lost_list = [
    [2, 4],
    [2, 4],
    [3]
]
# 여별 체육복
reserve_list = [
    [1, 3, 5]
    , [3]
    , [1]
]
return_list = [
    5, 4, 2

]
for p, c, _r, _result in zip(n_list, lost_list, reserve_list, return_list):
    print(n_list.index(p))
    result = solution(p, c, _r)
    print(result)
    print(_result)
    if result == _result:
        print("맞음")
    else:
        print("틀림")
