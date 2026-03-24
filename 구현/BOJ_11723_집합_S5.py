"""
[문제] 백준 11723번 - 집합
[링크] https://www.acmicpc.net/problem/11723
[분류] 자료 구조, 비트마스크
[난이도] Silver 5 Tier
"""

# 입력 속도 최적화
import sys
input = sys.stdin.readline

def solve():
    S = [0] * 21
    m = int(input())
    for _ in range(m):
        line = input().split()
        temp = line[0]
        if temp == 'add':
            S[int(line[1])] = 1
        elif temp == 'remove':
            S[int(line[1])] = 0
        elif temp == 'check':
            print(S[int(line[1])])
        elif temp == 'toggle':
            S[int(line[1])] = 1 - S[int(line[1])]
        elif temp == 'all':
            S = [1] * 21
        elif temp == 'empty':
            S = [0] * 21
        else:
            print('error')
            break

if __name__ == "__main__":
    solve()