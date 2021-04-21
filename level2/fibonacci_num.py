def fibo(n):
    if n == 0: return 0
    elif n == 1: return 1
    return (fibo(n-1) + fibo(n-2)) #%1234567

def solution1(n):
    answer = 0
    answer = fibo(n) #%1234567
    return answer

def solution2(n):
    Table = [0 for c in range(n+1)]
    Table[1] = 1
    print(Table)
    for i in range(2, n+1):
        Table[i] = (Table[i-1] + Table[i-2]) % 1234567

    return Table[i]
print(solution2(10))