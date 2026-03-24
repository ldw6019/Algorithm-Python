"""
[문제] 백준 1193번 - 분수찾기
[링크] https://www.acmicpc.net/problem/1193
[분류] 구현, 수학
[난이도] Silver 5 Tier
"""

# 입력 속도 최적화
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    line = 1
    result = 0
    while(n > line):
        n -= line
        line += 1
    if (line%2 == 0):
        print(n,"/",line-n+1,sep="")
    elif (line%2 != 0):
        print(line+1-n,"/",n,sep="")
        

if __name__ == "__main__":
    solve()