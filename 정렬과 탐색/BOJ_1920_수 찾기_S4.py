"""
[문제] 백준 문제번호1920번 - 수 찾기
[링크] https://www.acmicpc.net/problem/1920
[분류] 정렬, 이분 탐색
[난이도] Silver 4 Tier
"""

import sys

# 입력 속도 최적화
input = sys.stdin.readline

def solve():
    n = int(input())
    nlist = set(input().split())
    
    m = int(input())
    mlist = input().split()
    for num in mlist:
        if num in nlist:
            print(1)
        else:
            print(0)

if __name__ == "__main__":
    solve()