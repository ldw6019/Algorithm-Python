"""
[문제] 백준 1158번 - 요세푸스 문제
[링크] https://www.acmicpc.net/problem/1158
[분류] 자료 구조, 큐
[난이도] Silver 4 Tier
"""

# 입력 속도 최적화
import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    queue = list(range(1, n+1))
    result = []
    index = 0
    while(queue):
        index = (index + k - 1) % len(queue)
        result.append(queue.pop(index))
    print('<' + ', '.join(map(str, result)) + '>')
    

if __name__ == "__main__":
    solve()
