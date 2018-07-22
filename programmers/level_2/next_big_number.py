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


def binary_number_one_count(number):
    one_count = 0
    while number > 0:
        number, remainder = divmod(number, 2)

        if remainder == 1:
            one_count += 1

    return one_count


def solution(n):
    answer = n

    # 일단 들어온 n 이라는 숫자를 2진수로 바꾸는 기능을 구현하자. 정답의 n은 굳이 리스트로 만들 필요 없이 1이 찍히는 것들을 세면 될것 같다.
    one_count = binary_number_one_count(answer)

    # 이제 n 보다 큰 수들을 하나씩 2진수로 바꿔나가며 1의 개수를 확인해보자.
    is_find = False

    # 혹시 n 보다 큰 수들 중에서 1의 개수가 같을 수 있는 상황들이 공톰점이 있을 수 있는지 확인 해보자.
    while not is_find:
        answer += 1

        find_one_count = binary_number_one_count(answer)

        # 1의 갯수가 같은 n 보다 큰수가 나오면 거기서 멈추고 answer 로 돌려준다.
        if one_count == find_one_count:
            is_find = True

    return answer


# assert solution(6) == 83
assert solution(78) == 83, solution(78)
assert solution(15) == 23
