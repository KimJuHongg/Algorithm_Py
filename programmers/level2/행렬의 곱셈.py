def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append([])
        
        for j in range(len(arr2[0])):
            sum = 0
            
            for k in range(len(arr1[i])):
                sum += arr1[i][k] * arr2[k][j]
                
            answer[i].append(sum)
    return answer
