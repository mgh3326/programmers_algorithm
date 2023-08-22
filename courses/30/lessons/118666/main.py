def solution(survey, choices):
    user_personalities = {"RT": 0, "CF": 0, "JM": 0, "AN": 0}
    scores = [-3, -2, -1, 0, 1, 2, 3]

    for survey_value, choice in zip(survey, choices):
        sorted_value = "".join(sorted(survey_value))
        score_direction = -1 if survey_value != sorted_value else 1
        chosen_score = scores[choice - 1] * score_direction
        user_personalities[sorted_value] += chosen_score

    answer = [name[0] if score <= 0 else name[1] for name, score in user_personalities.items()]
    return "".join(answer)
