def solution(places):
    answer = []
    for place in places:
        # O 상하좌우에 P가 있으면 0
        # P 와 P가 붙어있으면 0
        p_set = set()
        for h, place_str in enumerate(place):
            for w, str in enumerate(place_str):
                if str == "P":
                    p_set.add((h, w))
        is_end = False
        for h, place_str in enumerate(place):
            for w, str in enumerate(place_str):
                if str == "P":
                    if len({(h - 1, w), (h + 1, w), (h, w - 1), (h, w + 1)} & p_set) > 0:
                        is_end = True
                        break
                if str == "O":
                    if len({(h - 1, w), (h + 1, w), (h, w - 1), (h, w + 1)} & p_set) > 1:
                        is_end = True
                        break
            if is_end:
                answer.append(0)
                break
        else:
            answer.append(1)
    return answer
