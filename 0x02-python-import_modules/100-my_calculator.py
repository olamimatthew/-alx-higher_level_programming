#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    argv_number = len(argv)
    op = argv[1]
    a = argv[0]
    b = argv[2]

    if argv_number != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")

