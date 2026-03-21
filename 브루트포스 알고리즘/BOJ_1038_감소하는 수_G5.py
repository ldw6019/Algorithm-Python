"""
[문제] 백준 1038번 - 감소하는 수
[링크] https://www.acmicpc.net/problem/1038
[분류] 브루트포스 알고리즘, 백트래킹
[난이도] Gold 5 Tier
"""

# 입력 속도 최적화
import sys
input = sys.stdin.readline
from itertools import combinations


def solve():
    n = int(input())
    # 감소하는 수의 최대값은 9876543210(10자리)
    # 감소한는 수의 개수: 10C1 + 10C2 + 10C3 + ...... 10C9 + 10C10
    # 그거 구하는 공식은 2**n - 1. 그러므로 감소하는 수의 총 개수는 1023
    max = 1023
    numbers = []
    if n >= max:
        print('-1')
        return
    
    def dfs(current_num, last_digit):
        numbers.append(current_num)
    
        for next_digit in range(last_digit):
            new_num = current_num * 10 + next_digit
            dfs(new_num, next_digit)
    for i in range(10):
        dfs(i, i)
    numbers.sort()
    print(numbers[n])
    

if __name__ == "__main__":
    solve()