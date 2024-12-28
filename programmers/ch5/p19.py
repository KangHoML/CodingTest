import sys
sys.setrecursionlimit(10**6)

def checkin(result, n):
    if n not in result:
        result[n] = n + 1 # 빈 방이 가리킬 위치 업데이트
        return n

    # 처음 방이 가리킬 위치도 업데이트
    empty = checkin(result, result[n])
    result[n] = empty + 1
    return empty

def sol(k, room_number):
    result = {}

    for n in room_number:
        _ = checkin(result, n)

    return list(result)

def sol2(k, room_number):
    result = {}
    
    for n in room_number:
        empty = n
        visit = [empty]
        while empty in result:
            empty = result[empty]
            visit.append(empty) # 탐색하며 방문한 위치 기록
        
        # 방문한 번호들이 가리킬 위치 업데이트
        for v in visit: result[v] = empty + 1
    
    return list(result)


if __name__ == "__main__":
    k = 10
    room_number = [1,3,4,1,3,1]
    print(sol2(k, room_number))