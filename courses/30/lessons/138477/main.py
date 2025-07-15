import heapq


def solution(k, score):
    answer = []
    heap = []
    heap_min_score = score[0]
    heap_max_score = score[0]
    for x in score:
        if len(heap) >= k:
            if heap_min_score < x:
                heapq.heappop(heap)
                heapq.heappush(heap, x)
                # heapreplace가 동일한가?

                heap_min_score = heapq.heappop(heap)
                heapq.heappush(heap, heap_min_score)
                #넣다 빼는것 말고 제일 작은 값을 확인할수 있나?
        else:
            heapq.heappush(heap, x)
            if heap_min_score > x:
                heap_min_score = x
            elif heap_max_score < x:
                heap_max_score = x
        answer.append(heap_min_score)
    return answer
