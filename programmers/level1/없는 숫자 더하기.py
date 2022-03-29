def solution(numbers):
    answer = 0
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers = sorted(numbers)
    
    for i in range(0,10,1):
        for j in range(len(numbers)):
            if numbers[j] == i:
                arr.remove(i)
    
    for i in range(len(arr)):
        answer += arr[i]
            
    return answer
