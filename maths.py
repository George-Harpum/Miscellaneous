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
