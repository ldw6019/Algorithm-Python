"""
[문제] 백준 1010번 - 다리놓기
[링크] https://www.acmicpc.net/problem/1010
[분류] 알고리즘 분류
[난이도] S5
"""

import sys

# 입력 속도 최적화
input = sys.stdin.readline

def factorial(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] * i
    return dp[n]


def solve():
    n, m = map(int, input().split())
    print(factorial(m) // (factorial(n) * factorial(m - n)))
    
    #강 서쪽:n, 동쪽:m
    #핵심은 다리 개수는 mCn
    #nCr 의 공식은 n!/r!(n-r)! 
    
    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()