def solution(answers):
    answer = []
    len_anw = len(answers)
    one = [1, 2, 3, 4, 5] * (int(len_anw / 5) + 1)
    two = [2, 1, 2, 3, 2, 4, 2, 5] * (int(len_anw / 8) + 1)
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (int(len_anw / 10) + 1)
    score = {'1': 0, '2': 0, '3': 0}
    print(answers, three, len(answers))
    for i in range(0, len(answers)):
        if answers[i] == one[i]:
            score['1'] += 1
        if answers[i] == two[i]:
            score['2'] += 1
        if answers[i] == three[i]:
            score['3'] += 1


    tmp = sorted(score.items(), key=lambda x: x[1], reverse=True)
    print(tmp)

    answer += [int(tmp[0][0])]
    if tmp[0][1] == tmp[1][1]:
        answer += [int(tmp[1][0])]
    if tmp[0][1] == tmp[2][1]:
        answer += [int(tmp[2][0])]

    return answer
print(solution([1,3,2,4,2]))