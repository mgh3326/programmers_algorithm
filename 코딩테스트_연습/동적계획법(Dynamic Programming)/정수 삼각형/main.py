def solution(triangle):
    for depth in range(len(triangle)):
        current_triangle = triangle[len(triangle) - 1 - depth]
        for triangle_idx, triangle_value in enumerate(current_triangle[:-1]):
            idx_ = max(triangle_value, current_triangle[triangle_idx + 1])
            triangle[len(triangle) - 2 - depth][triangle_idx] += idx_

    answer = triangle[0][0]
    return answer


print(
    solution(
        [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    )
)
