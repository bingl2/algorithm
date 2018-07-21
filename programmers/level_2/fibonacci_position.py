"""
문제 설명
피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 점화식입니다.
2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

제한 사항
* n은 1이상, 100000이하인 자연수입니다.

입출력   예
n	   return
3	   2
5	   5

입출력 예 설명
피보나치수는 0번째부터 0, 1, 1, 2, 3, 5, ... 와 같이 이어집니다.
"""

from util.time_util import runtime


# 일단 피보나치 수를 보면 [(숫자)는 자리를 의미함].
# 0(0) + [1(1) = 1(2)]
# 1(1) + [1(2) = 2(3)]
# 1(2) + [2(3) = 3(4)]
# 2(3) + [3(4) = 5(5)]
# 간단하게 대괄호에 쌓인 숫자들이, 다음 수를 구할 때 사용되는 공통점을 발견할 수 있다.
@runtime
def first_solution(position):
    # 시작할 피노차리 수열 리스트를 만든다.
    fibo_list = [0, 1]

    # 위치의 수를 구하기 위해 돌기 시작한다.
    while len(fibo_list) <= position:
        # 끝에서 두 수를 더하여 리스트에 추가.
        fibo_list.append(fibo_list[-1] + fibo_list[-2])

    # 원하는 포지션의 수에서 (1234567) 로 나눈 나머지를 구한다.
    return fibo_list[position] % 1234567


assert first_solution(5000) == 1178031
assert first_solution(10000) == 1107030
assert first_solution(100000) == 1168141
assert first_solution(200000) == 672799


# 원하는 포지션 값에서 "1234567"을 나눈 나머지를 구해주면 되니 리스트를 빼고 작성.
@runtime
def second_solution(position):
    first, second = 0, 1

    # postion 수 만큼 돌면서 원하는 값을 뽑아낸다. 내가 맨 처음에 찾아낸 공통점을 구현한 것이다.
    for count in range(position):
        # 이해를 돕기 위한 수식, 첫수와 두번째 수를 더해 세번째 수를 만들어내고, 첫수에는 두번째 수를, 두번쨰 수에는 세번째 수를
        # third = first + second
        # first = second
        # second = third

        #굳이 third 를 만들지 않아도 가능하다.
        first, second = second, first + second

    # 0, 1부터 시작하여 N회를 돌기 때문에 first 가 된다.
    # ex) N이 5일 경우 포문을 돌고 난 후 first, second 값 (1, 1), (1, 2), (2, 3), (3, 5), (5, 8)
    return first % 1234567


assert second_solution(5000) == 1178031
assert second_solution(10000) == 1107030
assert second_solution(100000) == 1168141
assert second_solution(200000) == 672799
