def solution(s, n):
    alpabet_l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    answer = ''
    for i in range(0, len(s)):
        if s[i] == ' ':
                answer += ' '
        else:
            for j in range(0, len(alpabet_l)):
                if s[i].lower() == alpabet_l[j]:
                    if s[i].islower() == True:
                        answer += alpabet_l[(j+n)%(len(alpabet_l))]
                    else: answer += alpabet_l[((j+n)%len(alpabet_l))].upper()
    return answer