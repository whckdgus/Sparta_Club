def check_slope(row):
    cnt = 1  # 연속된 같은 높이의 타일 개수 

    for i in range(1, N):  # 왼쪽부터 오른쪽으로 한 칸씩 확인
        if row[i] == row[i-1]:  # 같은 높이라면
            cnt += 1  # 연속 개수 증가

        elif row[i] - row[i-1] == 1 and cnt >= X:  # 높이가 1 증가
            cnt = 1  # 경사로 설치 후 다시 카운트 시작

        elif row[i-1] - row[i] == 1 and cnt >= 0:  # 높이가 1 감소 
            cnt = -X + 1  # 경사로 설치 

        else:  # 높이 차이가 2 이상이면 활주로 불가능
            return 0  

    if cnt >= 0:  # 경사로 설치가 정상적으로 끝났다면
        return 1  
    return 0  # 마지막에 경사로 설치 불가능하면 실패

T = int(input())  # 테스트 케이스 개수
for tc in range(T): # t번 반복
    N, X = map(int, input().split())  # 지도 크기와 경사로 길이 입력받기
    A = []  # 지형 정보를 저장할 배열
    result = 0  # 건설 가능한 활주로 개수

    # 가로줄 검사
    for i in range(N):
        A.append(list(map(int, input().split())))  # 지도 입력 받기
        result += check_slope(A[i])  # 해당 행이 활주로 건설 가능한지 검사

    # 세로줄 검사
    for i in range(N):
        temp = []  # i번째 열을 저장할 리스트
        for j in range(N):
            temp.append(A[j][i])  # 세로 방향으로 값 추출
        result += check_slope(temp)  # 해당 열이 활주로 건설 가능한지 검사

    #  결과 출력
    print("#{} {}".format(tc+1, result))
