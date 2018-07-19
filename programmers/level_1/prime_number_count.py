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


def bingl2_solution(n):
    # 정답 리스트를 만듬
    answer_array = list(range(2, n + 1))
    # 체로 거를 숫자들의 범위를 지정함. (2, N을 2부터 sqrt(N)까지 나눠서 나누어지지 않으면 소수)
    eratos_range = list(range(2, int(n ** 0.5 + 1)))

    # 채의 도는 수
    for er_num in eratos_range:
        # 정답을 제거해 나갈 수 (2의 배수로 시작)
        for check_num in answer_array:
            # 본인은 나누어 떨어지기 때문에, 본인 이외 체크
            if check_num != er_num:
                # 그 이외의 나누어 떨어질 경우 소수가 아님.
                if check_num % er_num == 0:
                    # 만약 삭제할 숫자가 eraots_range 에 존재할 경우 제거
                    if check_num in eratos_range:
                        eratos_range.remove(check_num)
                    # 정답 리스트에서 체크한 숫자 제거
                    answer_array.remove(check_num)

        # 일단 지속적으로 최적화를 시켜볼 생각이다.
        # 중간에 존재하는 본인 이외의 숫자 체크 등의 부분 ..

    # 정답 리스트 길이 반환
    return len(answer_array)


startTime = time.time()

assert bingl2_solution(10000) == 1229

endTime = time.time() - startTime

print(endTime)

# assert solution(10000) == 1229
# assert solution(20000) == 2262


