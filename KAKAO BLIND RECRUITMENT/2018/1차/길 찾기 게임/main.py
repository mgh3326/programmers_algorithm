import sys

sys.setrecursionlimit(10 ** 6)
my_dict = {}
my_oh_dict = {}


def solution(nodeinfo: list):
    def dfs(depth, h, w):
        # if depth != 0:
        #     pass

        temp_list.append(my_oh_dict[h, w][0])
        if my_oh_dict[h, w][1]["left"] != -1:
            dfs(depth + 1, my_oh_dict[h, w][1]["left"][0], my_oh_dict[h, w][1]["left"][1])
        if my_oh_dict[h, w][1]["right"] != -1:
            dfs(depth + 1, my_oh_dict[h, w][1]["right"][0], my_oh_dict[h, w][1]["right"][1])

    def two_dfs(depth, h, w):
        # if depth != 0:
        #     pass

        if my_oh_dict[h, w][1]["left"] != -1:
            two_dfs(depth + 1, my_oh_dict[h, w][1]["left"][0], my_oh_dict[h, w][1]["left"][1])
        if my_oh_dict[h, w][1]["right"] != -1:
            two_dfs(depth + 1, my_oh_dict[h, w][1]["right"][0], my_oh_dict[h, w][1]["right"][1])
        temp_list.append(my_oh_dict[h, w][0])

    my_dict = {}
    my_oh_dict = {}
    node_dict = {"left": -1,
                 "right": -1}
    for idx, node in enumerate(nodeinfo):
        if node[1] not in my_dict:
            my_dict[node[1]] = []
        _copy = node_dict.copy()
        my_dict[node[1]].append((node[0], idx + 1, _copy))
        my_oh_dict[(node[1], node[0])] = (idx + 1, _copy)

    sorted_my_dict_keys = sorted(my_dict.keys(), reverse=True)
    for idx, my_dict_key in enumerate(sorted_my_dict_keys):
        my_dict_value = my_dict[my_dict_key]
        if idx == 0:
            pass
        else:
            for x_idx_value in my_dict_value:
                node_w = my_dict[sorted_my_dict_keys[0]][0][0]  # Top
                node_h = (sorted_my_dict_keys[0])
                while True:
                    current_node = my_oh_dict[node_h, node_w][1]
                    if x_idx_value[0] < node_w:  # left
                        if current_node["left"] == -1:
                            current_node["left"] = (my_dict_key, x_idx_value[0])
                            break
                        else:
                            node_h, node_w = current_node["left"]

                    else:  # right
                        if current_node["right"] == -1:
                            current_node["right"] = (my_dict_key, x_idx_value[0])
                            break
                        else:
                            node_h, node_w = current_node["right"]
    answer = []
    temp_list = []
    dfs(0, sorted_my_dict_keys[0], my_dict[sorted_my_dict_keys[0]][0][0])
    answer.append(temp_list.copy())
    temp_list = []
    two_dfs(0, sorted_my_dict_keys[0], my_dict[sorted_my_dict_keys[0]][0][0])
    answer.append(temp_list)

    return answer


nodeinfo_list = [
    [[1, 2], [2, 3], [3, 3]],
    [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]],

]
return_list = [
    [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]],
    [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]],

]
for _input_data in zip(nodeinfo_list, return_list):
    _0 = _input_data[0]
    _r = _input_data[-1]
    print(nodeinfo_list.index(_0))
    result = solution(_0)
    print(result)
    print(_r)
    if result == _r:
        print("맞음")
    else:
        print("틀림")
