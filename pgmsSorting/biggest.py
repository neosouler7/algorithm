"""
출처: 프로그래머스 > 정렬 > 가장 큰 수
내용: -
메모: 중요한건 착안 아이디어다... 문제 조건사항까지 잘 읽을 것
"""

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)  # 최대 1000 이므로, 3자리를 맞추어 비교한다
    return str(int(''.join(numbers)))


numbers = [3, 30, 34, 5, 9]
print(solution(numbers))