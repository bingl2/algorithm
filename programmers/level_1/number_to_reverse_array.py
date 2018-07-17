"""
문제 설명
자연수 num을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 num이 12345이면 [5,4,3,2,1]을 리턴합니다.

제한 조건
n은 10,000,000,000이하인 자연수입니다.
입출력 예
num	     return
12345	[5,4,3,2,1]
"""


def solution(num):
    answer = []

    # reversed 를 활용하여 먼저 뒤집어 주도록 리팩토링 진행.
    for str_num in reversed(str(num)):
        # 그래도 아직 문자열 형태이기 때문에 int 형으로 바꿔준다.
        answer.append(int(str_num))

    return answer
