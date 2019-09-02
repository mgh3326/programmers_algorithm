def solution(citations):
    answer = 0
    l = sorted(citations, reverse=True)
    idx = 0
    current_result = l[idx]
    while True:
        if current_result ==-1:
            break

        count = l.count(current_result)
        idx += count

        if current_result <= idx:

            if current_result >= len(citations) - idx + count:
                return current_result

        current_result -= 1
    #
    # for idx, citation in enumerate(l):
    #     if idx != len(citations) - 1 and citation == l[idx + 1]:
    #         continue
    #     count = citations.count(citation)
    #     if citation <= idx + 1:
    #
    #         if citation >= len(citations) - idx - 1 + (count):
    #             return citation

    return answer


print(
    solution(
        [22, 42])
)
# 3
