"""
백준 1034. 램프
- 켤 수 있는 행에 대해 초기 상태가 동일한 것의 개수의 최대값을 반환
- 아래 두 가지 조건을 만족할 경우 켤 수 있는 행
    - 각 행의 0의 개수를 2로 나눈 나머지와 k를 2로 나눈 나머지가 동일한가
    - 행에 있는 0의 개수가 k 이하인가  
"""

def main():
    N, _ = map(int, input().split())
    state = [input() for i in range(N)]
    k = int(input())
    num_lamps_on = []

    for i in range(N):
        count = 0
        zeros = state[i].count('0')

        if (k % 2) == (zeros % 2) and zeros <= k:
            for j in range(N):
                    if state[i] == state[j]:
                        count += 1
        num_lamps_on.append(count)
    
    print(max(num_lamps_on))

if __name__ == "__main__":
    main()