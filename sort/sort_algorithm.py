import sys
input = sys.stdin.readline

'''
선택 정렬
    - Worst Case : O(N^2)
    - Best Case : O(N^2)
'''
def select_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                arr[j], arr[min_idx] = arr[min_idx], arr[j]

'''
삽입 정렬
    - Worst Case : O(N^2)
    - Best Case(이미 정렬되어 있는 경우) : O(N)
'''
def insert_sort(arr):
    n = len(arr)
    key_idx = 0
    for i in range(1, n):
        key = arr[i]
        
        for j in range(i-1, -1, -1):
            if arr[j] > key:
                arr[j+1] = arr[j]
            else:
                key_idx = j
                break
        
        arr[key_idx] = key


'''
버블 정렬
    - Worst Case : O(N^2)
    - Best Case(이미 정렬되어 있는 경우) : O(N)
'''
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

'''
병합 정렬 (O(N)의 추가 메모리 필요)
    - Worst Case : O(NlogN)
    - Best Case : O(NlogN)
'''
def merge_sort(arr):
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            merge_sort(left)
            merge_sort(right)

            merge(arr, left, right)

    def merge(arr, left, right):
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    merge_sort(arr)
        
def main():
    arr = [i for i in range(5, 0, -1)]
    merge_sort(arr)
    print(arr)

if __name__ == "__main__":
    main()

# 힙
# 퀵
# 트리
    

        