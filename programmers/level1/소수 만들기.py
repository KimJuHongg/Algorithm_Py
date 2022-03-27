import itertools

def solution(nums):
    answer = 0
    c_nums = list(itertools.combinations(nums,3))     
    for i in range(len(c_nums)):
        s_nums = sum(c_nums[i])
        for j in range(2,s_nums):
            if s_nums % j == 0:
                break
        else :
            answer += 1

    return answer
