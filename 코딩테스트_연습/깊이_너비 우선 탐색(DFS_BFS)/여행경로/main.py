answer = []


def solution(tickets):
    def dfs(ticket_index, depth):
        global answer
        if len(temp_list) == len(tickets) +1:
            if len(answer) == 0:
                answer = temp_list.copy()
            else:
                join = ''.join(temp_list)
                join2 = ''.join(answer)
                if join < join2:
                    answer = temp_list.copy()

            return
        current_ticket_start, current_ticket_end = tickets[ticket_index]
        for idx, ticket in enumerate(tickets):
            if status_list[idx] == False:
                continue
            if current_ticket_end == ticket[0]:  # 출발 도착 같을 경우
                status_list[idx] = False
                temp_list.append(ticket[1])
                dfs(idx, depth + 1)
                status_list[idx] = True
                temp_list.pop()

    # ticket_set = set()
    # for ticket in tickets:
    #     ticket_set.add(ticket[0])
    #     ticket_set.add(ticket[1])
    # l = sorted(ticket_set)
    # index_list = []  # 인덱스로 바꿔서 하는게 이득일까 별로 이득이 없을것 같다.
    answer.clear()
    status_list = [True] * len(tickets)
    temp_list = []
    for i in range(len(tickets)):
        if tickets[i][0]=="ICN":
            status_list[i] = False
            temp_list.append(tickets[i][0])
            temp_list.append(tickets[i][1])
            dfs(i, 0)
            status_list[i] = True
            temp_list = []
    return answer


print(
    solution(
        [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    )
)
print(
    solution(
        [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    )
)
# [ICN, ATL, ICN, SFO, ATL, SFO]
