def solution(wallpaper):
    file_positions = [[i, j] for i, row in enumerate(wallpaper) for j, char in enumerate(row) if char == "#"]
    first_elements, second_elements = zip(*file_positions)
    return [min(first_elements), min(second_elements), max(first_elements) + 1, max(second_elements) + 1]
