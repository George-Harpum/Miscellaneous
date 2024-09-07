"""
Algorithms and functions related more to coding than maths.
"""

def sieve_of_eratosthenes(upper_limit: int) -> list[int] | Exception:
  """Find all prime numbers in between 0 and upper_limit.
  Domain: upper_limit ∈ N+"""
  if upper_limit < 0:
    raise ValueError("upper limit must be ∈ N+ (A positive integer)")
  if upper_limit == 1:
    return []
  if upper_limit == 2:
    return [2]
  arr_bool = [False, False]
  arr_bool += [True]*(upper_limit - 1)
  i = 2
  while i*i < upper_limit:
    if arr_bool[i] is True:
      for j in range(i*i, upper_limit+1, i):
        arr_bool[j] = False
    i += 1
  return [x for x, y in enumerate(arr_bool) if y is True]


def binary_search(target: int, array: list[int]):
  lower = 0
  upper = len(array) - 1
  while lower <= upper:
    mid = ((upper - lower)//2) + lower
    if (search := array[mid]) < target:
      lower = mid+1
    elif search > target:
      upper = mid-1
    else:
      return mid
  else:
    raise ValueError(f"The item ({target}) cannot be found within array")


# Sorting Algorithms
def bubble_sort(arr: list[int]) -> list[int]:
  swap = True
  while swap:
    swap = False
    for i in range(2, len(arr)):
      if arr[i-1] > arr[i]:
        arr[i-1], arr[i] = arr[i], arr[i-1]
        swap = True
  return arr


def quicksort(arr: list, low, high) -> list:
  if low < high:
    part = quicksort_helper(arr, low, high)
    quicksort(arr, low, part-1)
    quicksort(arr, part+1, high)
  return arr

def quicksort_helper(arr, low, high):
  pivot = arr[high]
  for i in range(low, high):
    if arr[i] < pivot:
      arr[i], arr[low] = arr[low], arr[i]
      low += 1
  arr[low], arr[high] = arr[high], arr[low]
  return low


def merge_helper(left, right):
  lleft = len(left)
  lright = len(right)
  out = [0]*(lleft + lright)
  i, j = 0, 0
  idx = 0
  while i < lleft and j < lright:
    if left[i] <= right[j]:
      out[idx] = left[i]
      i += 1
    else:
      out[idx] = right[j]
      j += 1
    idx += 1
  while i < lleft:
    out[idx] = left[i]
    i += 1
    idx += 1
  while j < lright:
    out[idx] = right[j]
    j += 1
    idx += 1
  return out


def mergesort(arr: list) -> list:
  if (l:=len(arr)) < 2:
    return arr
  left = arr[:l//2]
  right = arr[l//2:]
  a = mergesort(left)
  b = mergesort(right)
  return merge_helper(a, b)

def insertion_sort(arr):
  for i in range(arr):
    while i > 0 and arr[i-1] > arr[i]:
      arr[i-1], arr[i] = arr[i], arr[i-1]
      i -= 1
  return arr


def selection_sort(arr):
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      if arr[j] < arr[i]:
        arr[i], arr[j] = arr[j], arr[i]
  return arr

