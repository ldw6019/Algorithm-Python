import sys

def solve():
    # 문자열을 입력받고 양끝 공백/개행문자 제거
    s = sys.stdin.readline().strip()
    
    # 입력이 비어있을 경우를 대비한 방어 코드
    if not s:
        return

    total = 0
    x_index = -1

    # 1. 'x'의 위치를 찾고 나머지 숫자들의 가중치 합 구하기
    for i in range(13):
        if s[i] == 'x':
            x_index = i
        else:
            digit = int(s[i])
            # 1, 3, 1, 3... 순서로 곱해짐 (인덱스 0, 1, 2, 3...)
            if i % 2 == 0:
                total += digit * 1
            else:
                total += digit * 3
                
    # 2. 'x' 자리에 0~9를 대입하며 체크섬 확인
    # x가 위치한 인덱스의 가중치 결정
    multiplier = 1 if x_index % 2 == 0 else 3
    
    for num in range(10):
        # (기존 합 + x에 의한 합)이 10의 배수인지 확인
        if (total + (num * multiplier)) % 10 == 0:
            print(num)
            break

if __name__ == "__main__":
    solve() 