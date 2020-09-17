import operator

# Dictionary of arithmetic operators and their respective functions
ops = {'+': operator.add, '-': operator.sub, '*': operator.mul,
       '/': operator.truediv, '%': operator.mod, '^': operator.pow}


def calculate(first_num: int, sec_num: int, user_op):
    """
    :param first_num: First numerical parameter
    :param sec_num: Second numerical parameter
    :param user_op: The user selected operation to be performed
    :return: Final calculation
    """
    try:
        if user_op in ops:
            # print the result of user selected operation of (1st number and 2nd number)
            return ops[user_op](first_num, sec_num)
        else:
            raise Exception(f'{user_op} is not a valid operation.')

    # Extremely basic error handling
    except ZeroDivisionError or ValueError:
        print("Zero Division Error or Value Error")
    except:
        print("Something went wrong :(")