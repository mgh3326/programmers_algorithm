def solution(words: list):
    answer = 0
    my_dict = {}
    sorted_words = sorted(words)
    word_dict = {}
    full_word_dict = {}
    # 1. 글자 수대로 단어를 가지고 있자. -> sort를 해주자
    #
    pre_word = ""
    for word in sorted_words:
        if word[0] not in my_dict:
            my_dict[word[0]] = []
        my_dict[word[0]].append(word)
        word_dict[word] = 1
    for my_dict_key in my_dict.keys():
        if len(my_dict[my_dict_key]) == 1:
            answer += 1
            word_dict.pop(my_dict[my_dict_key][0])
        for idx, word in enumerate(my_dict[my_dict_key][:-1]):
            is_change = True
            while True:
                if is_change == False:
                    break

                find_length = word_dict[word] + 1
                find_word = word[:find_length]
                if find_word != my_dict[my_dict_key][idx + 1][:find_length]:  # 다음꺼가 안 같으면 백트레킹
                    break

                is_change = False
                for two_word in my_dict[my_dict_key][idx + 1:]:
                    if two_word[:find_length] == find_word:
                        if not is_change:
                            word_dict[word] = find_length
                            is_change = True
                        word_dict[two_word] = find_length
                    else:
                        break  # 백트레킹

    for word_dict_key in word_dict.keys():

        key_ = word_dict[word_dict_key]
        answer += key_
        if key_ != len(word_dict_key):
            answer += 1

    return answer


words_list = [
    ["go", "gone", "guild"],
    ["abc", "def", "ghi", "jklm"],
    ["word", "war", "warrior", "world"],
]
return_list = [
    7, 4, 15
]
for _input_data in zip(words_list, return_list):
    _0 = _input_data[0]
    _r = _input_data[-1]
    print(words_list.index(_0))
    result = solution(_0)
    print(result)
    print(_r)
    if result == _r:
        print("맞음")
    else:
        print("틀림")
