# 1. 효율성 검사 미달
def solution(n):
    div_list = []
    div = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            if i % j == 0:
                div += 1
        if div == 2:
            div_list += [i]
        div = 0
    answer = len(div_list)
    return answer

# 2. 에라토스테네스의 체 이용
def solution(n):
    sqrt_ = int(n ** 0.5)
    s = [True] * (n + 1)

    for i in range(2, sqrt_ + 1):
        if s[i] == True:
            for j in range(i * 2, n + 1, i):
                s[j] = False

    answer = len([i for i in range(2, n + 1) if s[i] == True])
    return answer

print(solution2(5))
