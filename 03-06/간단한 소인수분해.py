T = int(input()) # 테스트 케이스 개수 입력

for tc in range(1, T+1): #테스트 케이스 번호 1부터 T까지 반복복
    N = int(input()) #소인수분해할 숫자 n입력력
    num_lst = [2,3,5,7,11] # 소인수 5개 리스트 저장장
    cnt_lst = [0,0,0,0,0] # 각 개수 저장할 리스트 저장
    for i in range(5): # 소인수 개수만큼 반복복
        while N % num_lst[i] == 0: # N이 현재 소인수로 나눠 떨어지면 반복
            cnt_lst[i] += 1 # 나눈 횟수 증가가
            N //= num_lst[i] #N 을 해당 소인수로 나눠서 갱신
    print(f'#{tc} ', end='') # 줄 바꿈 방지 및 공백추가
    print(*cnt_lst) #리스트 원소 공백기준으로 출력