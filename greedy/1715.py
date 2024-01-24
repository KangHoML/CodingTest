import sys
import heapq
input = sys.stdin.readline

def main():
    n = int(input())
    card = []
    for _ in range(n):
        heapq.heappush(card, int(input()))

    result = 0
    while len(card) > 1:
        prev = heapq.heappop(card)
        current = heapq.heappop(card)
        result += (prev + current)
        heapq.heappush(card, prev + current)

    print(result)

if __name__ == "__main__":
    main()
