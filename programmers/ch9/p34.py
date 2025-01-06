def sol(phone_book):
    tbl = {}
    for p in phone_book:
        # 이미 있음
        if tbl.get(p): return False
        tbl[p] = 1
    
    for n in tbl:
        for i in range(len(n) - 1):
            if tbl.get(n[:i+1]): return False
    
    return True

def sol2(phone_book):
    phone_book.sort()

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1): return False
    
    return True
    
if __name__ == "__main__":
    phone_book = ["119", "97674223", "1195524421"]
    print(sol2(phone_book))