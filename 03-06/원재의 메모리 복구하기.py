T = int(input())  # 테스트 케이스 개수 입력

for tc in range(1, T+1):
    memory = input().strip()  # 문자열 형태의 메모리 상태 입력 (공백제거)
    cnt = 0  # 변경 횟수 설정
    current = '0'  # 초기 상태는 모두 0

    for bit in memory: # 메모리 문자열 한 글자씩 bit로 순회회
        if bit != current:  # 현재 비트와 다르면 변경 필요
            cnt += 1 # 카운트 1증가
            current = bit  # 변경된 비트 현재 상태로 업데이트

    print(f"#{tc} {cnt}")  # 테스트 케이스와 변경횟수 출력력
