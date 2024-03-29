import operator


# Dictionary of arithmetic operators and their respective functions
ops = {'+': operator.add, '-': operator.sub, '*': operator.mul,
       '/': operator.truediv, '%': operator.mod, '^': operator.pow}


def calculate():
    try:
        while True:
            first_num = int(input("First Number: "))
            user_op = input("Operation: ")
            sec_num = int(input("Second Number: "))

            # Print the result of user selected operation of (1st number and 2nd number)
            print(ops[user_op](first_num, sec_num))

            again = input("Would you like to do another calculation? Press any key to continue or 'n' to quit\n")
            if again.lower() == 'n':
                break
            else:
                continue

    # Extremely basic error handling
    except ZeroDivisionError or ValueError:
        print("Zero Division Error or Value Error")
    except:
        print("stop testing me")


if __name__ == '__main__':
	print("Calculator Program")
	print("Use numerical characters and +, -, *, /, %, ^ operators.")

	calculate()
