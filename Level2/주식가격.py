def solution(prices):
    answer = [0 for _ in prices]
    stack = []
    for idx, val in enumerate(prices):
        if len(stack) == 0:
            stack.append((idx, val))
            continue
        #temp > val stack 채우기
        top = stack[-1][1]
        if top <= val:
            stack.append((idx, val))
        else: #temp < val
            while len(stack) and stack[-1][1] > val:
                temp = stack.pop()
                #print(temp)
                answer[temp[0]] = idx - temp[0]
            stack.append((idx, val))

        #print(stack)
    for i, v in stack:
        answer[i] = len(prices) - i - 1
    return answer
