def solution(msg):
    answer = []
    lzw_dict = {}
    stack = []
    temp_str = ""
    for i in range(ord('A'), ord('Z') + 1):
        lzw_dict[chr(i)] = i - ord('A') + 1
    msg_idx = 0
    while True:
        if msg_idx == len(msg):
            break
        msg_value = msg[msg_idx]
        temp_str += msg_value
        if temp_str not in lzw_dict:
            answer.append(lzw_dict[temp_str[:-1]])
            lzw_dict[temp_str] = len(lzw_dict) + 1
            temp_str = ""
        else:
            msg_idx += 1
    answer.append(lzw_dict[temp_str])
    return answer


print(
    solution(
        "KAKAO"
    )
)
#  [11, 1, 27, 15]
