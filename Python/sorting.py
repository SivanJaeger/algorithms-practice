from typing import List, Any

def quicksort(a: List[Any]) -> List[Any]:
    """
    Minimal quicksort (functional style).
    Average: O(n log n), Worst: O(n^2)
    """
    if len(a) < 2:
        return a
    pivot = a[len(a) // 2]
    left  = [x for x in a if x < pivot]
    mid   = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return quicksort(left) + mid + quicksort(right)
