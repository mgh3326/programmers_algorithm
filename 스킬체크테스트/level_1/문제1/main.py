def solution(strings: list, n: int):
    answer = []
    my_dict = {}
    for string in strings:
        if string[n] in my_dict:
            my_dict[string[n]].append(string)
        else:
            my_dict[string[n]] = [string]
    for temp in sorted(my_dict):
        for _temp in sorted(my_dict[temp]):
            answer.append(_temp)

    return answer


strings_list = [
    ["sun", "bed", "car"],
    ["abce", "abcd", "cdx"]
]

n_list = [
    1, 2

]
return_list = [
    ["car", "bed", "sun"],
    ["abcd", "abce", "cdx"]

]
for p, c, r in zip(strings_list, n_list, return_list):
    print(strings_list.index(p))
    result = solution(p, c)
    print(result)
    if result == r:
        print("맞음")
    else:
        print("틀림")
