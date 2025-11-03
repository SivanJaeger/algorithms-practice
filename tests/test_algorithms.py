import random
from python.binary_search import binary_search
from python.sorting import quicksort

def test_quicksort_basic():
    arr = [3, 1, 2, 5, 4]
    assert quicksort(arr) == [1, 2, 3, 4, 5]

def test_quicksort_duplicates():
    arr = [5, 1, 5, 3, 3, 2]
    assert quicksort(arr) == [1, 2, 3, 3, 5, 5]

def test_binary_search_found():
    arr = [1, 2, 3, 4, 5, 6]
    assert binary_search(arr, 4) == 3

def test_binary_search_not_found():
    arr = [10, 20, 30]
    assert binary_search(arr, 25) == -1

def test_binary_search_random_sorted():
    # random data -> sort -> pick an element we know exists
    arr = sorted(random.sample(range(0, 100), 10))
    idx_target = len(arr) // 2
    target = arr[idx_target]
    assert binary_search(arr, target) == idx_target
