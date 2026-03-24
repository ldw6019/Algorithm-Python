"""
[문제] 백준 15829번 - 해싱
[링크] https://www.acmicpc.net/problem/15829
[분류] 구현, 문자열, 해싱
[난이도] Bronze 2 Tier
"""

# 입력 속도 최적화
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    M = 1234567891
    result = 0
    word = []
    word = input().strip()
    alen = len(word)
    for i in range(alen):
        y = ord(word[i]) - 96
        result += (y * 31**i) % M
    print(int(result)%M)


if __name__ == "__main__":
    solve()