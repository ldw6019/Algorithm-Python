"""
[문제] 백준 10816번 - 숫자 카드 2   
[링크] https://www.acmicpc.net/problem/10816
[분류] 정렬, 이분 탐색
[난이도] Silver 4 Tier
"""

# 입력 속도 최적화
import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

def solve():
    n = int(input())
    cards = list(map(int, input().split()))
    cards.sort()
    m = int(input())
    needs = list(map(int, input().split()))
    result = []
    for i in range(m):
        x = needs[i]
        low = bisect_left(cards, x)
        high = bisect_right(cards, x)
        diff = high - low
        result.append(diff)
    print(' '.join(map(str, result))) # join문 출력을 위해 str 변환

if __name__ == "__main__":
    solve()