def sol(participant, completion):
    name_table = {}
    
    for p in participant:
        name_table[p] = name_table.get(p, 0) + 1
    
    for c in completion:
        name_table[c] -= 1
    
    for n in name_table:
        if name_table[n]: return n

if __name__ == "__main__":
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    print(sol(participant, completion))