"""
[문제] 정올 2097번 - 지하철_advanced
[링크] http://jungol.co.kr/problem/2097
[분류] 그래프 알고리즘, Dijkstra
[난이도] Advanced Tier
"""

import sys

# 입력 속도 최적화
input = sys.stdin.readline
INF = 99999

def solve():
    # n: 역의 수, m: 목적지 역 번호
    n, m = map(int, input().split())
    
    adj = []
    for _ in range(n):
        adj.append(list(map(int, input().split())))
        
    # 수업 자료(알고리즘 8.8)를 참고하여 변수 초기화
    dist = [INF] * n
    found = [False] * n    
    # 바로 이전 정점을 저장할 배열
    path = [-1] * n 
    
    # 1번 역(코드 상 인덱스 0)에서 출발
    dist[0] = 0
    
    # Dijkstra 최단경로 알고리즘 구현
    for _ in range(n):
        min_dist = INF
        u = -1
        
        # 아직 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 탐색
        for i in range(n):
            if not found[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
                
        if u == -1:
            break
            
        found[u] = True
        
        # 선택된 노드를 거쳐가는 인접 노드들의 거리 갱신
        for w in range(n):
            if u != w and not found[w]:
                if dist[u] + adj[u][w] < dist[w]:
                    dist[w] = dist[u] + adj[u][w]
                    # path[]에 바로 이전 정점을 저장
                    path[w] = u  
                    
    # 1. 목적지까지의 최소 소요 시간 출력
    print(dist[m-1])
    
    # 2. 강의 자료 응용
    result_path = []
    curr = m - 1
    
    # 목적지부터 시작점까지 path 배열을 타고 거슬러 올라감
    while curr != -1: 
        # 인덱스를 다시 1번부터 시작하는 역 번호로 변환
        result_path.append(curr + 1) 
        curr = path[curr]
        
    # 목적지부터 역추적했으므로 출력 시에는 뒤집어서 출발지->도착지 순으로 만듦
    result_path.reverse()
    print(' '.join(map(str, result_path)))

if __name__ == "__main__":
    solve()