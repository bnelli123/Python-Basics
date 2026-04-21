#!/usr/bin/env python3
"""
Prints a row of asterisks based on user input.
Example: For n=5, outputs: *****
"""

try:
    n = int(input("Enter the value of n: "))
    if n < 0:
        print("Please enter a non-negative integer.")
    else:
        print("*" * n)
except ValueError:
    print("Invalid input. Please enter an integer.")