from tkinter import *
import calculator

HEIGHT = 500  # Height variable
WIDTH = 350  # Width variable
BUTTON_HEIGHT = 2  # Standard button height
BUTTON_WIDTH = 2  # Standard button width
PAD_X = 5  # Standard padding
PAD_Y = 5


def main():
    """
    Set up and initialize window elements.
    Number, operation, and function buttons (20 total at base)
    """
    window = Tk()  # Declare the window
    window.title("Calculator")  # Set window title
    window.configure(width=WIDTH, height=HEIGHT)  # Set window width and height
    window.configure(bg='lightgray')  # Set window background color
    calculation = StringVar() # Hold the calculation in this variable

    # List of the keys to be displayed / Associated functions
    keys = ['CE', 'C', '<=', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '+-', '0', '.', '=']

    i = 0  # Iterator for the key list

    # For every row and column coordinate, place the proper keys[i] button
    for row in range(5):  # 5 rows
        for col in range(4):  # 4 columns
            # Button will use var 'i' to select the text,
            # and the standard button width and height vars
            button = Button(text='%s' % (keys[i]),
                            width=BUTTON_WIDTH,
                            height=BUTTON_HEIGHT)
            # Place the button at the proper row (+2 to account for expression_field) and col in the grid
            button.grid(row=row+2, column=col)
            i += 1  # Iterate through keys[] dict

        # Entry box that will show the equation in real-time
        expression_field = Entry(window, textvariable=calculation)
        expression_field.grid(row=0, columnspan=4, rowspan=2)

    window.mainloop()  # Main loop


def clear_entry():
    """
    Clear the last user entry -- not a total reset!
    """

    pass


def clear():
    """
    Global calculation clear
    """

    pass


if __name__ == '__main__':
    main()
