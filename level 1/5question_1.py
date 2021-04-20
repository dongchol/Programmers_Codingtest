#제일 작은 수 제거하기
def solution1(arr):
    if arr == [10]:
        return [-1]
    arr.remove(min(arr))    #remove(값), pop(인덱스)로 리스트 내 요소 제거
    return arr

#정수 내림차순으로 배치하기
def solution2(n):
    answer = ''
    list_n = list(str(n))
    list_n.sort(reverse=True)
    for i in range(0, len(list_n)): #int("".join(ls))으로 대체 가능
        answer += list_n[i]
    return int(answer)

#이상한 문자 만들기
def solution3(s):
    answer = []
    tmp = ''
    s_list = s.split(' ')
    for i in range(0, len(s_list)):
        for j in range(0, len(s_list[i])):
            if j % 2 == 0:
                tmp += str(s_list[i][j].upper())
            else: tmp += str(s_list[i][j].lower())
        answer += [tmp]
        tmp = ''
    answer = ' '.join(answer)
    return answer

#change_str2int
def solution4(s):
    answer = int(s)
    return answer

#수박수
def solution5(n):
    answer = ''
    for i in range(1, n+1):
        if i % 2 == 0:
            answer += '박'
        else: answer += '수'
    return answer