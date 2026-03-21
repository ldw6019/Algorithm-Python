"""
[문제] 백준 2163번 - 초콜릿 자르기
[링크] https://www.acmicpc.net/problem/2163
[분류] 수학, 사칙연산
[난이도] Bronze 3 Tier`
"""

import sys

# 입력 속도 최적화
input = sys.stdin.readline

def solve():
    # 입력 받기 (N, M)
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n, m = map(int, line.split())
        
        # 공식 적용: N * M - 1
        print(n * m - 1)
    except ValueError:
        pass    

if __name__ == "__main__":
    solve()
