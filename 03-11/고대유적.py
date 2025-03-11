T = int(input())  # 테스트 케이스 개수 입력

for tc in range(1, T + 1):  # 테스트 케이스 반복
    N, M = map(int, input().split())  # 격자 크기 입력
    arr = [list(map(int, input().split())) for _ in range(N)]  # 격자 정보 입력

    max_count = 0  # 최대 연속된 1의 길이 저장

    #행 탐색
    for i in range(N): # 행 탐색
        count = 0  # 현재 연속된 1의 개수
        for j in range(M): #열 탐색
            if arr[i][j] == 1:  # 1을 만나면 카운트 증가
                count += 1
                max_count = max(max_count, count)  # 최대값 업데이트
            else:
                count = 0  # 1이 끊기면 초기화

    #열(column) 탐색
    for j in range(M): #열 탐색
        count = 0  # 현재 연속된 1의 개수
        for i in range(N): #행 탐색
            if arr[i][j] == 1:  # 1을 만나면 카운트 증가
                count += 1
                max_count = max(max_count, count)  # 최대값 업데이트
            else:
                count = 0  # 1이 끊기면 초기화

    print(f"#{tc} {max_count}")  # 최종 결과 출력
