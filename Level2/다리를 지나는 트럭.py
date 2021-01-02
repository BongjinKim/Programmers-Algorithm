def solution(bridge_length, weight, truck_weights):
    answer = 1
    arr_going = [[truck_weights.pop(0),1]]
    #arr_going: , 1초에 한번씩 arr_going을 업데이트 해줌
    while len(arr_going):
        answer += 1
        arr_going = [[weight,time+1] for weight, time in arr_going if time+1<=bridge_length]
        if len(truck_weights) !=0 and weight >= truck_weights[0] + sum([ele[0] for ele in arr_going]):
            arr_going.append([truck_weights.pop(0), 1])
    #print(answer, arr_going, truck_weights)
    return answer
