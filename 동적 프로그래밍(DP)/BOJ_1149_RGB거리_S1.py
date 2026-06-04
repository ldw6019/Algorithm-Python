def min_cost(n, cost):
    dp = [[0] * 3 for _ in range(n)]

    # 첫 번째 집에 대한 초기값 설정
    for i in range(3):
        dp[0][i] = cost[0][i]

    # 두 번째 집부터 DP 배열 채우기
    for i in range(1, n):
        dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])

    # 마지막 집까지의 최소 비용 반환
    return min(dp[n-1][0], dp[n-1][1], dp[n-1][2])

def solve():
    n = int(input())
    cost = []

    for _ in range(n):
        r, g, b = map(int, input().split())
        cost.append([r, g, b])

    result = min_cost(n, cost)
    print(result)

if __name__ == "__main__":
    solve()

