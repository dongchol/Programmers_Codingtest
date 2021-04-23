def wrong_solution1(s):
    answer = ''
    s_lst = s.split(' ')
    for idx, i in enumerate(s_lst):
        if i[0].isalpha() == True:
            s_lst[idx] = s_lst[idx][0].upper() + s_lst[idx][1:].lower()
    answer = ' '.join(s_lst)
    return answer


def solution2(s):
    s = s.lower()
    L = s.split(" ")
    answer = ""
    for i in L:
        i= i.capitalize()
        answer += i+" "
    return answer[:-1]