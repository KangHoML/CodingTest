import sys
sys.setrecursionlimit(2000)

def find_room(r, room_dic):
    if r not in room_dic:
        room_dic[r] = r + 1
        return r
    
    empty = find_room(room_dic[r], room_dic)
    room_dic[r] = empty + 1

    return empty

def recur(k, room_number):
    room_dic = dict()

    for r in room_number:
        _ = find_room(r, room_dic)
    
    return list(room_dic)

def nonrecur(k, room_number):
    room_dic = {}
    ans = []

    for r in room_number:
        n = r
        visited = [n] # 현재 빈 방 방문 처리

        while n in room_dic:
            n = room_dic[n] # 이미 존재하는 방인 경우, 다음 방으로 이동
            visited.append(n) 
        
        ans.append(n)

        # 다음 방 일괄 처리
        for v in visited:
            room_dic[v] = n + 1
    
    return ans
        
if __name__ == '__main__':
    print(recur(1e12, [1] * 200000))