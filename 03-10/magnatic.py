for tc in range(1, 11): # 10개의 테스트 케이스스
    N = int(input())  # 격자 크기 입력
    magnetic = [list(map(int, input().split())) for _ in range(N)]  # 격자 입력

    cnt = 0  # 교착 상태 개수
    for j in range(N):  # 열 단위 탐색
        flag = 0  # 현재 상태
        for i in range(N):  # 행을 위에서 아래로 탐색
            if magnetic[i][j] == 1:  # N극(1)을 만나면
                flag = 1  # 활성화
            elif magnetic[i][j] == 2 and flag == 1:  # S극(2)을 만나면 교착
                cnt += 1 # 교착 상태 증가
                flag = 0  # 초기화
    print(f'#{tc}', cnt) # tc와 교착 상태 개수 출력