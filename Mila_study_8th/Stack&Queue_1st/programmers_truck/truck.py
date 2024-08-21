def solution(bridge_length, weight, truck_weights):
    from collections import deque

    seconds = 0
    on_bridge = deque([0] * bridge_length)
    on_bridge_cnt = 0
    on_bridge_weight = 0
    # ---
    while on_bridge:  # 다리에 건너야 할 트럭이 모두 없을 때 까지
        # 건너고 나서 on_bridge에서 빠져야 한다.
        on_bridge_weight -= (
            on_bridge.popleft()
        )  # 지금 지나가는 차량이 없을 경우 -0이라 문제가 되지 않는다.
        seconds += 1  # 시간은 흐른다

        if truck_weights:  # 건너야 할 트럭이 남은 경우
            if (
                on_bridge_weight + truck_weights[0] <= weight
            ):  # 수용 차량수, 수용 하중을 초과하지 않는다면
                truck = truck_weights.pop(0)  # 차고지에서 앞 트럭 출발
                on_bridge.append(truck)  # 차량 다리 진입
                on_bridge_cnt += 1  # 차량 한대
                on_bridge_weight += truck  # 차량 무게 추가

            else:  # 수용 차량수, 수용 하중을 초과한다 > 진입 불가
                on_bridge.append(0)  #  유령 하나 진출
        # print(f"seconds : {seconds}, truck : {truck}, on_bridge : {on_bridge}, on_bridge_cnt : {on_bridge_cnt}, on_bridge_weight : {on_bridge_weight}")
    return seconds


bridge_length, weight, truck_weights = 2, 10, [7, 4, 5, 6]
print(solution(bridge_length=bridge_length, weight=weight, truck_weights=truck_weights))
