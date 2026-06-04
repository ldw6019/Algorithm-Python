"""
[문제] 백준 2178번 - 미로 탈출
[링크] https://www.acmicpc.net/problem/2178
[분류] DFS, BFS, 격자 그래프
[난이도] Silver 1 Tier
"""

import sys
input = sys.stdin.readline

from collections import deque

def solve():
    N, M = map(int, input().split())
    graph = []
    for _ in range(N):
        row = input().strip()  # 양끝 공백 제거
        graph.append([int(char) for char in row])

    # 상하좌우 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        # 큐 생성
        queue = deque([(x, y)])
       
        while queue:
            cx, cy = queue.popleft()
           
            # 네 방향 확인
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
               
                #  유효성, 방문여부 검사
                if 0 <= nx < N and 0 <= ny < M:
                    if graph[nx][ny] == 1:  # 아직 방문하지 않았다면
                        # 거리 갱신 및 큐 삽입
                        graph[nx][ny] = graph[cx][cy] + 1
                        queue.append((nx, ny))
       
        # 목적지 거리 반환
        return graph[N-1][M-1]
    print(bfs(0, 0))

if __name__ == "__main__":
    solve()