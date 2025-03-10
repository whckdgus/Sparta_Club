T = int(input())  # 테스트 케이스 개수 입력

for tc in range(1, T + 1):
    N, M = map(int, input().split())  
    arr = list(map(int, input().split()))  # 초기 상태를 숫자로 변환

    for _ in range(M):  # 명령 개수만큼 반복
        i, j = map(int, input().split())  
        
        # i번부터 j개의 상태를 변경하는데, 범위를 벗어나지 않도록 체크
        for p in range(i - 1, i - 1 + j):  
            if p < N:  # 범위를 벗어나지 않을 때만 변경
                arr[p] = 1 - arr[p]  # 상태 반전 (0 → 1, 1 → 0)

    print(f"#{tc}", *arr)  # 리스트 요소를 공백으로 구분하여 출력
