def total(lst):
    cnt = 0
    for i, v in lst: cnt += v
    return cnt

def sol(genres, plays):
    table = {}
    for i in range(len(genres)):
        g, p = genres[i], plays[i]
         
        if table.get(g): table[g].append((i, p))
        else: table[g] = [(i, p)]
    
    tlst = sorted(table.items(), key=lambda x: -total(x[1]))
    answer = []
    for g, lst in tlst:
        if len(lst) < 2: answer.append(lst[0][0]); continue
        
        lst.sort(key=lambda x: (-x[1], x[0]))
        answer.append(lst[0][0])
        answer.append(lst[1][0])
    
    return answer

def sol2(genres, plays):
    d1, d2 = {}, {}

    for i in range(len(genres)):
        g, p = genres[i], plays[i]

        if d1.get(g): d1[g].append((i, p))
        else: d1[g] = [(i, p)]

        d2[g] = d2.get(g, 0) + p
    
    answer = []
    for genre, _ in sorted(d2.items(), key=lambda x: -x[1]):
        for i, _ in sorted(d1[genre], key=lambda x: (-x[1], x[0]))[:2]:
            answer.append(i)

    return answer

if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    print(sol2(genres, plays))
