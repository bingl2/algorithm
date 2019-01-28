"""

문제 설명
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

제한 사항
phone_book의 길이는 1 이상 1,000,000 이하입니다.
각 전화번호의 길이는 1 이상 20 이하입니다.

"""


def solution(phone_book):
    answer = True

    for pn_index, phone_num in enumerate(phone_book):
        for cpn_index, check_phone_num in enumerate(phone_book):
            if pn_index == cpn_index:
                continue

            if len(phone_num) > len(check_phone_num):
                break

            check_phone_num = check_phone_num[:len(phone_num)]

            if phone_num == check_phone_num:
                answer = False
                break

    return answer


assert solution(["119", "97674223", "1195524421"]) == False
assert solution(["123", "456", "789"]) == True
assert solution(["567", "1235", "12", "88", "123"]) == False

"""
무작정 풀기 진행.

정말 무식하게 빅오 n의 2승으로 풀이.
자기 자신은 패스, 접두어 이기 때문에 만약 검사해야할 길이보다 길 경우 중단.
배열을 이용하여 길이만큼 체크하고, 같을 경우 False 처리 진행.
 

"""
