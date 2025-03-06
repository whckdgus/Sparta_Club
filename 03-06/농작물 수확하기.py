T = int(input()) # 테스트 케이스 개수 입력

for tc in range(1,T+1):  #테스트 케이스 번호 1부터 T까지 반복
    N = int(input()) # 농장 크기 입력
    maze = [list(map(int, input().strip())) for _ in range(N)] # N x N 크기 농작물 정보 입력받기

    rows = len(maze) #행 개수저장
    cols = len(maze[0]) #열 개수 저장
    center_row = rows // 2 #가운데 행의 인덱스
    center_col = cols // 2 #가운데 열의 인덱스

    diamond = [] #다이아몬드 범위 내 숫자저장할 리스트
    for i in range(rows): #행 반복
        for j in range(cols): #열 반복
            if abs(i - center_row) + abs(j - center_col) <= center_row: 
                #현재위치의 행과 중앙행의 거리와 현재위치 열과 중앙 열의 거리의 합이
                #center_row이하면 다이아몬드 영역에 포함
                diamond.append(maze[i][j]) # 영역에 포함된 숫자 리스트에 추가가
    print(f"#{tc}",sum(diamond)) # 다이아몬드 모양 숫자들의 합 출력