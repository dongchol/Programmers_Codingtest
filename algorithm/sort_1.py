def solution(array, commands):
    answer = []
    tmp = []
    for i in range(0, len(commands)):
        tmp += array[commands[i][0]-1:commands[i][1]]
        tmp.sort()
        answer += [tmp[commands[i][2]-1]]
        tmp = []
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))