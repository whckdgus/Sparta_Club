#테스트 케이스 개수 T 입력
T = int(input())

# T번 테스트 케이스 반복
for tc in range(1, T + 1):

    # 한변의 길이 N , 플레이어가 돌을 놓는 횟수 M 입력받음
    N, M = map(int, input().split())

    # NxN 크기의 보드 0으로 초기화 
    board = [[0] * N for _ in range(N)]

    # 오셀로 초기 돌 배치 (중앙 4칸)
    board[N // 2 - 1][N // 2 - 1], board[N // 2][N // 2] = 2, 2  # 백돌 (2)
    board[N // 2 - 1][N // 2], board[N // 2][N // 2 - 1] = 1, 1  # 흑돌 (1)

    # 돌의 위치에서 8방향 탐색 (시계방향)
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]  # 행 이동 (위, 우상, 우, 우하, 아래, 좌하, 좌, 좌상)
    dc = [0, 1, 1, 1, 0, -1, -1, -1]  # 열 이동

    # M번 돌을 놓음
    for i in range(M):
        # 돌을 놓을 위치 (r, c)와 플레이어(1=흑돌, 2=백돌) 입력
        r, c, player = map(int, input().split())

        # 인덱스 0 부터 시작
        r -= 1
        c -= 1

        # 현재 돌을 놓은 위치 저장 
        x, y = r, c

        # 보드에 현재 플레이어의 돌 배치
        board[r][c] = player

        # 현재 위치에서 8방향 탐색
        for j in range(8):

            # 한 칸씩 이동한 새로운 위치
            nr = r + dr[j]
            nc = c + dc[j]

            # 탐색 범위를 벗어나거나, 빈 공간이거나, 같은 색이면 다음 방향 탐색
            if nr < 0 or nr >= N or nc < 0 or nc >= N or not board[nr][nc] or board[r][c] == board[nr][nc]:
                continue  # 현재 방향 무시하고 다음 방향 탐색

            # 상대방 돌이 있는 방향에서 같은 색 돌이 나올 때까지 반복 탐색
            while True:

                # 한 칸 이동 후 같은 방향으로 계속 탐색
                r, c = nr, nc
                nr, nc = r + dr[j], c + dc[j]

                # 같은 색 돌을 발견하면, 이제 되돌아가면서 사이의 돌을 뒤집음
                if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == board[x][y]:
                    # 되돌아가면서 돌 색깔 변경
                    while r != x or c != y:
                        board[r][c] = board[x][y]  # 현재 돌 색으로 변경
                        nr, nc = r - dr[j], c - dc[j]  # 한 칸 뒤로 이동
                        r, c = nr, nc  # 현재 위치 갱신신
                    break  # 돌 뒤집기 완료 후 종료

                # 같은 색 돌이 계속 이어지는 경우, 다음 칸 탐색
                elif 0 <= nr < N and 0 <= nc < N and board[nr][nc] == board[r][c]:
                    continue  # 탐색 진행

                # 상대방 돌이 없는 경우, 탐색 중단 (돌 뒤집기 불가능)
                else:
                    r, c = x, y  # 원래 위치로 되돌아감
                    break  # 탐색 종료

    # 마지막 흑돌이랑 백돌 개수 세기
    b_cnt = 0  # 흑돌 개수
    w_cnt = 0  # 백돌 개수

    # 보드를 순회하며 돌 개수 카운트
    for i in range(N): # 행 순회
        for j in range(N): #열 순회
            if board[i][j] == 1: # 1이면
                b_cnt += 1  # 흑돌 개수 증가
            if board[i][j] == 2: #2이면
                w_cnt += 1  # 백돌 개수 증가

    print(f'#{tc} {b_cnt} {w_cnt}') #tc와 흑돌,백돌 개수 출력력
