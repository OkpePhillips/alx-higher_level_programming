#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    num_args = len(sys.argv) - 1
    operator = ['+', '-', '*', '/']
    if num_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    args = sys.argv[1:]
    a = int(args[0])
    b = int(args[2])
    if args[1] not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if args[1] == '+':
        result = add(a, b)
        print("{} + {} = {}".format(a, b, result))
    if args[1] == '-':
        result = sub(a, b)
        print("{} - {} = {}".format(a, b, result))
    if args[1] == '*':
        result = mul(a, b)
        print("{} * {} = {}".format(a, b, result))
    if args[1] == '/':
        result = div(a, b)
        print("{} / {} = {}".format(a, b, result))
