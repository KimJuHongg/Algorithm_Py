def solution(nums):
    answer = 0
    s_nums = len(nums) / 2
    
    if s_nums < len(set(nums)):
        answer = s_nums
    elif s_nums >= len(set(nums)):
        answer = len(set(nums))
    return answer
