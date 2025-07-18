from itertools import permutations


def solution(k, dungeons):
    answer = 0
    for dungeon_indexes in permutations(range(len(dungeons)), len(dungeons)):
        current_k = k
        count = 0
        for dungeon_index in dungeon_indexes:
            min_k, consumed_k = dungeons[dungeon_index]
            if current_k >= min_k:
                current_k -= consumed_k
                count += 1
        answer = max(answer, count)

    return answer
