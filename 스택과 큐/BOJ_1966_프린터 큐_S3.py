"""
[문제] 백준 1966번 - 프린터 큐
[링크] https://www.acmicpc.net/problem/1966
[분류] 자료 구조, 큐
[난이도] Silver 3 Tier
"""
import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    # 중요도만 담긴 큐
    queue = deque(list(map(int, input().split())))
    
    count = 0
    while queue:
        # 1. 가장 앞의 중요도 확인
        current = queue.popleft()
        
        # 2. 현재 문서보다 높은 중요도가 있는지 확인
        if any(current < item for item in queue):
            # 더 높은게 있다면 뒤로 보냄
            queue.append(current)
            
            # 여기서 핵심! M의 위치를 조정합니다.
            if m == 0:
                m = len(queue) - 1 # 맨 앞으로 왔던 내 문서가 맨 뒤로 감
            else:
                m -= 1 # 내 문서가 한 칸 앞으로 당겨짐
        else:
            # 3. 인쇄하기
            count += 1
            if m == 0: # 지금 인쇄하는게 내가 찾던 문서라면
                print(count)
                break
            else:
                m -= 1 # 내 문서가 한 칸 앞으로 당겨짐

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()