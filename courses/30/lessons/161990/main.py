def solution(wallpaper):
    file_positions = []
    for i in range(len(wallpaper)):
        string = wallpaper[i]
        for j in range(len(string)):
            char = string[j]
            if char == "#":
                file_positions.append([i, j])
    first_elements = [x[0] for x in file_positions]
    second_elements = [x[1] for x in file_positions]
    min_h = min(first_elements)
    max_h = max(first_elements)
    min_w = min(second_elements)
    max_w = max(second_elements)
    return [min_h, min_w, max_h + 1, max_w + 1]
