"""
[문제] 백준 14916번 - 거스름돈
[링크] https://www.acmicpc.net/problem/14916
[분류] 동적 프로그래밍, 그리디 알고리즘, 수학
[난이도] Silver 5 Tier
"""

# 입력 속도 최적화
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    count = 0
    while(1):
        if n==1 or n==3:
            print("-1")
            break
        elif (n%5 != 0):
            n -= 2
            count += 1
        elif (n%5 == 0):
            temp = n/5
            count += temp
            print(int(count))
            break
        if n == 0:
            print(int(count))
            break

if __name__ == "__main__":
    solve()