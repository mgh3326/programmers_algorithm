def solution(id_list, report, k):
    result_hash = {}
    reported_hash = {}
    send_hash = {}

    for _id in id_list:
        result_hash[_id] = 0
        reported_hash[_id] = set()
        send_hash[_id] = set()

    for r in report:
        reporter, reported = r.split(" ")

        reported_hash[reported].add(reporter)
        if len(reported_hash[reported]) >= k:
            for _reporter in reported_hash[reported]:
                if reported in send_hash[_reporter]:
                    continue
                result_hash[_reporter] += 1
                send_hash[_reporter].add(reported)
    answer = []
    for value in send_hash.values():
        answer.append(len(value))
    return answer


def test_solution1():
    assert solution(["muzi", "frodo", "apeach", "neo"],
                    ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2) == [2, 1, 1, 0]


def test_solution2():
    assert solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3) == [0, 0]
