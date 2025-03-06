T = int(input()) #테스트 케이스 개수 입력받기
for tc in range(1, T+1): #테이스 케이스 만큼 반복
    numbers = map(int, input().split()) #공백으로 나누어 입력받고 정수형으로 변환
    total = 0 # 홀수만 더한 총 합 변수생성
    for i in range(numbers): #숫자들을 하나씩 꺼내어
        if i % 2 == 1: # 숫자가 홀수라면(2로 나누어 나머지가 1)
            total += i # 총합에 더한다
print(f"#{tc} {total}") #해당 테스트 케이스와 총합을 출력
