# 테스트 케이스 개수 T 입력력
T = int(input())

# T번 테스트 케이스 
for tc in range(1, T + 1):

    # N개의 박스, Q번의 명령어 개수 입력
    N, Q = map(int, input().split())

    # 길이 N의 리스트를 생성하고, 모든 값을 0으로 초기화
    box = [0] * N  

    # Q번 동안 명령어를 실행
    for i in range(1, Q + 1):

        # L부터 R까지의 범위 입력
        L, R = map(int, input().split())

        # L부터 R까지의 인덱스에 `i`값을 넣어줌
        for j in range(L, R + 1):
            box[j - 1] = i  # L, R은 1부터 시작하므로 -1하기

    print(f"#{tc}", *box)  # *box는 언패킹으로 공백으로 나누어 출력력
