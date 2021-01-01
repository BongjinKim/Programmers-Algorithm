def ceil(a, b):
    return a//b + 1 if a%b else a//b

def solution(progresses, speeds):
    answer = []
    prev = 0
    for p, s in zip(progresses, speeds):
        now = ceil(100-p, s)
        if prev >= now:
            answer[-1] += 1
        else:
            prev = now
            answer.append(1)

    return answer
