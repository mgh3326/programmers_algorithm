answer = 0


def solution(begin, target, words):
    def dfs(current_str, depth):
        global answer
        if current_str == target:
            if answer == 0 or depth < answer:
                answer = depth
                return
        for idx, word in enumerate(words):
            if status_list[idx] == False:
                continue
            count = 0
            for begin_idx, begin_value in enumerate(current_str):
                if begin_value == word[begin_idx]:
                    count += 1
            if count == len(current_str) - 1:
                status_list[idx] = False
                dfs(word, depth + 1)
                status_list[idx] = True

                # temp_list.append(word)

    if words.count(target) == 0:
        return 0
    status_list = [True] * len(words)
    dfs(begin, 0)

    return answer


print(
    solution(
        "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
    )
)
# 4

print(
    solution(
        "hit", "cog", ["hot", "dot", "dog", "lot", "log"]
    )
)
# 0
