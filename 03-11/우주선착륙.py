T = int(input())  # 테스트 케이스 개수 입력

# 8방향 (상, 하, 좌, 우, 좌상, 우상, 좌하, 우하)
dr = [-1, 1, 0, 0, -1, -1, 1, 1]  
dc = [0, 0, -1, 1, -1, 1, -1, 1]  

for tc in range(1,T + 1):  # 테스트 케이스 반복
    n, m = map(int, input().split())  # 격자 크기 입력
    arr = [list(map(int, input().split())) for _ in range(n)]  # 격자 정보 입력
    result = 0  # 예비 후보지 개수 저장 변수

    for i in range(n):  # 행 순회
        for j in range(m):  # 열 순회
            temp = arr[i][j]  # 현재 위치 값 저장
            section = 0  # 착륙지보다 낮은 지역 개수 카운트 

            for k in range(8):  # 8방향 탐색
                nr = i + dr[k]  # 새 위치 (행)
                nc = j + dc[k]  # 새 위치 (열)

                if 0 <= nr < n and 0 <= nc < m:  # 범위 체크
                    if arr[nr][nc] < temp:  # 착륙지보다 낮은 지역 확인
                        section += 1  # 착륙지보다 낮은 지역 개수 추가

            if section >= 4:  # 4개 이상이면 예비 후보지로 선정
                result += 1  # 예비 후보지 개수 증가

    print(f"{tc} {result}")  # 결과 출력
