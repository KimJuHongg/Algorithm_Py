def solution(x):
    answer = True
    a = list(map(int, str(x)))
    add = sum(a)
    if x % add == 0:
        return answer
    else :
        return False
