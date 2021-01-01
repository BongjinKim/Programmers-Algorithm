def convert_s(n, s):
    arr_124 = ['1','2','4']
    q, r = divmod(n, s)
    if q == 0:
        return arr_124[r]
    return '{}{}'.format(convert_s(q-1, s), arr_124[r])

def solution(n):
    answer = convert_s(n-1, 3)
    return answer
