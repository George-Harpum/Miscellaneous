"""jkkj
Maths-based functions implemented in python. 
(Not intended to be used practically, but proof of concept).
"""

def sqrt(n: int | float, iters:int=10) -> float | complex:
  complex_tag = None
  if n < 0:
    n = abs(n)
    complex_tag = True
  x = n/2
  y = x
  for _ in range(iters):
    x -= ((x*x)-n)/(2*x)
    if x == y:
      break
    y = x
  if complex_tag:
    return complex(0, x)
  return x


def factorial(n: int) -> int:
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


def combination(n: int, r: int) -> int:
  """The number of unordered subsets containing 'r' unique elements chosen from a set with 'n' elements.
  nCr = n!/r!(n-r)!
  e.g. There are three subsets of (1, 2, 3) that contain two elements (1, 2), (1, 3), (2, 3).
  Domain: {n, r} ∈ N+
    nCr ∈ N+ """
  return int(factorial(n) / (factorial(n-r) * factorial(r)))  # Proof that the result in always an integer is beyond this implementation

def comb(n: int, r: int) -> int:
  """faster implementation of nCr / combinations / bionomial coefficient using the multiplicative formula"""
  if r == 1 or n-r == 1:
    return n
  if n == r or r == 0:
    return 1
  if r > n or r < 0:
    raise ValueError(f"domain is 1 <= r <= n, cannot accept {r=}")
  if r > 1:
    if n-r < r:
      r = n-r
    t = n
    for i in range(2, r+1):
      n *= (t+1-i)/i
  return int(n)


def permutation(n: int, r: int) -> int | TypeError:
  """The number of subsets containing 'r' elements elements chosen from a set with 'n' elements.
  In comparison to combinations, in permutations the order of a set is important, e.g. (1, 2, 3) != (3, 2, 1)
  nPr = n!/(n-r)!
  Domiain: {n, r} ∈ N+
      nPr ∈ N+ """
  return int(factorial(n) / (factorial(n-r)))  # Proof that the result in always an integer is beyond this implementation

# Below are kept as separate functions for now. 
def sum_between(lower: int, upper: int) -> int:
  """sum of all integers between lower -> upper bound (both inclusive)"""
  return (upper*(upper+1)-(lower*(lower-1)))//2

def sum_to(upper: int) -> int | TypeError:
  """Sum of all integers 1 -> upper (inclusive)"""
  return (upper*(upper+1))//2


def digital_root(x: int | str, /, base: int = 10) -> int:
  """repeated sum of digits until only a single digit remains
  e.g. 12345 -> 1+2+3+4+5 = 15 -> 1+5 -> 6
  digital_root(12345, 10) -> 6
  when x is an int, it must be in base 10.
  when x is a str, it must be in the same base as given as base parameter"""
  if isinstance(x, str):
    x = int(x, base)
  if x == 0:
    return 0
  new_base = base - 1
  if (out:= x % new_base) == 0:
    return new_base
  return out


""" Dice probability functions """

def keep_highest(x: int, /, num_dice: int=2, dice_sides: int=20) -> float:
  """Probability of rolling a number 'x' on a s-sided die when rolling n dice and only keeping the highest value"""
  return (x**num_dice - (x-1)**num_dice) / (dice_sides**num_dice)

def keep_lowest(x: int, /, num_dice: int=2, dice_sides: int=20) -> float:
  """Probability of rolling a number 'x' on a s-sided die whne rolling n dice and only keeping the lowest value"""
  a = dice_sides+1 - x  # The values are reversed
  return keep_highest(a, num_dice, dice_sides)

def avg_roll(num: int, sides: int) -> float:
  """Simple average of xdy dice"""
  return num*((sides+1)/2)

def success_distribution(odds_per: float, total=1) -> dict[int, float]:
  """Distribution of number of successes with an independent probability.
  returns dict[number_of_successes, probability]"""
  if not isinstance(total, int) or total < 0:
    raise ValueError(f"Domain: Attacks ∈ N, instead received {total}")
  out = {}
  for num in range(total+1):
    temp = comb(total, num)
    temp *= odds_per**num
    temp *= (1-odds_per)**(total-num)
    out[num] = temp
  return out

from functools import partial
def chance_to_beat_target(target, mod, *, adv=0, sides=20):
  """Calculate the proibability of rolling >= target when total roll is dice+modifier
  Assumes (and can only handle) "meets it beats it" (roll >= target) method of rolling
  Parameters:
    target: int = the number you must roll >= then
    mod: int = modifier that is added to the roll (can be negative)
    dice_sides: int = total number of sides the dice has (assumes sides are 1 -> dice_sides)
  """
  higher = sides+1
  lower = target-mod
  if abs(adv) < 2: 
    if lower >= higher:
      return 0.05 # allows automatic success (DnD 5e nat 20 rules)
    if lower < 1:
      return 0.95 # allows automatic failure (nat 1 always fails)
  hit_range = range(lower, higher)
  if adv > 0:
    return sum(map(partial(keep_highest, num_dice=adv), hit_range))
  if adv < 0:
    return sum(map(partial(keep_lowest, num_dice=abs(adv)), hit_range))
  return (higher-lower)/sides

def prob_of_sum(num, size, val):
  """Probability of rolling Val when rolling 'num' die with 'size' sides and each rolled value is added together
  e.g. odds of rolling 7 on 2d6 is prob_of_sum(2, 6, 7)"""
  limit = ((val-num)//size)+1
  if num == val:
    return 1/(size**num)
  S = 1
  if num != val:
    S = sum([(-1)**i * comb(num, i) * comb(val-(size*i)-1, num-1) for i in range(limit)])
  return 1/(size**num) * S


def sum_n_dice_dist(num: int, size: int) -> dict[int, float]:
  """Probability distribution of ALL possible sums for 'num' 'size'-sided die"""
  out = {}
  top = num*(size+1)
  for x in range(num, ((top)//2)+1):
    odds = prob_of_sum(num, size, x)
    out[x] = odds
    out[top-x] = odds
  return dict(sorted(out.items()))

