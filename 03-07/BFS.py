from collections import deque

# BFS 함수 정의
def bfs(start):
    # 방문 여부를 저장하는 리스트
    visited = [False] * (V + 1)
    
    # BFS를 위한 큐 생성
    q = deque([start])
    visited[start] = True

    # 탐색 순서 저장
    result = []

    while q:
        now = q.popleft()
        result.append(now)  # 현재 방문한 노드를 결과에 추가

        # 현재 노드와 연결된 노드들을 확인
        for next in sorted(G_list[now]):  # 정점 번호가 작은 순서대로 방문
            if not visited[next]:
                q.append(next)
                visited[next] = True  # 방문 처리

    # 결과 출력
    print(" - ".join(map(str, result)))


# 정점(V)과 간선(E) 입력
V, E = 7, 8

# 그래프 저장 (인접 리스트 방식)
G_list = [[] for _ in range(V + 1)]

# 주어진 간선 정보
edges = [
    (1, 2), (1, 3), (2, 4), (2, 5),
    (4, 6), (5, 6), (6, 7), (3, 7)
]

# 간선 정보를 인접 리스트에 추가
for s, e in edges:
    G_list[s].append(e)
    G_list[e].append(s)  # 무방향 그래프이므로 양쪽 연결

# BFS 탐색 수행 (시작 정점: 1)
bfs(1)
