import itertools


def solution(relation):
    answer = 0
    index_list = []
    result_set = set()
    for i in range(len(relation[0])):
        index_list.append(i)
    for index in index_list:
        my_set = set()
        for relation_value in relation:
            if relation_value[index] in my_set:
                break
            my_set.add(relation_value[index])
        if len(my_set) == len(relation):
            result_set.add(index)
    for r in range(len(relation[0]))[2:]:
        combinations = list(itertools.combinations(index_list, r))
        for index in combinations:
            my_set = set()
            for relation_value in relation:
                if relation_value[index] in my_set:
                    break
                my_set.add(relation_value[index])
            if len(my_set) == len(relation):
                print()
                result_set.add(index)
    return answer


print(
    solution(
        [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
         ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
    )
)
