class Calculator:
    def __init__(self):
        # Asking user to input 1st number
        self.a = int(input("Enter furst number:"))
        # Asking user to input 2nd number
        self.b = int(input("Enter 2nd number:"))

    def add(self):
        self.result = self.a+self.b
        return self.result

    def subtract(self):
        self.result = self.a-self.b
        return self.result

    def multiply(self):
        self.result = self.a*self.b
        return self.result

    def divide(self):
        self.result = self.a/self.b
        return self.result

    def choice(self):
        self.choice = int(
            input("TYPE\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\nWHAT DO YOU WANT TO DO:"))

    def display(self):
        if self.choice == 1:
            print(f"result:{self.add()}")
        if self.choice == 2:
            print(f"result:{self.subtract()}")
        if self.choice == 3:
            print(f"result:{self.multiply()}")
        if self.choice == 4:
            print(f"result:{self.divide()}")


while True:
    p1 = Calculator()
    p1.choice()
    p1.display()
    terminate = input(
        "\nIf calculations done type 'Break' to continue calculation type 'Continue':").lower()
    if (terminate == "break"):
        break
    elif (terminate == "continue"):
        continue
