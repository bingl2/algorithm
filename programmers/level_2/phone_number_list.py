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
    phone_book = sorted(phone_book)

    for pn, pn2 in zip(phone_book, phone_book[1:]):
        if pn2.startswith(pn):
            return False

    return True


assert solution(["119", "97674223", "1195524421"]) == False
assert solution(["123", "456", "789"]) == True
assert solution(["567", "1235", "12", "88", "123"]) == False

"""
무작정 풀기 진행.

정말 무식하게 빅오 n의 2승으로 풀이.
자기 자신은 패스, 접두어 이기 때문에 만약 검사해야할 길이보다 길 경우 중단.
배열을 이용하여 길이만큼 체크하고, 같을 경우 False 처리 진행.

빠른 풀이후 개선 방법

- 속도 개선
1. 배열을 길이별로 정리를 할 수 있다면 비교해할 부분이 상당수 줄어들것 같다.  


- 읽기 쉬운 코드 개선
1. 필요한 로직 파악이 필요, 숫자가 들어있는 배열을 정렬 하면 앞자리의 숫자 크기 순서데로 배열이됨.
2. 만약 '뒤의 수' 가, '앞의 수' 를 포함하지 않을 경우 '뒤의 수의 뒤의 수' 는 당연히 '앞의 수' 를 포함하지 않음.

"""