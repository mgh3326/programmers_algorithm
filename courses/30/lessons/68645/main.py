def solution(n):
    arr = [[0] * (i + 1) for i in range(n)]

    def fill_triangle(h, w, triangle_size, current_num):
        if triangle_size < 1:
            return
        for i in range(triangle_size):  # Go downwards
            arr[h + i][w] = current_num
            current_num += 1
        for i in range(1, triangle_size):  # Go rightwards
            arr[h + triangle_size - 1][w + i] = current_num
            current_num += 1
        for i in range(1, triangle_size - 1):  # Go upwards
            arr[h + triangle_size - 1 - i][w + triangle_size - 1 - i] = current_num
            current_num += 1
        fill_triangle(h + 2, w + 1, triangle_size - 3, current_num)

    fill_triangle(0, 0, n, 1)
    answer = []
    for i in range(n):
        for v in arr[i]:
            answer.append(v)
    return answer
