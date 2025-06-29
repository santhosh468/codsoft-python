def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        return "Error: Division by zero"
    return a/b

def calc(a,b,operation):
    if  operation == "+" or operation == "add":
        return add(a,b)
    elif operation == "-" or operation == "sub":
        return sub(a,b) 
    elif operation == "*" or operation == "mul":
        return mul(a,b)
    elif operation == "/" or operation == "div":
        return div(a,b)
    else:
        return "Error: Invalid operation"

def main():
    print("Simple Calculator")
    print("Available operations: +, -, *, /")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operation = input("Enter operation: ").strip().lower()
    
    result = calc(a, b, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    while True:
        main()
        cont = input("Do you want to perform another calculation? (yes to continue, no to quit): ").strip().lower()
        if cont == "no":
            print("Exiting calculator. Thank You! Come back again!")
            break