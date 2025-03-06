T = int(input()) # 테스트 케이스 개수 입력
for tc in range(1,T+1): #테스트 케이스 번호 1부터 T까지 반복

    num_list = ['0','1','2','3','4','5','6','7','8','9'] #찾아야할 숫자 리스트 저장장
    n = int(input()) #정수입력력
    number = n #현재 검사 중인 숫자자
    Count = 1 # 몇 번째 배수인지 세는 변수 초기값1
    num_list2 = [] # 등장한 숫자를 저장할 리스트트

    while True: # 모든 숫자가 등장할때 까지 실행
        num_list2.extend(list(str(number))) #현재 숫자를 문자열로 바꾼 후 숫자리스트에 추가가
        num_list2 = list(set(num_list2)) # 중복제거 > 리스트 변환
        num_list2.sort() #리스트 정렬렬
        if num_list2 == num_list: #모든 숫자가 등장했는지 확인
            break # 모두 등장했다면 반복종료
        number += n # 다음배수 확인위해 현재숫자 증가
        Count += 1 #배수 카운트 증가
    
    print(f'#{tc} {Count * n}') #마지막으로 확인한 숫자 출력