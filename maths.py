"""
Maths-based functions implemented in python. 
(Not intended to be used practically, but proof of concept).
"""
from typing import Any


def type_check(var: Any, *types: Any) -> None | Exception:
  if type(var) not in types:
    raise TypeError(f"{var} must be in types: {types}, not {type(var)}")


def sqrt(n: int | float, iters:int=10) -> float | Exception:
  type_check(n, *(int, float))
  complex_tag = None
  if n < 0:
    n = abs(n)
    complex_tag = True
  x = n/2
  y = x
  for i in range(iters):
    x -= ((x*x)-n)/(2*x)
    if x == y:
      break
    y = x
  if complex_tag:
    return complex(0, x)
  return x

def factorial(n: int) -> int | Exception:
  """Factorial, n! = Π{i=1, n} i
  or: n * (n-1) * (n-2) * ... * 2 * 1
  e.g. 5! = 5 x 4 x 3 x 2 x 1 = 120
  Domain: n ∈ N+
  """
  type_check(n, int)
  if n < 0:
    raise ValueError("Factorial of a negative number requires the Gamma Function")
  for i in range(2, n):
    n *= i
  return n
