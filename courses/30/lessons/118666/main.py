def solution(survey, choices):
    user_personality_names = ["RT",
                              "CF",
                              "JM",
                              "AN"]
    user_personality_scores = [0, 0, 0, 0]
    scores = [-3, -2, -1, 0, 1, 2, 3]
    for i, value in enumerate(survey):
        sorted_value = "".join(sorted(value))
        personality_index = user_personality_names.index(sorted_value)
        direction = 1
        if value != sorted_value:
            direction = -1
        choice = choices[i]
        user_personality_scores[personality_index] += scores[choice - 1] * direction
    answer = ''
    for i, user_personality_name in enumerate(user_personality_names):
        if user_personality_scores[i] <= 0:
            answer += user_personality_name[0]
        else:
            answer += user_personality_name[1]
    return answer
