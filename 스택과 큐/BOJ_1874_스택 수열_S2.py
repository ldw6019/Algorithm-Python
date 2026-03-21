"""
[문제] 백준 1874번 - 스택 수열
[링크] https://www.acmicpc.net/problem/1874
[분류] 자료 구조, 스택
[난이도] Silver 2 Tier
"""

# 입력 속도 최적화
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    target = [int(input()) for _ in range(n)]
    stack = []
    result = []
    current = 1
    possible = True
    for n in target:
        while current <= n:
            stack.append(current)
            result.append('+')
            current += 1
        if stack[-1] == n:
            stack.pop()
            result.append('-')
            pass
        else:
            print("NO")
            possible = False
            break
    if possible:
        print("\n".join(result))
    
if __name__ == "__main__":
    solve()