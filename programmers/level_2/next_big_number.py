"""
자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.

제한 사항
n은 1,000,000 이하의 자연수 입니다.

입출력 예
n	result
78	83
15	23

입출력 예 설명
입출력 예#1
문제 예시와 같습니다.
입출력 예#2
15(1111)의 다음 큰 숫자는 23(10111)입니다.
"""


# 굳이 2진수 전체 배열을 알 필요가 없다고 판단이 들어, 1의 개수만 파악하도록 로직을 구성하였다.
def binary_number_one_count(number):
    # 변수 초기화
    one_count = 0

    while number > 0:
        # 간단하게 숫자르 2진수로 변환할 경우 나머지가 1일 경우 무조건 해당 자리를 1로 채우게 된다.
        number, remainder = divmod(number, 2)

        # 그래서 나머지가 1일 경우, 1카운트를 증가시킨다.
        if remainder == 1:
            one_count += 1

    # 반복문이 끝나고 나면 1을 센 갯수를 넣어준다.
    return one_count


def solution(number):
    # 숫자를 넣으면 2진수로 변환 후 1의 개수를 구해주는 함수 실행.
    one_count = binary_number_one_count(number)

    # 찾았는지를 확인해주는 변수 선언.
    is_find = False

    # 찾을 경우 루프를 끝낸다.
    while not is_find:
        # 숫자를 계속 더해가며 확인을 한다.
        number += 1

        # 2진수 변환 후 1 개수 찾기 진행.
        find_one_count = binary_number_one_count(number)

        # 찾을 경우 루프를 종료한다.
        if one_count == find_one_count:
            is_find = True

    # 증가된 값을 리천해준다.
    return number


# assert solution(6) == 83
assert solution(78) == 83, solution(78)
assert solution(15) == 23, solution(15)


"""
진수를 구하는 문제를 이미 앞에서 풀었다보니 생각보다 쉽게 풀 수 있었다.

1을 구하는 함수에, 최대 1 카운트 값을 넣을 경우에 1을 카운팅하다 한계 값을 넘어가면 다음 루프를 돌리는 것도 좋을 것 같다.
"""