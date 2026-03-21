"""
[문제] 백준 2606번 - 바이러스
[링크] https://www.acmicpc.net/problem/2606
[분류] 그래프 이론, DFS, BFS
[난이도] Silver 3 Tier
"""

# 입력 속도 최적화
import sys
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    for nxt in graph[v]:
        if not visited[nxt]:
            dfs(graph, nxt, visited)

def solve():
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (n + 1)
    dfs(graph, 1, visited)
    print(sum(visited) -1)


if __name__ == "__main__":
    solve()