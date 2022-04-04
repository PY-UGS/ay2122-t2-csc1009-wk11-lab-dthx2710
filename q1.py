class Calculator:
    def __init__(self, input1, input2):
        self.input1 = 0
        self.input2 = 0

    def adder(self):  # add together
        return self.input1 + self.input2

    def subtractor(self):  # subtract
        return self.input1 - self.input2

    def multiplier(self):  # multiply
        return self.input1 * self.input2

    def divider(self):  # divide
        return self.input1 / self.input2

    def clear(self):  # clear values
        self.input1 = 0
        self.input2 = 0

#  store input in x and y
x = float(input("Enter 1st value: "))
y = float(input("Enter 2nd value: "))
calc = Calculator(x, y)

print("Add: ", calc.adder())
print("Subtract: ", calc.subtractor())
print("Multiply: ", calc.multiplier())
print("Divide: ", calc.divider())

# check if cleared
print("Before clear: " + str(calc.input1) + " and " + str(calc.input2))
calc.clear()
print("After clear: " + str(calc.input1) + " and " + str(calc.input2))


