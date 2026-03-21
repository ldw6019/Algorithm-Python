"""
[문제] 백준 문제번호28702번 - FizzBuzz
[링크] https://www.acmicpc.net/problem/28702
[분류] 알고리즘 분류
[난이도] Bronze 1 Tier
"""

import sys

# 입력 속도 최적화
input = sys.stdin.readline

def fzbz(n):
    if n%3==0 and n%5==0:
        return "FizzBuzz"
    elif n%3==0:
        return "Fizz"
    elif n%5==0:
        return "Buzz"
    else:
        return str(n)
def solve():
    strings = [input().strip() for _ in range(3)]
    target = 0
    for i in range(3):
        if strings[i] not in ["Fizz", "Buzz", "FizzBuzz"]:
            target = int(strings[i]) + (3 - i)
            break
    result = fzbz(target)
    print(result)

if __name__ == "__main__":
    solve()