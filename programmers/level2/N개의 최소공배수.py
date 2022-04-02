def solution(arr):
    answer = 0
    l_arr = []
    arr = sorted(arr)
    for i in range(1,len(arr)):
        a = arr[i-1]
        b = arr[i]
        for j in range(b, a*b+1, 1):
            if j % a == 0 and j % b == 0:
                answer = j
                arr[i] = answer
                l_arr.append(answer)
                break
    return max(l_arr)
