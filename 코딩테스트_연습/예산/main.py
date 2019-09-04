def solution(budgets, M):
    budgets.sort()
    budgets_min = len(budgets)
    budgets_max = budgets[-1]
    answer = 0
    while True:
        average = (budgets_max + budgets_min) // 2
        ok_average = is_ok_average(M, budgets, average)
        if ok_average == 1:
            budgets_max = average
        elif ok_average == 2:
            if answer == average:
                return answer
            answer = average
            budgets_min = average
        else:
            return average


def is_ok_average(M, budgets, average):
    temp_sum = 0
    for budget_idx in range(len(budgets)):
        budget = budgets[budget_idx]
        if budget > average:
            temp_sum += (len(budgets) - budget_idx) * average
            break
        temp_sum += budget
        if temp_sum > M:
            return 1
    if temp_sum < M:
        return 2
    elif temp_sum > M:
        return 1
    else:
        return 0


print((solution(
    [120, 110, 140, 150], 485
)))
