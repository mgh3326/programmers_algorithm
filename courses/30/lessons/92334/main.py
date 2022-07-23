def solution(id_list, report, k):
    reported_hash = {}
    result_hash = {}

    for _id in id_list:
        reported_hash[_id] = set()
        result_hash[_id] = 0

    for r in report:
        reporter, reported = r.split(" ")
        reported_hash[reported].add(reporter)

    for reported_hash_key in reported_hash.keys():
        reported_hash_value = reported_hash[reported_hash_key]
        if len(reported_hash_value) >= k:
            for _id in reported_hash_value:
                result_hash[_id] += 1
    return list(result_hash.values())


def test_solution1():
    assert solution(["muzi", "frodo", "apeach", "neo"],
                    ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2) == [2, 1, 1, 0]


def test_solution2():
    assert solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3) == [0, 0]

# https://school.programmers.co.kr/learn/courses/30/lessons/92334?language=python3
# 유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.
# 위 내용을 관과하여 오래 걸렸다.
