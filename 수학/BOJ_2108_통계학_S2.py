"""
[문제] 백준 2108번 - 통계학
[링크] https://www.acmicpc.net/problem/2108
[분류] 수학, 구현, 정렬
[난이도] Silver 2 Tier
"""

# 입력 속도 최적화
import sys
input = sys.stdin.readline

def round_fx(n):
    if n >= 0:
        return int(n + 0.5)
    else:
        # 음수일 때는 0.5를 빼서 더 작은 쪽으로 보낸 뒤 int()
        return int(n - 0.5)
    
#최빈값 계산 함수    
def frequency(nums):
    if len(nums) == 1:
        return nums[0]
    count = 1
    max = 0
    modes = []
    for i in range(len(nums) - 1): 
        if nums[i] == nums[i+1]: # 숫자가 같은 케이스
            count += 1
        else: # 숫자가 바뀐 케이스
            if count > max:
                max = count
                modes.clear()
                modes.append(nums[i])
                count = 1 #count 초기화

            elif count == max:
                modes.append(nums[i])
                count = 1 #count 초기화
            else: 
                count = 1 #count 초기화 
    if count > max:
        modes = [nums[-1]]
    elif count == max:
        modes.append(nums[-1])
    return modes[1] if len(modes) > 1 else modes[0]

def solve():
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    nums.sort()
    print(round_fx(sum(nums)/n))
    print(nums[n//2])
    freq = frequency(nums)
    print(freq)
    print(nums[-1] - nums[0])
    

if __name__ == "__main__":
    solve()