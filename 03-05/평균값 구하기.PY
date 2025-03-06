T = int(input())  # 테스트 케이스 개수 입력

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))  # 숫자 리스트 입력
    total = sum(numbers)  # 리스트의 모든 원소를 더하기
    n = len(numbers)  # 원소 개수
    aver = round(total / n)  # 평균 구하기 (반올림)

    print(f"#{tc} {aver}")  # 해당 테이스 케이스 번호와 평균값 출력
