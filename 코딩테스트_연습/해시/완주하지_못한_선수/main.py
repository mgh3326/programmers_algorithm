def solution(participant, completion):
    completion_dict = {}

    for _c in completion:
        if _c in completion_dict:
            completion_dict[_c] += 1
        else:
            completion_dict[_c] = 1
    for _p in participant:
        if _p in completion_dict:
            if completion_dict[_p] == 1:
                completion_dict.pop(_p)
            else:
                completion_dict[_p] -= 1

        else:
            return _p


participant_list = [
    ["leo", "kiki", "eden"],
    ["marina", "josipa", "nikola", "vinko", "filipa"],
    ["mislav", "stanko", "mislav", "ana"]
]
completion_list = [
    ["eden", "kiki"],
    ["josipa", "filipa", "marina", "nikola"],
    ["stanko", "ana", "mislav"]
]
return_list = [
    "leo",
    "vinko",
    "mislav"
]
for p, c, r in zip(participant_list, completion_list, return_list):
    print(participant_list.index(p))
    result = solution(p, c)
    if result == r:
        print("맞음")
    else:
        print("틀림")
