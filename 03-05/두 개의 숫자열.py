T = int(input())  # 테스트 케이스 개수 T를 입력
for tc in range(1, T+1):  # 테스트 케이스 개수만큼 반복문 실행
    N, M = map(int, input().split())  # 두 리스트 길이 N,M 입력받음
    A_list = list(map(int, input().split()))  # A 리스트 공백기준 입력받고 정수 변환
    B_list = list(map(int, input().split()))  # B 리스트 공백기준 입력받고 정수 변환
    max_num = float("-inf")  # 최대 곱의 합을 저장할 변수
    if N > M:  # 항상 N <= M이 되도록 리스트를 정렬 (N이 더 크다면)
        A_list, B_list = B_list, A_list  # A와 B리스트 스왑
        N, M = M, N  # N,M 길이 스왑
    for i in range(M-N+1):  # B_list에서 B_list 를 이동할 수 있는 구간 반복
        sum_num = 0  # 곱의 합 저장 변수 생성
        for j in range(N):  # N번만큼 반복
            # 이동하면서 A_list의 j번째 값과 B_list의 i+j값을 곱해서 더함
            sum_num += A_list[j] * B_list[i + j]
        if max_num < sum_num:  # sum_num이 max_sum 보다 크다면
            max_num = sum_num  # 해당 sum_num이 max_num 으로 갱신
    print(f"#{tc} {max_num}")  # 해당 tc와 최대 곱의 합 출력
