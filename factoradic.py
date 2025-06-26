import argparse
import math


def dec_to_fact(n: int) -> int:
    """Refer tp XKCD 2835."""
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("value")

    args = parser.parse_args()
    decimal = int(args.value)

    factoradic = dec_to_fact(decimal)
    print(factoradic)
