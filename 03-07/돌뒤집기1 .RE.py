T=int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = input().split()

    for _ in range(M):
        i,j = map(int,input().split())
        i -= 1

        for l in range(i,i+j): #인덱스가 4까지임 ^^ (N이 5라면)
            if l >= N:
                break
            if arr[l] != arr[i]: 
                arr[l] = arr[i]
    
    print(f"#{tc}", *arr)