#permutation 구현해보기, 내장함수 사용하면 빠르게 풀 수 있을듯
def permutation(numbers, n):
    def generate(chosen, remain):
        if len(chosen) == n:
            answer.append(int(''.join(chosen)))
            return

        for i in range(len(numbers)):
            chosen.append(remain[i])
            temp = remain.pop(i)
            generate(chosen, remain)
            remain.insert(i, temp)
            chosen.pop()
    generate([], numbers)

def solution(numbers):
    global answer
    answer = []
    max_num = 10000001
    arr_prime = [1 for _ in range(max_num)]
    arr_prime[0] = 0
    arr_prime[1] = 0
    for i in range(2, int(max_num**0.5)+1):
        for j in range(i+i, max_num, i):
            if arr_prime[j]:
                arr_prime[j] = 0
    #숫자를 만들수 있는 전부를 구하면 7P7++...+7P1까지이므로 시간 충분
    arr_numbers = [s for s in numbers]
    for i in range(1, len(numbers)+1):
        permutation(arr_numbers, i)
    #같은 것은 set으로 제거 후 개수 구하기
    a = set(answer)
    return len([i for i in a if arr_prime[i]])
