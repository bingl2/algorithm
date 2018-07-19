"""
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

제한 조건
n은 2이상 1,000,000이하의 자연수입니다.

입출력 예
n	result
10	4
5	3

입출력 예 설명
입출력 예 #1
1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환

입출력 예 #2
1부터 5 사이의 소수는 [2,3,5] 3개가 존재하므로 3를 반환
"""
import time


def solution(n):
    answer_array = list(range(2, n + 1))
    eratos_range = list(range(2, int(n ** 0.5 + 1)))

    for er_num in eratos_range:
        for check_num in answer_array:
            if check_num != er_num:
                if check_num % er_num == 0:
                    answer_array.remove(check_num)

    return len(answer_array)


startTime = time.time()

assert solution(10000) == 1229

endTime = time.time() - startTime

print(endTime)
# assert solution(10000) == 1229
# assert solution(20000) == 2262


