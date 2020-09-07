
def func_calc():
    x1, x2, y1, y2, x3 = get_input()
    y3 = calculate_output(x1, x2, y1, y2, x3)
    return print("Your output y3 is {}".format(y3))

def get_input():
    x1 = input("Enter x1: ")
    y1 = input("Enter y1: ")
    x2 = input("Enter x2: ")
    y2 = input("Enter y2: ")
    x3 = input("Enter x3: ")
    return float(x1), float(x2), float(y1), float(y2), float(x3)

def calculate_output(x1, x2, y1, y2, x3):
    a = (y1 - y2)/(x1 - x2)
    b = y1 - a * x1
    y3 = a * x3 + b
    return float(y3)


if __name__ == "__main__":
    func_calc()
