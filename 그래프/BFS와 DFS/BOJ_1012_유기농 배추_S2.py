"""
[문제] 백준 1012번 - 유기농 배추
[링크] https://www.acmicpc.net/problem/1012
[분류] 그래프, BFS
[난이도] Silver 2 Tier
"""

# 입력 속도 최적화
import sys
input = sys.stdin.readline 
sys.setrecursionlimit(10**5) # 재귀 횟수 한도 증가

def solve():
    T = int(input())
    for _ in range(T):
        m, n, k = map(int, input().split()) # m: 가로 길이, n: 세로 길이, k: 배추 개수
        graph = [[0] * m for _ in range(n)]

        for _ in range(k):
            x, y = map(int, input().split())
            graph[y][x] = 1
        
        count = 0
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        def dfs(graph, x, y):
            graph[y][x] = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (0 <= nx < m) and (0 <= ny < n) and (graph[ny][nx] == 1):
                    dfs(graph, nx, ny)

        for i in range(n):
            for j in range(m):
                if graph[i][j] == 1:
                    dfs(graph, j, i)
                    count += 1
        print(count)


if __name__ == "__main__":
    solve()