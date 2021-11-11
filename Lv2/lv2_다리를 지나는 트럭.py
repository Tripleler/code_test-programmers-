def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    ton = 0
    while len(truck_weights) > 0:
        ton -= bridge.pop(0)
        if (ton + truck_weights[0]) <= weight:
            n = truck_weights.pop(0)
            ton += n
            bridge.append(n)
        else:
            bridge.append(0)
        answer += 1
    answer += bridge_length
    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
