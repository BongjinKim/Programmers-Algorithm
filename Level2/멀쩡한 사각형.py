def gcd(a, b):
    #유클리드 호재법 a, b의 최대공약수는 b, a%b 의 최대공약수와 같음
    return gcd(b, a%b) if a%b else b

def solution(w,h):
    answer = 1
    #입출력의 예제에서 본 것 처럼 8*12 직사각형을 자르면 2*3 자른 것이 4개가 나온다. 즉, 최대공약수를 구해서 푸는 문제
    #잘랐을 때, 사용할 수 없는 종이의 양은 a,b가 서로소일때, 최단거리 블럭개수와 같다. 즉, a+b-1 블럭만큼 잘린다.
    g = gcd(w, h)
    s_w = w // g
    s_h = h // g
    cutted_papers = (s_w+s_h-1) * g
    #print(cutted_papers)
    answer = w*h - cutted_papers
    return answer
