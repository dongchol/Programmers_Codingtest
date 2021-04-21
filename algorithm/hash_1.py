def solution(participant, completion):
    answer = ''
    hash = {}

    for name in completion:
        if name in hash:
            hash[name] += 1
        else:
            hash[name] = 1
    print(hash)
    for key in participant:
        if key in hash:
            hash[key] -= 1
            if hash[key] < 0:
                print(hash[key])
                answer = key
        else:
            answer = key
    print(hash)
    return answer

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))