while True:
    try:
        print("Press 'e' to exit.")
        n1 = float(input("Enter first number: "))
        operator = input("Enter an operator(+, -, *, /): ")
        n2 = float(input("Enter second number: "))
        line = "----------------------------"
        
        if n1 == 'e':
            break
        
        if operator == 'e':
            break
        
        if n2 == 'e':
            break
        
        if operator == '+':
            result = n1 + n2
            print(f"{n1} {operator} {n2} = {result}")
            print(line)
        elif operator == '-':
            result = n1 - n2
            print(f"{n1} {operator} {n2} = {result}")
            print(line)
            
        elif operator == '*':
            result = n1 * n2
            print(f"{n1} {operator} {n2} = {result}")
            print(line)
            
        elif operator == '/':
            result = n1 / n2
            print(f"{n1} {operator} {n2} = {result}")
            print(line)
            
        else:
            print(f"(+, -, *, /) -> Only these operators are supported and you entered {operator}.")
            print(line)
            
        
    except ValueError as e:
        print("Please enter a valid number.")
        print(line)
        
    except ZeroDivisionError as e:
        print("Division by zero can't be done.")
        print(line)
    
    except Exception as e:
        print("Something went wrong!")
        print(line)

            

