from itertools import product
def n_power(n):
    a = 0
    for i in range(0, 10):
        if (3/2)*(3**i -1) >= n:
            a = i
            break
    return a, (3/2)*(3**a -1), (3/2)*(3**a -1)-3**a+1   #a, end, start

def solution1(n):   #효율성 문제
    lst = []
    k = 0
    n_digit, end, start = n_power(n)
    idx = int(n-start)
    print(n_digit, idx)
    a = ()
    for i in product([1, 2, 4], repeat=n_digit):
        #lst += [i]
        if k == idx:
            a = i#lst[idx]
            break
        k+=1
        #print(n)
    a_ = ''
    for i in range(0, len(a)):
        a_ += str(a[i])
    return a_

def solution2(n):
    num = ['1', '2', '4']
    answer = ""

    while n > 0:
        print(n, end=' ')
        n -= 1
        answer = num[n % 3] + answer
        print(answer)
        n //= 3
    return answer

print(solution(110))