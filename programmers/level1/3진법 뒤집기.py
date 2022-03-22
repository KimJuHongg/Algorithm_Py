def solution(n):
    arr = []
    answer = 0
    while True:
        a = n // 3
        b = n % 3
        arr.append(b)
        if a == 0:
            break
        n = a
    num = ''
    for i in arr:
        num += str(i)
    answer = int(num,3)
    return answer
