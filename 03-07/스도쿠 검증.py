T = int(input())  # 테스트 케이스 개수 입력

for tc in range(1, T + 1): # 테스트 케이스 반복복
    arr = [list(map(int, input().split())) for _ in range(9)]  # 9x9 스도쿠 판 입력 받기
    flag = 1  # 올바른 스도쿠인지 판별하는 변수

    # 행 체크
    for i in range(9): # 행 순회
        cmp = [0] * 9  # 1에서 9 숫자 등장했는지 체크할 리스트
        for j in range(9): # 열 순회
            cmp[arr[i][j] - 1] += 1 #숫자가 등장한 위치에 카운팅
        if 0 in cmp:  # 모든 숫자가 등장하지 않으면
            flag = 0 # 스토쿠 규칙 어긴것
            break #검사 중단 빠져나옴

    # 열 체크
    if flag: # flag가 True라면
        for i in range(9): # 열 순회
            cmp = [0] * 9 # 1에서 9 숫자 등장했는지 체크할 리스트
            for j in range(9): #행 순회
                cmp[arr[j][i] - 1] += 1 #숫자 등장한 위치 카운팅
            if 0 in cmp: # 1~9 중 빠진 숫자 있으면면
                flag = 0 # 위반
                break # 중단하고 빠져나옴옴

    # 3x3 박스 검증
    if flag:
        for i in range(0, 9, 3): # 3씩 증가하며 3×3 박스 시작 행 순회
            for j in range(0, 9, 3): #3씩 증가하며 3×3 박스 시작 열 순회
                cmp = [0] * 9 # 1에서 9 숫자 등장했는지 체크할 리스트
                for x in range(3): # 3x3 박스 내부 행 탐색
                    for y in range(3): # 3x3 박스 내부 열 탐색색
                        cmp[arr[x + i][y + j] - 1] += 1 #숫자 등장한 위치 카운팅
                if 0 in cmp: # 1~9 중 빠진 숫자 있으면
                    flag = 0 # 위반
                    break # 중단하고 빠져나옴
            if flag == 0:
                break  # 바깥 루프도 빠져나오기 위해 필요

    # 🔹 결과 출력
    print(f"#{tc} {flag}") #tc와 유효한 결과인지 판별하는 flag 출력
