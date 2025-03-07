T=int(input()) # 테스트 케이스 입력
for tc in range(1, T + 1): #테스트 케이스 만큼 반복
    N, M = map(int, input().split()) # N개의 돌과 M개 줄 입력
    arr = input().split() # 입력간 공백기준 나누기

    for _ in range(M): # M번 반복
        i, j = map(int, input().split()) # i,j 정수로 입력받기

        for p in range(i - 1, i + j - 1): 
            #인덱스가 0부터 시작이므로 
            # i번째 돌은 i-1로 바꾸고 여기부터 
            # i+j-1까지 돌의색 범위 바꿔야 하므로 반복
            if p >= len(arr): # 해당 인덱스가 arr의 길이랑 같거나 크면 끝이므로
                break # 멈춰준다
            if arr[p] != arr[i - 1]: # i-1번째 인덱스가 arr[p]와 다르다면
                arr[p] = arr[i - 1] # i-1번째 값으로 바꿔준다.
    print(f"#{tc} {' '.join(arr)}")
