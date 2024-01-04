"""
11000. 강의실 배정
1. (Si, Ti)에 대해 Si에 따라 오름차순 정렬
2. 각각에 대한 배열 생성
3. Ti 배열 값 중 Si에 없는 값일 경우에만 count
"""
import time

def main():
    N = int(input())
    lecture = [map(int, input().split()) for _ in range(N)]
    


    
if __name__ == "__main__":
    start = time.time()
    main()
    print(f"{time.time() - start}s")