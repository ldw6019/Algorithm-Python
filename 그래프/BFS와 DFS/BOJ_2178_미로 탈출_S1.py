"""
[문제] 백준 2178번 - 미로 탈출
[링크] https://www.acmicpc.net/problem/2178
[분류] DFS, BFS, 격자 그래프
[난이도] Silver 1 Tier
"""

# 입력 속도 최적화
import sys
input = sys.stdin.readline

from collections import deque

# 1. 입력 받기
N, M = map(int, input().split())
graph = []
for _ in range(N):
    row_str = input().strip() # 양끝 공백 제거
    graph.append([int(char) for char in row_str])

# 2. 이동 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    # 3. 큐 생성 및 시작점 추가
    queue = deque([(x, y)])
    
    while queue:
        cx, cy = queue.popleft()
        
        # 4. 네 방향 확인
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            # 5. 조건 체크 (미로 범위 내, 이동 가능 여부, 첫 방문 여부)
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1: # 아직 방문하지 않은 길이라면
                    # 6. 거리 업데이트 및 큐 삽입
                    graph[nx][ny] = graph[cx][cy] + 1
                    queue.append((nx, ny))
    
    # 7. 목적지 거리 반환
    return graph[N-1][M-1]

# BFS 실행 및 결과 출력
if __name__ == "__main__":
    print(bfs(0, 0))