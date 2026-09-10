#!/usr/bin/env python3
"""
FizzBuzz with a twist: FizzBuzzBazz

Rules:
- multiples of 3  -> "Fizz"
- multiples of 5  -> "Buzz"
- multiples of 7  -> "Bazz"
- multiples of shared factors combine the words (e.g. 15 -> "FizzBuzz",
  21 -> "FizzBazz", 35 -> "BuzzBazz", 105 -> "FizzBuzzBazz")
- otherwise, print the number itself
"""


def fizzbuzzbazz(n: int) -> str:
    result = ""
    if n % 3 == 0:
        result += "Fizz"
    if n % 5 == 0:
        result += "Buzz"
    if n % 7 == 0:
        result += "Bazz"
    return result or str(n)


def main() -> None:
    for i in range(1, 101):
        print(fizzbuzzbazz(i))


if __name__ == "__main__":
    main()
