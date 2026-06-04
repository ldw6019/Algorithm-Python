"""
[문제] 정올 1278번 - 가방채우기2
[링크] http://www.jungol.co.kr/problem.php?id=1278
[분류] 배낭 문제, DP
[난이도] Intermediate Tier
"""

# 입력 속도 최적화
import sys
input = sys.stdin.readline

def solve():
    # n: 보석 개수, w: 가방 용량
    n, w = map(int, input().split())
    gems = []

    for _ in range(n):
        wi, pi = map(int, input().split())
        # [2 40], [5 110]같은 형태로 저장[무게, 가치]
        gems.append([wi, pi])
    
    dp = [[0] * (w + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        # 현재 보석의 무게와 가치
        wi, pi = gems[i-1]
        for j in range(w + 1):
            # 현재 보석을 선택하지 않는 경우의 최대 가치
            dp[i][j] = dp[i-1][j]

            if j >= wi:
                # 현재 보석을 선택하는 경우의 최대 가치(이전 보석까지의 최대 가치 + 현재 보석의 가치)
                dp[i][j] = max(dp[i][j], dp[i-1][j-wi] + pi)
    print(dp[n][w])

if __name__ == "__main__":
    solve()