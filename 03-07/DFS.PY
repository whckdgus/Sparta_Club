def dfs_l(s, V, adj_list):
    """ 
    인접 리스트를 사용한 DFS 탐색 함수 
    - s: 시작 정점
    - V: 정점 개수
    - adj_list: 인접 리스트 (연결 정보)
    """
    visited = [0] * (V + 1)  # 방문 여부 체크
    stack = []  # 돌아갈 경로 저장할 스택
    visited[s] = 1  # 시작 정점 방문 처리
    result = [s]  # 방문한 정점 순서 저장

    v = s  # 현재 정점

    while True:
        for w in sorted(adj_list[v]):  # 작은 번호부터 방문 (오름차순 정렬)
            if not visited[w]:  # 방문하지 않은 정점만 탐색
                stack.append(v)  # 돌아올 곳 저장
                visited[w] = 1  # 방문 처리
                result.append(w)  # 방문 순서 저장
                v = w  # 현재 정점 변경
                break
        else:
            if stack:  # 돌아갈 곳이 남아 있다면
                v = stack.pop()
            else:  # 돌아갈 곳이 없으면 탐색 종료
                break

    print(*result)  # 방문한 정점 출력


# 🔹 입력 처리
V, E = map(int, input().split())  # 정점 개수, 간선 개수 입력
edges = list(map(int, input().split()))  # 간선 정보 입력

# 🔹 인접 리스트 생성
adj_list = [[] for _ in range(V + 1)]

for i in range(E):
    s, e = edges[i * 2], edges[i * 2 + 1]
    adj_list[s].append(e)
    adj_list[e].append(s)  # 무향 그래프이므로 양방향 추가

# 🔹 DFS 탐색 실행
dfs_l(1, V, adj_list)
