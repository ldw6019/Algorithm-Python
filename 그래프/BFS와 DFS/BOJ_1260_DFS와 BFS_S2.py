"""
[문제] 백준 1260 - DFS와 BFS
[링크] https://www.acmicpc.net/problem/1260
[분류] 그래프 이론, 그래프 탐색
[난이도] Silver 2 Tier
"""

# 입력 속도 최적화
import sys
input = sys.stdin.readline
from collections import deque


def dfs(v, graph, visited):
    visited[v] = True
    print(v, end=' ')

    for nxt in graph[v]:
        if not visited[nxt]:
            dfs(nxt, graph, visited)
    

def bfs(graph, start):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for nxt in graph[v]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

def solve():
    n, m, v = map(int, input().split())

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, n+1):
        graph[i].sort()

    visited = [False] * (n+1)

    dfs(v, graph, visited)
    print('')
    bfs(graph, v)

if __name__ == "__main__":
    solve()