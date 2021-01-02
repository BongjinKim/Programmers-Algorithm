#1회차: 27분24초 // 설계 15분, 구현 12분 24초
def convert(w):
    if w == '':
        return ''
    stack = 0
    u = ''
    v = ''
    for i in range(len(w)):
        if w[i] == '(':
            stack += 1
        else:
            stack -= 1
        if stack == 0:
            u = w[:i+1]
            v = w[i+1:]
            break
    # print("u:", u)
    # print("v:", v)
    for c in u:
        if c == '(':
            stack += 1
        else:
            stack -= 1
        if stack < 0:
            return '(' + convert(v) + ')' + ''.join([')' if c=='(' else '(' for c in u[1:-1]])
    return u + convert(v)

def solution(p):
    answer = ''
    answer = convert(p)
    return answer
