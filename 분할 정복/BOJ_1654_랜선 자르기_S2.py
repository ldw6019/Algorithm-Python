"""
[문제] 백준 1654번 - 랜선 자르기
[링크] https://www.acmicpc.net/problem/1654
[분류] 이분 탐색
[난이도] Silver 2Tier
"""

# 입력 속도 최적화
import sys
input = sys.stdin.readline

def solve():
    k, n  = map(int, input().split())
    lan = [int(input()) for _ in range(k)]
    left, right = 1, max(lan)
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        count = 0
        for x in lan:
            count += x // mid

            if count >= n:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
    print(result)

if __name__ == "__main__":
    solve()