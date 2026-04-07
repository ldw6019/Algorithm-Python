"""
[문제] 백준 15650번 - N과 M (2)
[링크] https://www.acmicpc.net/problem/15650
[분류] 백트래킹
[난이도] Silver 3 Tier
"""

# 입력 속도 최적화
import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    arr = []
    def backtracking(start):
        if len(arr) == m:
            print(' '.join(map(str, arr)))
            return
        for i in range(start, n+1):
            arr.append(i)
            backtracking(i+1)
            arr.pop()
    backtracking(1)
    

if __name__ == "__main__":
    solve()