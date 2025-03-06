T = int(input())  # 테스트 케이스 개수 입력받기

for tc in range(1, T+1):  # 테이스 케이스 만큼 반복
    N, K = map(int, input().split())  # 학생수와 k번째 학생번호 입력
    student_dict = {}  # 학생 번호별 점수 딕셔너리로 저장
    score_list = []  # 점수만 저장할 리스트를 생성
    grade_list = ['A+', 'A0', 'A-', 'B+', 'B0',
                  'B-', 'C+', 'C0', 'C-', 'D0']  # 학점 리스트에 저장

    for i in range(1, N+1):  # 학생수 만큼 반복
        mid, final, homework = map(int, input().split())  # 중간,기말,과제 입력
        total_score = mid * 0.35 + final * 0.45 + homework * 0.2  # 총점 계산
        student_dict[i] = total_score  # 학생 i에 대한 점수 딕셔너리에 저장
        score_list.append(total_score)  # 점수 리스트에 저장

    score_list.sort(reverse=True)  # 점수 내림차순 정렬

    for i in range(len(score_list)):
        if student_dict[K] == score_list[i]:  # K번 학생의 점수 찾기
            grade = grade_list[i // (N // 10)]  # 등급 계산
            print(f"#{tc} {grade}")  # 해당 tc와 학점 출력
            break  # 찾으면 반복 종료 (불필요한 반복 방지)
