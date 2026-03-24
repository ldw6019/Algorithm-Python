"""
[문제] 백준 문제번호1032번 - 명령 프롬포트
[링크] https://www.acmicpc.net/problem/1032
[분류] 알고리즘 분류
[난이도] B1   
"""
import sys
input = sys.stdin.readline

def solve():
    a = int(input())
    files = []

    for i in range(a):
        files.append(input().strip())
    
    result = []
    length = len(files[0])
    
    for i in range(length):
        is_same = True 
        
        for j in range(1, a): 
            if files[0][i] != files[j][i]:
                is_same = False 
                break
        
        if is_same:
            result.append(files[0][i])
        else:
            result.append('?')
            
    print("".join(result))

if __name__ == "__main__":
    solve()