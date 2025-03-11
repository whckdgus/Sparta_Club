T = int(input())  # 테스트 케이스 개수 입력
dr = [1, -1, 0, 0]  # 행 이동 방향 (상하좌우)
dc = [0, 0, 1, -1]  # 열 이동 방향 (상하좌우)

for tc in range(1,T + 1):  # 테스트 케이스 각 반복
    n, m = map(int, input().split())  # 격자 크기 입력
    arr = [list(map(int, input().split())) for _ in range(n)]  # 격자 정보 입력
    result = 0  # 최대 합 저장 변수

    for i in range(n):  # 행 순회
        for j in range(m):  # 열 순회
            temp = arr[i][j]  # 현재 위치 값 저장
            for k in range(4):  # 네 방향 탐색
                for x in range(1, arr[i][j] + 1):  # 현재 값만큼 확장하여 탐색
                    if 0 <= i + x * dr[k] < n and 0 <= j + x * dc[k] < m:  # 범위 체크
                        temp += arr[i + x * dr[k]][j + x * dc[k]]  # 값 누적
            result = max(temp, result)  # 최대값 갱신
    print(f"#{tc} {result}")  # 결과 출력
