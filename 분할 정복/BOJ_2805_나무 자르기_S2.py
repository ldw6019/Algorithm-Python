"""
[문제] 백준 2805번 - 나무 자르기
[링크] https://www.acmicpc.net/problem/2805
[분류] 이분 탐색
[난이도] Silver 2Tier
"""

# 입력 속도 최적화
import sys
input = sys.stdin.readline

def solve():
    # k: 나무의 수, n: 필요한 나무 길이
    n, m = map(int, sys.stdin.readline().split())
    # 나무 높이들 (한 줄에 공백으로 구분되어 들어옴)
    woods = list(map(int, sys.stdin.readline().split()))
    
    left, right = 0, max(woods)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        total = 0
        
        # woods 순회
        for i in range(n):
            if woods[i] > mid:
                total += woods[i] - mid
            
            # m만큼 모았으면 즉시 탈출 (가장 효율적인 지점)
            if total >= m:
                break
        
        if total >= m:
            result = mid    # '합격'한 절단기 높이 저장
            left = mid + 1  # 더 높은 높이가 있는지 탐색
        else:
            right = mid - 1 # 나무가 모자라니 높이를 낮춤

    print(result)

if __name__ == "__main__":
    solve()