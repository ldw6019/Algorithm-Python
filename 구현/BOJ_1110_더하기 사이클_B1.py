"""
[문제] 백준 1110번 - 더하기 사이클
[링크] https://www.acmicpc.net/problem/1110
[분류] 구현
[난이도] B1
"""

import sys

# 입력 속도 최적화
input = sys.stdin.readline
def solve():
    n = int(input())
    first = n
    temp = n
    count = 0
    while(1):
        temp = (temp % 10) * 10 + ((temp // 10) + (temp % 10)) % 10
        count += 1
        if temp == first:
            break
    print(count)


if __name__ == "__main__":
    solve()