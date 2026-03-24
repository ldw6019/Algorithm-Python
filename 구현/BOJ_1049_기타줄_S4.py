"""
[문제] 백준 문제번호1049번 - 기타줄
[링크] https://www.acmicpc.net/problem/1049
[분류] 알고리즘 분류
[난이도] S4
"""

import sys
# 입력 속도 최적화
input = sys.stdin.readline


def solve():
    n, m = map(int, input().split())
    
    min6 = 1001
    min1 = 1001

    for i in range(m):
        p, s = map(int, input().split())
        if p < min6: min6 = p
        if s < min1: min1 = s

    # 전부 낱개로 구매
    case1 = n * min1
    # 패키지 + 낱개 
    case2 = (n // 6) * min6 + (n % 6) * min1
    # 전부 패키지
    case3 = (n // 6 + 1) * min6

    print(min(case1, case2, case3))
    

if __name__ == "__main__":
    solve()