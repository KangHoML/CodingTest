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
    def _merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            _merge_sort(left)
            _merge_sort(right)

            _merge(arr, left, right)

    def _merge(arr, left, right):
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

    _merge_sort(arr)

'''
퀵 정렬
    - Worst Case(이미 정렬되어 있는 경우): O(N^2)
    - Best Case: O(NlogN)
'''
def quick_sort(arr):
    def _quick_sort(low, high):
        if high > low:
            mid = _partition(low, high)
            _quick_sort(low, mid-1)
            _quick_sort(mid, high)

    def _partition(low, high):
        pivot = arr[(low + high)//2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    _quick_sort(0, len(arr) -1)

'''
힙 정렬
    - Worst Case : O(NlogN)
    - Best Case : O(NlogN)
'''

def heap_sort(arr):
    def _max_heapify(arr):
        parent = len(arr) // 2 - 1
        for current in range(parent, -1, -1):
            while current <= parent:
                child_left = current * 2 + 1
                child_right = child_left + 1

                #  leaf node 중 큰 값 찾기
                if child_right < len(arr) and arr[child_left] < arr[child_right]:
                    child_left = child_right
                
                # leaf node가 root node보다 클 경우, 교환
                if arr[current] < arr[child_left]:
                    arr[current], arr[child_left] = arr[child_left], arr[current]    
                    current = child_left
                else:
                    break
                
    def _heappop(heap, end_idx):
        # 최상위 노드와 최하위 노드를 교환
        heap[end_idx], heap[0] = heap[0], heap[end_idx]
        current, child_left = 0, 1

        # 마지막 요소를 새로운 루트로 설정하여 heapify 수행
        while child_left < end_idx:
            child_right = child_left + 1
            if child_right < end_idx and heap[child_left] < heap[child_right]:
                    child_left = child_right
            
            if heap[current] < heap[child_left]:
                heap[current], heap[child_left] = heap[child_left], heap[current]
                current = child_left
                child_left = current * 2 + 1
            else:
                break
    
    _max_heapify(arr)
    for end_idx in range(len(arr)-1, 0, -1):
        _heappop(arr, end_idx)


def main():
    arr = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    heap_sort(arr)
    print(arr)

if __name__ == "__main__":
    main()

# 힙    