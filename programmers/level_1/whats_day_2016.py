"""
2016년 1월 1일은 금요일입니다.

2016년 a월 b일은 무슨 요일일까요? 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.
요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT
"""


def solution(month, day):
    answer = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]

    # 1월과 1일을 기준으로 시작하기 때문에 0으로 생각하여 내려가면서 더할 월(month)와 전체 일수(total_day)의 총합에서 1씩 빼면서 시작
    month = month - 1
    # 1월 보다 작을 경우 루프를 돌 필요가 없기 때문에 total_day 에 바로 day 값을 넣어서 계산함. 하지만 1월 1일이 기준이기 때문에 -1 진행.
    total_day = day - 1

    # month 를 내려가며 전체 일수를 더하는 루프
    while month > 0:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            total_day += 31
        elif month in [4, 6, 9, 11]:
            total_day += 30
        elif month == 2:
            # 2016 년은 윤년이기 때문에 문제상 29일로 고정. 년도 까지 있을 경우 year % 4 == 0 을 통해 해결하면 될것 같다.
            total_day += 29
        month -= 1

    # 1월 1일을 기준으로 나머지에서 증가된 수 만큼이 앞선 요일.
    index = total_day % 7

    return answer[index]


print(solution(1, 1)) # FRI
print(solution(1, 8)) # FRI
print(solution(2, 29)) # MON
print(solution(12, 31)) # SAT
