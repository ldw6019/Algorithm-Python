"""
[문제] 백준 1074번 - Z
[링크] https://www.acmicpc.net/problem/1074
[분류] 분할 정복, 재귀
[난이도] Gold 5 Tier
"""

# 입력 속도 최적화
import sys
input = sys.stdin.readline

def solve(n, r, c):
    if n == 0: return 0
    
    half = 2**(n-1) # 한 변 길이의 절반
    
    # 1사분면 (좌상)
    if r < half and c < half:
        return solve(n-1, r, c)
    # 2사분면 (우상)
    elif r < half and c >= half:
        return (half**2) * 1 + solve(n-1, r, c - half)
    # 3사분면 (좌하)
    elif r >= half and c < half:
        return (half**2) * 2 + solve(n-1, r - half, c)
    # 4사분면 (우하)
    else:
        return (half**2) * 3 + solve(n-1, r - half, c - half)

if __name__ == "__main__":
    n, r, c = map(int, input().split())
    print(solve(n, r, c))