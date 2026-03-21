"""
[문제] 백준 문제번호1065번 - 한수
[링크] https://www.acmicpc.net/problem/1065
[분류] 알고리즘 분류
[난이도] Silver 4 Tier
"""

import sys

# 입력 속도 최적화
input = sys.stdin.readline

def solve():
    n = int(input())
    if n < 100: print(n)
    else:
        count = 99
        for i in range(100, n+1):
            if (i//100 - i//10%10) == (i//10%10 - i%10):
                count += 1
        print(count)
    # 문제의 핵심 아이디어를 메모하세요
    

if __name__ == "__main__":
    solve()