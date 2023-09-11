def compress(arr):
    if len(arr) == 1:
        return arr[0][0]
    else:
        zero_count = 0
        one_count = 0
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == 0:
                    zero_count += 1
                else:
                    one_count += 1
        if zero_count == 0:
            return [1]
        if one_count == 0:
            return [0]
        half_length = len(arr) // 2
        result_arr = []
        temp_arr = []
        for i in range(half_length):
            width_temp_arr = []
            for j in range(half_length):
                width_temp_arr.append(arr[i][j])
            temp_arr.append(width_temp_arr)
        result_arr.append(compress(temp_arr))
        temp_arr = []
        for i in range(half_length, half_length * 2):
            width_temp_arr = []
            for j in range(half_length):
                width_temp_arr.append(arr[i][j])
            temp_arr.append(width_temp_arr)
        result_arr.append(compress(temp_arr))
        temp_arr = []
        for i in range(half_length):
            width_temp_arr = []
            for j in range(half_length, half_length * 2):
                width_temp_arr.append(arr[i][j])
            temp_arr.append(width_temp_arr)
        result_arr.append(compress(temp_arr))
        temp_arr = []
        for i in range(half_length, half_length * 2):
            width_temp_arr = []
            for j in range(half_length, half_length * 2):
                width_temp_arr.append(arr[i][j])
            temp_arr.append(width_temp_arr)
        result_arr.append(compress(temp_arr))
        return result_arr


def count_elements(lst, element=0):
    count = 0
    for i in lst:
        if type(i) is list:
            count += count_elements(i, element)
        elif i == element:
            count += 1
    return count


def solution(arr):
    compressed_arr = compress(arr)
    zero_count = count_elements(compressed_arr, 0)
    one_count = count_elements(compressed_arr, 1)
    return [zero_count, one_count]
