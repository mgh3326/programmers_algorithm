def solution(files):
    answer = []
    my_file_list = []
    for file in files:
        temp_list = []
        saved_idx = 0
        for idx, value in enumerate(file):
            if len(temp_list) == 0 and value.isdigit():
                saved_idx = idx
                temp_list.append(file[:idx])
            elif len(temp_list) > 0 and value.isdigit() == False:
                temp_list.append(file[saved_idx:idx])
                temp_list.append(file[idx:])
                break
        if len(temp_list) == 1:
            temp_list.append(file[saved_idx:])
        my_file_list.append(temp_list)
    my_file_list.sort(key=lambda x: (x[0].lower(), int(x[1])))
    for my_file in my_file_list:
        answer.append(''.join(my_file))
    return answer


print(
    solution(
        ["img12", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    )
)
