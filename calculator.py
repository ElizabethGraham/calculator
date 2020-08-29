import operator

ops = {'+': operator.add, '-': operator.sub, '*': operator.mul,
       '/': operator.truediv, '%': operator.mod, '^': operator.xor}


def calculate():
    first_num = input("First Number: ")
    user_op = input("Operation: ")
    sec_num = input("Second Number: ")

    print(ops[user_op](int(first_num), int(sec_num)))


print("Calculator Program")
print("Use numerical characters and +, -, *, /, %, ^ operators.")

calculate()
