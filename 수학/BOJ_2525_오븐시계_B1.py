"""
[문제] 백준 2525번 - 오븐 시계
[링크] https://www.acmicpc.net/problem/2525
[분류] 수학, 사칙연산
[난이도] Bronze 1 Tier
"""

import sys

# 입력 속도 최적화
input = sys.stdin.readline

def solve():
    n, m = map(int, sys.stdin.readline().split())
    x = int(sys.stdin.readline())

    total = (n * 60 + m + x) % (24 * 60)
    print(total // 60, total % 60)    

if __name__ == "__main__":
    solve()