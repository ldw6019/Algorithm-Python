"""
[문제] 백준 15650번 - N과 M (2)
[링크] https://www.acmicpc.net/problem/15650
[분류] 백트래킹
[난이도] Silver 3 Tier
"""

# 입력 속도 최적화
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5) # 재귀 깊이 제한 늘리기

def solve():
    n, m = map(int, input().split())
    arr = []
    def backtracking():
        if len(arr) == m:
            print(' '.join(map(str, arr)))
            return
        for i in range(1, n+1):
            if i not in arr:
                arr.append(i)
                backtracking()
                arr.pop()
    backtracking()
    

if __name__ == "__main__":
    solve()

    