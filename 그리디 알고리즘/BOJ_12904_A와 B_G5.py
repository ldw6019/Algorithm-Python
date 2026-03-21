"""
[문제] 백준 문제번호12904번 - A와 B
[링크] https://www.acmicpc.net/problem/12904
[분류] 그리디 알고리즘
[난이도] Gold 5 Tier
"""

import sys

# 입력 속도 최적화
input = sys.stdin.readline

def solve():
    s = list(input().rstrip())
    t = list(input().rstrip())
    
    while len(s) < len(t):
        last = t.pop()
        if last == 'A':
            pass
        else:
            t.reverse()
    if s == t:
        print(1)
    else: print(0)

if __name__ == "__main__":
    solve()