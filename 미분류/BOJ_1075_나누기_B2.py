"""
[문제] 백준 1075번 - 나누기
[링크] https://www.acmicpc.net/problem/1075
[분류] 수학, 브루트포스 알고리즘
[난이도] Bronze 2 Tier
"""

import sys

# 입력 속도 최적화
input = sys.stdin.readline

def solve():
    n = int(input())
    m = int(input())
    ans = []
    for i in range(100):
        if (n-n%100 + i) % m == 0:
            ans.append(i)
    temp = min(ans)
    if temp < 10:
        print("0"+str(temp))
    else: print(temp)

if __name__ == "__main__":
    solve()