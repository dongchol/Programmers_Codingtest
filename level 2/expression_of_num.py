def solution1(n):   # 효율성 문제
    answer = 0
    start, end = 1,2
    while start <= int(n/2):
        while end <= (int(n/2)+1):
            if (start+end)*(end-start+1)/2 == n:
                answer += 1
            end += 1
        start +=1
        end = 0
    return answer +1

def solution(n):
    answer = 1
    for i in range(1, n//2 + 1):
        cnt = 0
        for j in range(i, n+1):
            cnt += j
            if cnt == n:
                answer += 1
                break
            elif cnt > n: break
            else: continue
    return answer

def expressions(num):
    answer = 0
    for i in range(1, num + 1):
        s = 0
        while s < num:
            s += i
            i += 1
        if s == num:
            answer += 1


    return answer