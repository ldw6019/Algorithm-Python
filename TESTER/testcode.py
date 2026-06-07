input_data = """7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
"""

lines = input_data.strip().split('\n')

n, m = map(int, lines[0].split())
edges = []
parent = [i for i in range(n)]  # 1,2,3 노드를 -> 0,1,2로 저장할 예정

line_idx = 1
for _ in range(m):
    a, b, w = map(int, lines[line_idx].split())
    line_idx += 1
    edges.append((w, a - 1, b - 1))  # 1,2,3 노드를 -> 0,1,2로 저장할 예정

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])  # find 거슬러 올라가면서 parent[x] 값도 갱신
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:  # 작은 쪽을 부모로 통일
        parent[b] = a
    else:
        parent[a] = b

edges.sort(key=lambda x: x[0])  # 0번째 인덱스에 있는 w(가중치) 기준으로 오름차순 정렬
cnt = 0  # 연결한 엣지수
i = 0
cost = 0  # 총 비용

while cnt < n - 2:  # n-1 하면 모든 노드가 연결된다.
    w, a, b = edges[i][0], edges[i][1], edges[i][2]
    if find(a) != find(b):
        cnt += 1
        cost += w
        union(a, b)
    i += 1

print(cost)