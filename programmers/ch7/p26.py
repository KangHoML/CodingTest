def sol(citations):
    citations.sort(reverse=True)
    
    for i, h in enumerate(citations):
        if i >= h: return i
            
    # 모든 논문의 인용 수가 n보다 많은 경우
    return len(citations)

if __name__ == "__main__":
    citations = [3, 0, 1, 6, 5]
    print(sol(citations))