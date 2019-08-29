def meldy_to_list(melody_sharp_list, music_song):
    for idx, melody_sharp in enumerate(melody_sharp_list):
        if melody_sharp in music_song:
            music_song = music_song.replace(melody_sharp, str(idx))
    return music_song


def solution(m, musicinfos: list):  # 기억한 멜로디 , # 방송곡의 정보
    answer = ""
    current_time = 0
    melody_list = ["C", "0", "D", "1", "E", "F", "2", "G", "3", "A", "4", "B"]
    melody_sharp_list = ["C#", "D#", "F#", "G#", "A#"]
    my_music_list = []
    m = meldy_to_list(melody_sharp_list, m)
    for musicinfo in musicinfos:
        start_time, end_time, music_name, music_song = musicinfo.split(",")
        start_hour, start_minute = map(int, start_time.split(":"))
        end_hour, end_minute = map(int, end_time.split(":"))
        start_minute += start_hour * 60
        end_minute += end_hour * 60
        music_song = meldy_to_list(melody_sharp_list, music_song)
        my_music_list.append((start_minute, end_minute, music_name, music_song))
    for my_music in my_music_list:
        start_minute, end_minute, music_name, music_song = my_music
        if m in (music_song * (len(m) // len(music_song) + 2))[:(end_minute - start_minute)]:
            if answer == "" or current_time < end_minute - start_minute:
                current_time = end_minute - start_minute
                answer = music_name
    if answer == "":
        answer = "(None)"

    return answer


m_list = [
    "AC",
    "ABCDEFG",
    "CC#BCC#BCC#BCC#B",
    "ABC"
]
musicinfos_list = [
    ["12:00,12:14,HELLO,A", "13:00,13:05,WORLD,B"],
    ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"],
    ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"],
    ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]

]
return_list = [
    "HELLO",
    "HELLO",
    "FOO",
    "WORLD"
]
for _input_data in zip(m_list, musicinfos_list, return_list):
    _0, _1 = _input_data[:-1]
    _r = _input_data[-1]
    print(m_list.index(_0))
    result = solution(_0, _1)
    print(result)
    print(_r)
    if result == _r:
        print("맞음")
    else:
        print("틀림")
