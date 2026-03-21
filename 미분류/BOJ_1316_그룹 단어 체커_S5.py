"""
[문제] 백준 1316번 - 그룹 단어 체커
[링크] https://www.acmicpc.net/problem/1316
[분류] 구현, 문자열
[난이도] S5
"""

import sys

# 입력 속도 최적화
input = sys.stdin.readline

def solve():
    words = []
    counts = 0
    n = int(input())
    for _ in range(n):
        words.append(input().strip())
    for word in words:
        compress = ""
        for char in word:
            if not compress or compress[-1] != char:
                compress += char
        if len(compress) == len(set(compress)):
            counts += 1
    print(counts)

if __name__ == "__main__":
    solve()