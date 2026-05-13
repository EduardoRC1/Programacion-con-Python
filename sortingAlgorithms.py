# Implementacion de algoritmos de ordenamiento clasicos
import random
import time

def bubble_sort(arr):
    """Ordena una lista usando Bubble Sort."""
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def selection_sort(arr):
    """Ordena una lista usando Selection Sort."""
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def insertion_sort(arr):
    """Ordena una lista usando Insertion Sort."""
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def merge_sort(arr):
    """Ordena una lista usando Merge Sort."""
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def benchmark(sort_func, arr, name):
    """Mide el tiempo de ejecucion de un algoritmo de ordenamiento."""
    start = time.time()
    result = sort_func(arr)
    elapsed = time.time() - start
    print(f"  {name:<20} {elapsed:.6f}s")
    return result

# Generar lista aleatoria
size = 1000
data = [random.randint(1, 10000) for _ in range(size)]

print(f"Sorting {size} random numbers:\n")

sorted_bubble = benchmark(bubble_sort, data, "Bubble Sort")
sorted_selection = benchmark(selection_sort, data, "Selection Sort")
sorted_insertion = benchmark(insertion_sort, data, "Insertion Sort")
sorted_merge = benchmark(merge_sort, data, "Merge Sort")

# Verificar que todos producen el mismo resultado
expected = sorted(data)
all_correct = (
    sorted_bubble == expected
    and sorted_selection == expected
    and sorted_insertion == expected
    and sorted_merge == expected
)
print(f"\nAll algorithms produced correct results: {all_correct}")
