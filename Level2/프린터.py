def solution(priorities, location):
    answer = []
    priorities = list(enumerate(priorities))
    #1 가장 앞에 있는 문서를 꺼냄
    while len(priorities):
        #print(priorities, answer)
        J = priorities[0]
        priorities = priorities[1:]
        flag = True
        for ele in priorities:
            #print(ele)
            #2 J보다 중요도가 높은 문서 있으면 대기열 마지막
            if ele[1] > J[1]:
                priorities.append(J)
                flag = False
                break
        if flag:
            answer.append(J)

    for i, ele in enumerate(answer):
        if ele[0] == location:
            return i+1
