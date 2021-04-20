#약수의 합
def solution1(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    return answer

#평균 구하기
def solution2(arr):
    answer = 0
    for i in range(0, len(arr)):
        answer += arr[i]
    answer /= len(arr)
    return answer

#짝수와 홀수
def solution3(num):
    answer = ''
    if num % 2 == 0:
        answer = 'Even'
    else: answer = "Odd"
    return answer

#핸드폰 번호 가리기
def solution4(phone_number):
    answer = ''
    for i in range(0, len(phone_number)-4):
        answer += '*'
    answer += phone_number[len(phone_number)-4:]
    return answer

#하샤드 수
def solution5(x):
    str_x = str(x)
    sum = 0
    for i in range(0, len(str_x)):
        sum += int(str_x[i])
    if x % sum == 0:
        return True
    else: return False


#콜라츠 추측
def solution6(num):
    answer = 0
    if num == 1: return 0
    for i in range(0, 500):
        if num % 2 == 0:
            num /= 2
            if num == 1:
                return i+1
        elif num %2 != 0:
            num = num*3 + 1
            if num == 1:
                return i+1
    return -1

#최대 공약수와 최소 공배수
def solution7(n, m):
    answer = []
    if m<n:
        tmp = m
        m = n
        n = tmp
    for i in range(1, n+1):
        if (n % i == 0) and (m % i == 0):
            answer += [i]
            answer += [n/i*m/i*i]
    return answer[len(answer)-2:]


#자릿수 더하기
def solution8(n):
    answer = 0
    str_n = str(n)
    for i in range(0, len(str_n)):
        answer += int(str_n[i])
    return answer

#정수 제곱근 판별
def solution9(n):
    answer = 0
    if n % (n ** 0.5) == 0:
        return (n**0.5+1)**2
    else: return -1

#자연수 뒤집어 배열로 만들기
def solution10(n):
    answer = list(str(n))
    tmp = [0]* len(answer)
    for i in range(0, len(answer)):
        tmp[len(answer)-i-1] = int(answer[i])

    return tmp