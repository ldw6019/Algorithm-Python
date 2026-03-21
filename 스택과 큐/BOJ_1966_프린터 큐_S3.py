"""
[문제] 백준 1966번 - 프린터 큐
[링크] https://www.acmicpc.net/problem/1966
[분류] 자료 구조, 큐
[난이도] Silver 3 Tier
"""

# 입력 속도 최적화
import sys
input = sys.stdin.readline
from collections import deque

def solve():
    x = int(input())
    for _ in range(x):
        n, m = map(int(input()).split)
    


    '''
1. 테스트 케이스 수만큼 반복
2. N, M과 중요도 리스트를 입력받음
3. 큐에 (중요도, 원래_인덱스) 형태로 저장
4. 인쇄 횟수 count = 0
5. 큐가 빌 때까지 반복:
    - 현재 맨 앞 문서가 큐 안에서 중요도가 가장 높은가?
    - YES: 
        - 인쇄한다 (count + 1)
        - 만약 이 문서의 인덱스가 M이라면? -> count 출력 후 종료
    - NO:
        - 맨 앞 문서를 꺼내서 맨 뒤로 다시 넣는다'''
    
if __name__ == "__main__":
    solve()