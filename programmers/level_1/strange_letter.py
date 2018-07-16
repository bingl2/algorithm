"""
문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

제한 사항
문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.

입출력 예
string	           return
try hello world	   TrY HeLlO WoRlD

입출력 예 설명
try hello world는 세 단어 try, hello, world로 구성되어 있습니다.
각 단어의 짝수번째 문자를 대문자로, 홀수번째 문자를 소문자로 바꾸면 TrY, HeLlO, WoRlD입니다. 따라서 TrY HeLlO WoRlD 를 리턴합니다.
"""


def solution(string):
    answer = ''
    char_count = 0

    # 문장에서 단어의 시작과 끝을 카운팅 하는 방식으로 문제를 풀었다.
    for char in string:
        # 공백이 나오면 단어 카운트를 초기화 시켰다.
        if char == ' ':
            char_count = 0
        else:

            if char_count % 2 == 0:
                char = char.upper()
            else:
                char = char.lower()
            char_count += 1

        # 공백이면 공백, 카운팅에 따른 변경은 받아드렸다.
        answer = answer + char

    return answer


print(solution("try hello world")) # TrY HeLlO WoRlD


"""
걸린 시간 : 4시간
난이도 : Basic

걸린 시간이 정말 부끄럽다. 하지만 남겨야겠다.

문제 분석에 실패했다. 아주 부끄러운 실수다. 문제를 보자마자 자신 있게 split 을 사용하며 해결을 진행했는데
제공하는 테스트 케이스는 통과해도 프로그래머스에서 제공하는 채점에서 실패 케이스들이 발생했다. 

이유는 split을 사용하면서 나도 모르게 공백을 split 하며 자연스럽게 공백들이 아무리 많아도 깔끔하게 한개로 줄여서 보여주는걸로 착각을 했다.
ex) AS   FFFDDD  AS -> As FfFdDd As 

그렇게 고민을 문자열을 쪼개서도 해보고, 내가 어떤 실수를 했나 문제를 다시 읽어봐도 문제를 찾지 못했다.

그러다가 멍청하지만 뛰어난 생각으로 문자에는 공백이 무조건 들어간다니 공백과 공백 사이의 공백을 문자로 취급해서 넣어주는건 어떨까 라는 생각을 했고
정말 우연치 않게 채점 점수가 오르는 것을 확인했다. 하지만 역시 실패 케이스 발생했다.

이 상태로 문제를 다시 읽으니 머리를 종으로 한대 맞은 기분이였다. 실패 할 때마다 문제를 지속적으로 읽고, 원하고자 하는 요구사항을 확인 했는데 
너무나 어처구니 없는 마음데로 해석하는 실수를 해버렸다.

124나라 문제 풀때와는 다르게 너무나 허탈했다 .. 반성하자.
"""