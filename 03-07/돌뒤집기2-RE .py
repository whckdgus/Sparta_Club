T=int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):
        i,j = map(int,input().split())
        i -= 1

        for l in range(1,j+1):
            if 0 <= i - l and i + l < N: 
                if arr[i-l] == arr[i+l]:
                    arr[i-l] = 1 -arr[i-l]
                    arr[i+l] = 1-arr[i+l]

    print(f"#{tc}", *arr)
