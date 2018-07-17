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

    # num 을 문자열로 바꾼 후 배열으 돌린다.
    for str_num in str(num):
        # 먼저 나온수가 뒤집어 져야하니 합칠 때 앞에 배열에 추가한다.
        answer = [int(str_num)] + answer

    return answer
