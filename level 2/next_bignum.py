def solution(n):
    answer = 0
    k = 0
    index = []
    for idx, i in enumerate(str(bin(n)[2:])):
        if i == '1':
            k += 1
        else: index += [idx]
    if k == len(str(bin(n))[2:]):
        return n - 2**(len(str(bin(n))[2:])-1) + 2**(len(str(bin(n))[2:]))
    num = 1
    tmp = 0

    while tmp != k:
        tmp = 0
        for i in str(bin(n + num)[2:]):
            if i == '1':
                tmp += 1
        num += 1
    return n+num-1

def nextBigNumber(n):
    c = bin(n).count('1')   # 문자열에 count 함수
    for m in range(n+1,1000001):
        if bin(m).count('1') == c:
            return m

print(solution(6))