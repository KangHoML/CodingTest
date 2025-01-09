def sol(record):
    info = {}
    
    for i, r in enumerate(record):
        line = r.split()
        name = None
        if len(line) == 3: act, uid, name = line
        else: act, uid = line
        
        # name 변경
        if name is not None:
            if info.get(uid): info[uid]["name"] = name
            else: info[uid] = {"name": name, "act": []}    

        # 활동 기록
        if act == "Enter": info[uid]["act"].append((i, "들어왔습니다."))
        elif act == "Leave": info[uid]["act"].append((i, "나갔습니다."))

    answer = [''] * len(record)
    
    for uid in info:
        name = info[uid]["name"]
        for idx, a in info[uid]["act"]:
            answer[idx] = f"{name}님이 {a}"
    
    answer = [i for i in answer if i]
    
    return answer

def sol2(record):
    info = {}
    
    for r in record:
        line = r.split()
        if line[0] != "Leave":
            _, uid, name = line
            info[uid] = name

    answer = []
    for r in record:
        line = r.split()
        if line[0] == "Enter": answer.append(f"{info[line[1]]}님이 들어왔습니다.")
        elif line[0] == "Leave": answer.append(f"{info[line[1]]}님이 나갔습니다.")
    
    return answer

if __name__ == "__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(sol(record))
