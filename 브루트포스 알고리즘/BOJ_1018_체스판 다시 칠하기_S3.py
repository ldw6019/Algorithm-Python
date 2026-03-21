"""
[문제] 백준 1018번 - 체스판 다시 칠하기
[링크] https://www.acmicpc.net/problem/1018
[분류] 구현, 브루트포스
[난이도] S3
"""

import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    board = [input().strip() for _ in range(n)]
    
    repair_counts = []

    # 1. 8x8 크기로 자를 수 있는 모든 시작 지점 탐색
    for i in range(n - 7):
        for j in range(m - 7):
            draw1 = 0 # 'W'로 시작하는 경우
            draw2 = 0 # 'B'로 시작하는 경우
            
            # 2. 해당 시작 지점부터 8x8 영역 탐색
            for a in range(i, i + 8):
                for b in range(j, j + 8):
                    # 체스판의 인덱스 합이 짝수/홀수임에 따라 색이 결정됨
                    if (a + b) % 2 == 0:
                        if board[a][b] != 'W':
                            draw1 += 1
                        if board[a][b] != 'B':
                            draw2 += 1
                    else:
                        if board[a][b] != 'B':
                            draw1 += 1
                        if board[a][b] != 'W':
                            draw2 += 1
            
            # 두 경우 중 최솟값을 리스트에 저장
            repair_counts.append(draw1)
            repair_counts.append(draw2)

    # 3. 모든 경우의 수 중 가장 작은 값 출력
    print(min(repair_counts))

if __name__ == "__main__":
    solve()