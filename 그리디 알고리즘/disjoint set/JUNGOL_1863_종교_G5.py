"""
[문제] 정올 1863번 - 종교
[링크] http://jungol.co.kr/problem/1863
[분류] disjoint set, 그래프 알고리즘
[난이도] Gold 5 Tier (Advanced)
"""

# 입력 속도 최적화
import sys
input = sys.stdin.readline

class DisjointSet:
    def __init__(self, n):
        self.parent = [-1] * n
        self.set_size = n

    def find(self, id):
        while (self.parent[id] >= 0):
            id = self.parent[id]
        return id
    
    def union(self, s1, s2):
        S1 = self.find(s1)
        S2 = self.find(s2)

        # 이미 같은 집합에 속해 있다면 합치지 않음
        if S1 == S2:
            return
        
        # 번호 작은 쪽을 루트로
        if S1 > S2: 
            S1, S2 = S2, S1
        self.parent[S2] = S1
        self.set_size -= 1
        
def solve():
    n, m = map(int, input().split())
    ds = DisjointSet(n)
    
    for _ in range(m):
        i, j = map(int, input().split())
        ds.union(ds.find(i - 1), ds.find(j - 1))

    print(ds.set_size)

if __name__ == "__main__":
    solve()