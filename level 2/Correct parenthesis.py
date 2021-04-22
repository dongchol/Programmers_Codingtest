def check(s_lst):
    s_tmp_lst = s_lst[:]
    tmp = ''
    k = 0
    for idx, i in enumerate(s_lst):
        if ((idx + k) < len(s_lst)) and ((idx - 1 - k) >= 0):
            while str(s_tmp_lst[idx-1-k]) + str(s_tmp_lst[idx+k]) == '()':
                s_tmp_lst[idx+k] = True
                s_tmp_lst[idx-1-k] = True
                k += 1
                if ((idx + k) < len(s_lst)) and ((idx - 1 - k) >= 0):
                    continue
                else: break
            k = 0
            print(s_tmp_lst)
    return s_tmp_lst
def wrong_solution1(s):
    s_lst = list(s)
    s_tmp_lst = check(s_lst)
    print('gh')
    print(s_tmp_lst )
    if True in s_tmp_lst: return True
    return False


def solution2(s):
    queue = []
    for i in s:
        if i == '(':
            queue.append(i)
        elif i == ')':
            if len(queue) == 0: return False
            queue.pop()

    if len(queue) != 0: return False
    return True
print(solution("))(()())()))(("))