"""
[문제] 백준 2309번 - 일곱 난쟁이
[링크] https://www.acmicpc.net/problem/2309
[분류] 브루트포스 알고리즘
[난이도] Bronze 1 Tier
"""

# 입력 속도 최적화
import sys
input = sys.stdin.readline
from itertools import combinations

def solve():
    nums = [int(input()) for _ in range(9)]
    total = sum(nums)
    
    for combo in combinations(nums, 2):
        if sum(combo) == total - 100:
            
            nums.sort() 
            for n in nums:
                print(n)
            return 
    
if __name__ == "__main__":
    solve()