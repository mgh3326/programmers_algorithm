def solution(rows, columns, queries):
    answer = []
    matrix = {}
    count = 1
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            matrix[(i, j)] = count
            count += 1
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    corners = [
        [0, 3],
        [2, 3],
        [2, 1],
        [0, 1],
    ]
    for query in queries:
        min_value = rows * columns
        new_matrix = matrix.copy()
        current_h, current_w = query[0], query[1]
        for direction, corner in zip(directions, corners):
            direction_h, direction_w = direction
            corner_h, corner_w = corner
            destination_h = query[corner_h]
            destination_w = query[corner_w]
            while True:
                previous_h = current_h
                previous_w = current_w
                current_h = current_h + direction_h
                current_w = current_w + direction_w
                new_matrix[(current_h, current_w)] = matrix[(previous_h, previous_w)]
                min_value = min(min_value, matrix[(previous_h, previous_w)])
                if current_h == destination_h and current_w == destination_w:
                    break
        matrix = new_matrix
        answer.append(min_value)
    return answer
