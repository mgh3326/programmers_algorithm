def solution(s):
    number_hash = {"zero": "0",
                   "one": "1",
                   "two": "2",
                   "three": "3",
                   "four": "4",
                   "five": "5",
                   "six": "6",
                   "seven": "7",
                   "eight": "8",
                   "nine": "9"
                   }
    numbmer_set = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
    size_3_hash = {}
    size_4_hash = {}
    size_5_hash = {}
    for key in number_hash.keys():
        if len(key) == 3:
            size_3_hash[key] = number_hash[key]
        elif len(key) == 4:
            size_4_hash[key] = number_hash[key]
        elif len(key) == 5:
            size_5_hash[key] = number_hash[key]
    index = 0
    result_str = ""
    while True:
        if index == len(s):
            break
        value = s[index]
        index2 = index + 1
        if value in numbmer_set:
            result_str += value
        else:
            while True:
                value += s[index2]
                index2 += 1
                if len(value) == 3:
                    if value in size_3_hash:
                        result_str += size_3_hash[value]
                        break
                elif len(value) == 4:
                    if value in size_4_hash:
                        result_str += size_4_hash[value]
                        break
                elif len(value) == 5:
                    if value in size_5_hash:
                        result_str += size_5_hash[value]
                        break
        index = index2
    answer = int(result_str)
    return answer
