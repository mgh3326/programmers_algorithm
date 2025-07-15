import heapq


def solution(k, score):
    answer = []
    heap = []
    for x in score:
        if len(heap) >= k:
            if heap[0] < x:
                heapq.heapreplace(heap, x)
        else:
            heapq.heappush(heap, x)
        answer.append(heap[0])
    return answer
