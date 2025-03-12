def s(t):  #  테스트 케이스 번호 t
    arr = list(map(str, input().split()))  # 입력을 문자열 리스트로 변환
    total_time = 0  # 총 걸린 시간 초기화
 
    # 로봇 B와 O의 시작 위치(1번 위치) 및 마지막 버튼 누른 시간(초기값: 0)
    robots = {'B': [1, 0], 'O': [1, 0]}

    # 1부터 시작하여, 2칸씩 이동하면서 작업 리스트를 처리 (로봇 이름, 버튼 위치)
    for i in range(1, len(arr) - 1, 2):
        robot = arr[i]  # 현재 버튼을 누를 로봇 ('B' 또는 'O')
        target_pos = int(arr[i + 1])  # 해당 로봇이 눌러야 할 버튼 위치

        # 이동해야 할 거리 = 목표 위치 - 현재 위치
        robot_button_distance = abs(target_pos - robots[robot][0])

        #  현재 로봇이 주어진 시간 (전체 경과 시간 - 이전 버튼 누른 시간)
        robot_time = total_time - robots[robot][1]

        # 만약 이동해야 할 거리보다 주어진 시간이 크거나 같다면 (즉, 이동을 마쳤다면)
        if robot_button_distance <= robot_time:
            total_time += 1  # 버튼만 누르면 되므로 1초 추가
        else:
            # 총 소요 시간 = (남은 거리 이동 시간) + (버튼 누르는 1초)
            total_time += (robot_button_distance - robot_time) + 1

        #  현재 로봇의 위치와 마지막 버튼 누른 시간을 업데이트
        robots[robot] = [target_pos, total_time]

    print(f'#{t} {total_time}')  # 테스트 케이스 결과 출력
  
if __name__ == '__main__':  #  메인 실행부
    T = int(input())  #  테스트 케이스 개수 입력
    for t in range(1, T + 1):  #  각 테스트 케이스 실행
        s(t)  # 함수 호출
