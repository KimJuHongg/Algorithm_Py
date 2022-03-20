def solution(n, arr1, arr2):
    answer = [] 
    
    for i in range(n):
        arr1[i]=format(arr1[i],'b')     
        arr2[i]=format(arr2[i],'b')
        
        while len(arr1[i])<n or len(arr2[i])<n :
            if len(arr1[i])<n:
                arr1[i] ='0'+arr1[i]
                
            if len(arr2[i])<n:
                arr2[i] ='0'+arr2[i]
            
    for i in range(n):
        tmp=''
        for j in range(n):
            if arr1[i][j]=='1' or arr2[i][j]=='1':
                tmp +='#'
            else :
                tmp +=' '
        answer.append(tmp) 
    
    return answer
