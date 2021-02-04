def solution(citations):
    answer = 0
    for i in range(max(citations)+1):
        stack = 0
        for ele in citations:
            if ele >= i:
                stack += 1
        #print(i, stack, answer)
        if stack >= i:
            answer = max(i, answer)
    return answer
