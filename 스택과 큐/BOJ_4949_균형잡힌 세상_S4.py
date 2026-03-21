"""
[문제] 백준 문제번호4949번 - 균형잡힌 세상
[링크] https://www.acmicpc.net/problem/4949
[분류] 알고리즘 분류
[난이도] Silver 4 Tier
"""

import sys
input = sys.stdin.readline

def solve():
    while True:
        line = input().rstrip()
        
        if line == ".":
            break
            
        stack = []
        is_balanced = True
        
        for char in line:
            if char == '(' or char == '[':
                stack.append(char)
                
            elif char == ')':
                if not stack or stack[-1] != '(':
                    is_balanced = False
                    break
                stack.pop()
                
            elif char == ']':
                if not stack or stack[-1] != '[':
                    is_balanced = False
                    break
                stack.pop()
        
        if is_balanced and not stack:
            print("yes")
        else:
            print("no")

if __name__ == "__main__":
    solve()