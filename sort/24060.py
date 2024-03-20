import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def merge(arr, left, right):
    i, j, k = 0, 0, 0
    global cnt
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        
        cnt += 1
        if cnt == m:
            print(arr[k])

        k += 1

    while i < len(left):
        arr[k] = left[i]

        cnt += 1
        if cnt == m:
            print(arr[k])

        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        
        cnt += 1
        if cnt == m:
            print(arr[k])

        j += 1
        k += 1

def merge_sort(arr):
    if len(arr) > 1:
        mid = (len(arr) + 1) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)
        merge(arr, left, right)

def main():
    global n, m, cnt
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    cnt = 0
    merge_sort(arr)
    if cnt < m:
        print(-1)
        
if __name__ == "__main__":
    main()