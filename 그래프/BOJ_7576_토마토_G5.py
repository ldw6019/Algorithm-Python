"""
[문제] 백준 7576번 - 토마토
[링크] https://www.acmicpc.net/problem/7576
[분류] 그래프, BFS
[난이도] Gold 5 Tier
"""

from collections import deque 
# 입력 속도 최적화
import sys
input = sys.stdin.readline

def solve():
    # 상, 하, 좌, 우 이동 리스트
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    queue = deque()

    m, n = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
   
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((i, j))
    while(queue):
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((ny, nx))
    maxday = 0
    for row in graph:
        for value in row:
            if value == 0: # 하나라도 안 익은 게 있다면
                print(-1)
                return
            # 현재까지의 최댓값과 비교해서 더 큰 값을 저장
            if value > maxdays:
                maxdays = value
    print(max_days - 1)

if __name__ == "__main__":
    solve()