def solution(s):
    answer = ''
    s_lst = s.split(' ')
    s_num_lst = []
    for i in range(0, len(s_lst)):
        s_num_lst += [int(s_lst[i])]
    answer += str(min(s_num_lst)) +' '+ str(max(s_num_lst))
    return answer