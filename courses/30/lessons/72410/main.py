def solution(new_id):
    new_id = new_id.lower()

    possible_set = set("0123456789-_.").union(list(map(chr, range(ord('a'), ord('z') + 1))))
    answer = ""
    for value in new_id:
        if value in possible_set:
            answer += value
    while True:
        temp_len = len(answer)
        answer = answer.replace("..", ".")
        if temp_len == len(answer):
            break

    if answer[0] == ".":
        answer = answer[1:]
    if len(answer) > 1 and answer[-1] == ".":
        answer = answer[:-1]
    if answer == "":
        answer = "a"
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]
    if len(answer) <= 2:
        answer += answer[-1] * (3 - len(answer))
    return answer
