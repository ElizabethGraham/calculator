import re
import operator

# Dictionary of arithmetic operators and their respective functions
ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, 'x': operator.mul,
       '/': operator.truediv, '%': operator.mod, '^': operator.pow, '**': operator.pow}


def main():
    while True:
        expr = input("Enter calculation (or 'q' to quit): ")
        if expr.lower() == 'q':
           break

        result = calculate_expression(expr)
        if result is not None:
            if result.is_integer():
                result = int(result)

            print("Result:", round(result, 4))

def calculate_expression(expr: str) -> float | None:
    """
    :param first_num: First numerical parameter
    :param sec_num: Second numerical parameter
    :param op: The user selected operation to be performed
    :return: Final calculation
    """
    # remove spaces and normalize operator symbols
    expr = expr.replace(' ', '').replace('X', 'x')

    # match numbers and operator
    match = re.fullmatch(r'(-?\d+\.?\d*)(\*\*|\^|[+\-*/x%])(-?\d+\.?\d*)', expr)
    if not match:
        print("Invalid input format. Use: number operator number")
        return None

    first, op, second = match.groups()
    first, second = float(first), float(second)

    if op not in ops:
        print("Invalid operator.")
        return None

    try:
        return ops[op](first, second)
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None

if __name__ == '__main__':
    main()
