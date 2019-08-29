def solution(files: list):
    answer = []

    my_dict = {}

    for file in files:
        head = ""
        number = ""
        tail = ""
        number_start_start = 0
        for file_idx, file_value in enumerate(file):
            if file_value.isdigit():
                head = file[:file_idx]
                number_start_start = file_idx
                break
        number_tail = file[number_start_start:]
        tail_idx = 0
        for file_idx, file_value in enumerate(number_tail):
            if not file_value.isdigit():

                number = number_tail[:file_idx]
                tail_idx = file_idx
                break
            else:
                if file_idx == 5:
                    number = number_tail[:file_idx]
                    tail_idx = file_idx

                    break
        if tail_idx == 0:
            number = number_tail
        else:
            tail = number_tail[tail_idx:]
        temp_head = ""
        for idx, head_value in enumerate(head):
            if head_value.islower():
                temp_head += head_value.upper()
            else:
                temp_head += head_value

        if temp_head not in my_dict:
            my_dict[temp_head] = {}
        if int(number) not in my_dict[temp_head]:
            my_dict[temp_head][int(number)] = []
        my_dict[temp_head][int(number)].append((head, number, tail))

        # if head[0].islower():
        #     heapq.heappush(my_dict[temp_head], ((int(number), 1), (head, number, tail)))
        # else:
        #     heapq.heappush(my_dict[temp_head], ((int(number), 2), (head, number, tail)))
    for key in sorted(my_dict.keys()):  # Head 사전 순 구현

        for key_key in sorted(my_dict[key].keys()):
            for i in my_dict[key][key_key]:

                temp_str = i[0] + i[1] + i[2]
                answer.append(temp_str)

    return answer


files_list = [
    ["a0001", "a0", "a00"],
    ["a1", "a-1", "a01", "a0101.09.zip", "app.0.zip", "ver.009.zip", "ver.10.zip", "ver.09.zip", "ve.9.zip",
     "very.009.zip", "a1"],
    ["a0", "a99999", "a0000.zip", "a0101.09.zip", "app.0.zip", "ver.009.zip", "ver.10.zip", "ver.09.zip", "ve.9.zip",
     "very.009.zip", "a1"],
    ["muzi1.txt", "MUZI1.txt", "muzi001.txt", "muzi1.TXT"],
    ["muzi1.ZIP", "muzi99999.ZIP", "muzi999999.ZIP", "muzi999990.ZIP", "muzi1-00000.ZIP", "muzi002.png", "muzi001.png",
     "muzi1.zip"],

    # ["F-05 Freedom Fighter", "F-5 Freedom Fighter", "F-005 Freedom Fighter", "B-50 Superfortress",
    #  "A-10 Thunderbolt II", "F-14 Tomcat"],
    ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"],
    # ["img12.png", "img10.png", "img2.png", "img1.png", "muzi1.txt", "MUZI1.txt", "muzi001.txt", "muzi1.TXT"],
    # ["muzi1.txt", "MUZI1.txt", "muzi001.txt", "muzi1.TXT"],
    # ["foo9.txt"],
    # ["foo010bar020.zip"],
    # ["F-15"],
    # ["MUZI01.zip", "muzi1.png"],
    # ["img12.png", "img10.png", "img002.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"],
    ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"],

]

return_list = [
    # [".txt", "MUZI1.txt", "muzi001.txt", "muzi1.TXT"],
    #
    # ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"],
    ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"],
    # ["img1.png", "img2.png", "img10.png", "img12.png", "muzi1.txt", "MUZI1.txt", "muzi001.txt", "muzi1.TXT"],
    # ["muzi1.txt", "MUZI1.txt", "muzi001.txt", "muzi1.TXT"],
    # ["foo9.txt"],
    # ["foo010bar020.zip"],
    # ["F-15"],
    # ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"],
    # ["MUZI01.zip","muzi1.png"],
    ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"],
    ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"],
    ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"],

]
for _input_data in zip(files_list, return_list):
    _0 = _input_data[0]
    _r = _input_data[-1]
    print(files_list.index(_0))
    result = solution(_0)
    print(result)
    print(_r)
    if result == _r:
        print("맞음")
    else:
        print("틀림")
