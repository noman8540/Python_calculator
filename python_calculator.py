from art import logo
print(logo)

# Add
def add (n1, n2):
    return n1 + n2

# Subtract
def subtract (n1, n2):
    return n1 - n2

# Multiply
def multiply (n1, n2):
    return n1 * n2

# Divide
def divide (n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
        
    should_continue = True

    while should_continue:
        
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculations = operations[operation_symbol]
        result = calculations(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {result}")
        
        retry = input("Type 'y' for continue calulating with {result}, or type 'n' to start with new calculation, or type exit to exit(): ")         
        
        if retry == 'y':
            num1 = result
        elif retry == 'exit':
            break
        else:
            should_continue = False
            calculator()

calculator()


quit()