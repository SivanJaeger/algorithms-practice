from typing import List, Any

def binary_search(arr: List[Any], target: Any) -> int:
    """
    Iterative binary search.
    :param arr: sorted list
    :param target: element to find
    :return: index if found, else -1
    """
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
