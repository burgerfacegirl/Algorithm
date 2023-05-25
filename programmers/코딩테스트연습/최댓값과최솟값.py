def solution(s):
    nums = [ int(i) for i in s.split(" ") ]
    answer = ''
    answer += str(min(nums)) + ' ' + str(max(nums))
    return answer