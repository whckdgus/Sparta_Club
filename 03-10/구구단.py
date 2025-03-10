T = int(input())  # 테스트 케이스 입력
for tc in range(1, T + 1):  # 테이스 케이스 만큼 반복
    N = int(input())  # 정수 N 입력
    found = False  # False로 설정했다가 찾으면 True로 출력되고 끝

    for i in range(1, 10):  # 1부터 9 반복
        for j in range(1, 10):  # 1부터 9반복
            if i * j == N:  # i * j 가 N이라면
                found = True  # 파운드 변수는 참

    if found:  # 참이라면 YES 프린트
        print(f"#{tc} Yes")
    else:  # 참이 안 나오면 NO 프린트
        print(f"#{tc} No")

