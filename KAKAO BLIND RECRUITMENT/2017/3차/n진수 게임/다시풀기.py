def solution(n, t, m, p):
    answer = ''
    num = 0
    m_index = 0
    p_index = 0
    while True:
        if m_index == t:
            break
        output = make_demical(n, num)
        for i in output:
            if p_index == p - 1:
                m_index += 1
                answer += i
                if m_index == t:
                    break

            p_index += 1
            p_index %= m
        num += 1

    return answer


def make_demical(n, num):
    output = ""
    if num == 0:
        return "0"
    while True:
        if num == 0:
            break
        result = num % n
        if result == 10:
            result = "A"
        elif result == 11:
            result = "B"
        elif result == 12:
            result = "C"
        elif result == 13:
            result = "D"
        elif result == 14:
            result = "E"
        elif result == 15:
            result = "F"
        output = str(result) + output
        num = num // n
    return output


print(
    solution(
        2, 4
        , 2
        , 1
    )
)
# 0111
