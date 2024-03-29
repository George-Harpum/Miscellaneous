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
