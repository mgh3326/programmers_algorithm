def solution(words):
    answer = 0
    temp_dict = {
        "name": "",
        "child": {},
        "value": 0
    }
    my_dict = {}
    for word in words:
        current_dict = my_dict
        for i in range(len(word)):
            word_value = word[i]
            if word_value not in current_dict:
                copy = temp_dict.copy()
                copy["name"] = i
                copy["value"] = 1
                current_dict[word_value] = copy
            current_dict = current_dict[word_value]["child"]

        print()

    return answer


print(
    solution(
        ["go", "gone", "guild"]
    )
)
