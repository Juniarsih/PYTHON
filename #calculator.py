#calculator

class Calculator:
    def __init__(self):
        print ("Calculator")

    def add (self, a,b):
        return a + b
    
    def subtract (self, a,b):
        return a - b
    
    def multiply (self, a, b):
        return a * b
    
    def divide (self, a, b):
        if b == 0:
            print ("ERRORR! DIVISION BY ZERO IS NOT ALLOWED")

        return a / b
    
    def power (self, a, b):
        return a ** b
    
    def run (self):
        print ("CALCULATOR")
        print ("1. Add")
        print ("2. Subtract")
        print ("3. Multiply")
        print ("4. Divide")
        print ("5. Power")

        while True:
            choice = input("choose operation \nEnter q for quit  ")

            if choice.lower() == 'q':
                print("Quitting...")
                break

            if choice in ['1', '2', '3', '4', '5']:
                try :
                    a = float(input("enter first number  "))
                    b = float(input("enter second number  "))
                
                except ValueError:
                    print ("INVALID!! PLEASE ENTER NUMBER ONLY")
                    continue

                if choice == '1':
                    print(f"result = {self.add(a,b)}")
                
                elif choice == '2':
                    print(f"result = {self.subtract(a,b)}")

                elif choice == '3':
                    print(f"result = {self.multiply(a,b)}")

                elif choice == '4':
                    print(f"result = {self.divide(a,b)}")

                elif choice == '5':
                    print(f"result = {self.power(a,b)}")

            else :
                print("ERROR")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
    











