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
            # 길이가 m에 도달하면 띄어쓰기로 구분해 출력
            print(' '.join(map(str, arr)))
            return
        
        for i in range(start, n + 1):
            arr.append(i)
            # 다음 숫자는 현재 숫자보다 큰 숫자부터 시작
            backtracking(i + 1)
            arr.pop()

    backtracking(1)

if __name__ == "__main__":
    solve()