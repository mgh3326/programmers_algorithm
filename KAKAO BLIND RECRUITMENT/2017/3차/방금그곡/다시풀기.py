def solution(m, musicinfos):
    answer = ''
    answer_music_length = 0
    my_dict = {
        "C#": 'a',
        "D#": 'b',
        "F#": 'c',
        "G#": 'd',
        "A#": 'e'
    }
    m = music_content_replace(m, my_dict)

    for musicinfo in musicinfos:
        start_time, end_time, music_name, music_content = musicinfo.split(",")
        music_content = music_content_replace(music_content, my_dict)
        start_minute = time_to_minute(start_time)
        end_minute = time_to_minute(end_time)
        music_length = end_minute - start_minute
        current_music_content = (music_content * (len(m) + 1))[:music_length]
        if m in current_music_content:
            if answer == "" or answer_music_length < music_length:
                answer = music_name
                answer_music_length = music_length
    if answer == "":
        answer = "(None)"
    return answer


def music_content_replace(m, my_dict):
    for my_dict_key in my_dict.keys():
        m = m.replace(my_dict_key, my_dict[my_dict_key])
    return m


def time_to_minute(start_time):
    hour, minute = map(int, start_time.split(":"))
    start_minute = hour * 60 + minute
    return start_minute


print(
    solution(
        "ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
    )
)
