#딕셔너리 사용법 학습
def solution(clothes):
    answer = 1
    dic = {}
    arr = []

    for clothe, kind in clothes:
        if kind in dic:
            dic[kind].append(clothe)
        else:
            dic[kind] = [clothe]

    for ele in dic.values():
        answer *= len(ele)+1
    return answer - 1 #하나도 안 입은 경우 제외
