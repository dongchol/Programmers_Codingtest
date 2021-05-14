def solution1(arr):
    answer = 0
    sum = 0
    for i in arr:
        sum += i
    answer = sum/len(arr)
    return answer


## solution2
a, b = map(int, input().strip().split(' '))

for i in range(0, b):
    for i in range(0, a):
        print('*', end = '')
    print()