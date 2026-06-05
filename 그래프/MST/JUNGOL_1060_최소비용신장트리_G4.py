"""
[문제] 정올 1060번 - 최소비용신장트리
[링크] http://jungol.co.kr/problem/1060
[분류] 그래프 알고리즘, MST, Kruskal
[난이도] Gold 4 Tier (Advanced)
"""


import sys
input = sys.stdin.readline

class DisjointSets:
    def __init__(self, n):
        self.parent = [-1] * n

    def find(self, id):
        if self.parent[id] < 0:
            return id
        # 경로 압축
        self.parent[id] = self.find(self.parent[id])
        return self.parent[id]
    
    def union(self, s1, s2):
        S1 = self.find(s1)
        S2 = self.find(s2)

        if S1 == S2:
            return
        
        # 번호가 작은 쪽을 루트로
        if S1 > S2: 
            S1, S2 = S2, S1
        self.parent[S2] = S1

def kruskal(n, adj):
    ds = DisjointSets(n)
    edges = []

    # i < j 인 우측 상단 삼각형만 탐색하므로 0을 무시할 필요가 없음
    for i in range(n - 1):
        for j in range(i + 1, n):
            edges.append((i, j, adj[i][j]))
            
    edges.sort(key=lambda e: e[2])
    
    ecount = 0
    total_cost = 0 

    for e in edges:
        uset = ds.find(e[0])
        vset = ds.find(e[1])

        # 사이클이 발생하지 않는 경우
        if uset != vset:
            ds.union(uset, vset)
            total_cost += e[2]
            ecount += 1
            
            # 선택된 간선이 n-1개가 되면 조기 종료
            if ecount == n - 1:
                break
                
    return total_cost


def solve():
    n = int(input())
    
    adj = []
    for _ in range(n):
        row = list(map(int, input().split()))
        adj.append(row)
    
    ans = kruskal(n, adj)
    print(ans)

if __name__ == '__main__':
    solve()