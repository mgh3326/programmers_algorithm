def solution(n):
    arr = []
    for i in range(n):
        arr.append([0] * (i + 1))

    def triangle(h, w, triangle_size, current_num):
        if triangle_size == 1:
            arr[h][w] = current_num
            return
        for i in range(triangle_size):
            arr[h + i][w] = current_num
            current_num += 1
        for i in range(triangle_size - 1):
            arr[h + triangle_size - 1][w + i + 1] = current_num
            current_num += 1
        for i in range(triangle_size - 2):
            arr[h + triangle_size - 1 - (i + 1)][w + triangle_size - 1 - (i + 1)] = current_num
            current_num += 1
        if triangle_size - 3 >= 1:
            triangle(h + 2, w + 1, triangle_size - 3, current_num)

    triangle(0, 0, n, 1)
    answer = []
    for i in range(n):
        for v in arr[i]:
            answer.append(v)
    return answer
