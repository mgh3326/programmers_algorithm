def solution(data, col, row_begin, row_end):
    answer = -1
    sorted_data = sorted(data, key=lambda x: (x[col - 1], -x[0]))
    for i in range(row_begin - 1, row_end):
        _sum = 0
        for v in sorted_data[i]:
            _sum += v % (i + 1)
        if answer == -1:
            answer = _sum
        else:
            answer ^= _sum
    return answer
