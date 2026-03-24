"""
[문제] 백준 11053번 - 가장 긴 증가하는 부분 수열
[링크] https://www.acmicpc.net/problem/11053
[분류] 동적 프로그래밍
[난이도] Silver 2 Tier
"""

# 입력 속도 최적화
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))


if __name__ == "__main__":
    solve()