"""
[문제] 백준 1100번 - 하얀 칸
[링크] https://www.acmicpc.net/problem/1100
[분류] 구현
[난이도] B2
"""

import sys

# 입력 속도 최적화
input = sys.stdin.readline

def solve():
    board = [input().strip() for i in range(8)]
    count = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0 and board[i][j] == 'F':
                count += 1
    print(count)

if __name__ == "__main__":
    solve()