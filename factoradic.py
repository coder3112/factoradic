import math
import os
from functools import cache
from typing import Callable


@cache
def dec_to_fact(n: int) -> int:
    """Refer to XKCD 2835."""
    # FIXME: This algorithm si quite wrong right now. It assumes that the leading_digit is <10 but this is not always true. Indeed, one finds the first error at 10*10!, which cannot be easily represented without it also looking like 11!, causing a conflict. This problem becomes especially common as one moves towards larger numbers.
    fact = 1
    i = 1
    while fact < n:
        i += 1
        fact = math.factorial(i)
    if fact == n:
        largest_base, largest_fact = i, fact
    else:
        largest_base = i - 1
        largest_fact = math.factorial(largest_base)
    leading_digit = math.floor(n / largest_fact)
    leading_digit_padded = int(str(leading_digit) + "0" * (largest_base - 1))
    full_number = leading_digit_padded
    total_n_found_so_far = leading_digit * largest_fact
    if total_n_found_so_far == n:
        return full_number
    return full_number + dec_to_fact(n - total_n_found_so_far)


def fact_to_dec(n: int) -> int:
    """Reverses dec_to_fact."""
    i = 1
    decimal = 0
    for digit in str(abs(n))[::-1]:
        decimal += int(digit) * math.factorial(i)
        i += 1
    sign: Callable[[int], int] = lambda x: int(math.copysign(1, x))
    return decimal * sign(n)


def factoradic(decimal: int) -> int:
    """Convert with wraps and checks."""
    if decimal == 0:
        print("Not possible. $\\Gamma(1 + z)=0$ has no solutions in $\\CC$")
        os._exit(1)

    factoradic = dec_to_fact(abs(decimal))
    if decimal < 0:
        factoradic *= -1
    if fact_to_dec(factoradic) != decimal:
        print(
            f"Calculated {decimal}_10={factoradic}_f. But that is wrong, since {factoradic}_f={fact_to_dec(factoradic)}"
        )
        os._exit(1)
    return factoradic


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("value")

    args = parser.parse_args()
    decimal = int(args.value)

    factoradic(decimal)
    #i = 1
    #while True:
    #    factoradic(i)
    #    i += 1
