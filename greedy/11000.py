import sys
import heapq # 이진 트리 기반 최소 힙 자료구조
input = sys.stdin.readline

def main():
    n = int(input())
    lecture = []
    
    for _ in range(n):
        s, t = map(int, input().split())
        lecture.append([s, t])
    lecture.sort()

    room = []
    heapq.heappush(room, lecture[0][1]) # 첫 번째 강의의 종료 시간
    
    for i in range(1, n):
        if lecture[i][0] < room[0]: # 현재 강의 종료 시간 > 다음 강의 시작 시간
            heapq.heappush(room, lecture[i][1]) # 새로운 회의실 개설
        else:
            heapq.heappop(room) # 새로운 회의 시간 변경을 위해 현재 강의 종료 시간 pop
            heapq.heappush(room, lecture[i][1])

    print(len(room))

if __name__ == "__main__":
    main()