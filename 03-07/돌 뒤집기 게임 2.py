T = int(input())  # 테스트 케이스 입력

for tc in range(1, T + 1): #테스트 케이스 만큼 반복 
    N, M = map(int, input().split()) #돌의수 N과 뒤집기 횟수 M 입력
    arr = list(map(int, input().split())) # N개 돌의 초기상태 입력

    for _ in range(M): # M번 반복
        i, j = map(int, input().split()) # M번만큼 i,j반복
        i = i - 1 #인덱스는 0부터 시작하므로 -1

        for l in range(1, j + 1): # 1부터 j+1 반복 (마주보는 돌의 범위) 
            if 0 <= i - l and i + l < N: # i기준 마주보는 돌 왼쪽이 0이상 오른쪽이 N보다 작고(범위)
                if arr[i - l] == arr[i + l]: #i기준 마주보는 왼쪽과과 오른쪽이 같은색이라면
                    arr[i - l] = (arr[i - l] + 1) % 2 # 0을 1로 또는 1을 0으로 바꿔준다
                    arr[i + l] = (arr[i + l] + 1) % 2 # 0을 1로 또는 1을 0으로 바꿔준다

    print(f"#{tc}", *arr) #언패킹으로 공백으로 나눠 arr 출력
