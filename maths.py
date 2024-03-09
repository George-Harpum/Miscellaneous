"""
Maths-based functions implemented in python. 
(Not intended to be used practically, but proof of concept).
"""

def Sqrt(n: int | float, iters:int=10) -> float | TypeError:
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


def Factorial(n: int) -> int | TypeError | ValueError:
  """The Factorial, n! = Π{i=1, n} i
  or: n * (n-1) * (n-2) * ... * 2 * 1
  e.g. 5! = 5 x 4 x 3 x 2 x 1 = 120
  Domain: n ∈ N+
  """
  if n < 0:
    raise ValueError("Factorial of a negative number requires the Gamma Function")
  if n == 0:
    return 1
  for i in range(2, n):  # x * 1 = x, starting at 2 saves a loop.
    n *= i
  return n


def Combination(n: int, r: int) -> int | TypeError:
  """The number of unordered subsets containing 'r' unique elements chosen from a set with 'n' elements.
  nCr = n!/r!(n-r)!
  e.g. There are three subsets of (1, 2, 3) that contain two elements (1, 2), (1, 3), (2, 3).
  Domain: {n, r} ∈ N+
    nCr ∈ N+ """
  return int(Factorial(n) / (Factorial(n-r) * Factorial(r)))  # Proof that the result in always an integer is beyond this implementation


def Permutation(n: int, r: int) -> int | TypeError:
  """The number of subsets containing 'r' elements elements chosen from a set with 'n' elements.
  In comparison to combinations, in permutations the order of a set is important, e.g. (1, 2, 3) != (3, 2, 1)
  nPr = n!/(n-r)!
  Domiain: {n, r} ∈ N+
      nPr ∈ N+ """
  return int(Factorial(n) / (Factorial(n-r)))  # Proof that the result in always an integer is beyond this implementation

# Below are kept as separate functions for now. 
def Sum_between(lower: int, upper: int) -> int | TypeError:
  """sum of all integers between lower -> upper bound (both inclusive)"""
  return (upper*(upper+1)-(lower*(lower-1)))//2

def Sum_to(upper: int) -> int | TypeError:
  """Sum of all integers 1 -> upper (inclusive)"""
  return (upper*(upper+1))//2


""" Dice probability functions """

def keep_highest(x: int, /, num_dice: int=2, dice_sides: int=20) -> float | TypeError:
  """Probability of rolling a number 'x' on a s-sided die when rolling n dice and only keeping the highest value"""
  return (x**num_dice - (x-1)**num_dice) / (dice_sides**num_dice)

def keep_lowest(x: int, /, num_dice: int=2, dice_sides: int=20) -> float | TypeError:
  """Probability of rolling a number 'x' on a s-sided die whne rolling n dice and only keeping the lowest value"""
  a = dice_sides+1 - x  # The values are reversed
  return keep_highest(a, num_dice, dice_sides)
