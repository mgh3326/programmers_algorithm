def solution(n, wires):
    answer = n - 1
    for i in range(len(wires)):
        _hash = {}
        for j in range(len(wires)):
            if i != j:
                v1, v2 = wires[j]
                if v1 not in _hash:
                    _hash[v1] = []
                _hash[v1].append(v2)
                if v2 not in _hash:
                    _hash[v2] = []
                _hash[v2].append(v1)
        _set = {1}
        _queue = [1]
        while True:
            if len(_queue) == 0:
                break
            v = _queue.pop()
            if v in _hash:
                w_list = _hash[v]
                for w in w_list:
                    if w not in _set:
                        _set.add(w)
                        _queue.append(w)
        answer = min(answer, abs(n - len(_set) - len(_set)))
    return answer
