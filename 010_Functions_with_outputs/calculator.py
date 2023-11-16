from art import logo

print(logo)
continue_calculating = True
accumulated_value = ''

while continue_calculating == True:

    first_number = float(input("What is the first number?\n"))
    operation = str(input("What is the Operation?\n+ : addition\n- : subtraction\n/ : division\n* : multiplication\n"))
    second_number = float(input("What is the second number?\n"))

    print(f" You full answer is ( {first_number} {operation } {second_number} ), is that right? ")
    print(f"Here is the answer:")

    def calculator(first_number, second_number, operation):
        
        if operation == '+':
            value = first_number + second_number
            return value
        elif operation == '-':
            value = first_number - second_number
            return value
        elif operation == '/':
            value = first_number / second_number
            return value
        elif operation == '*':
            value = first_number * second_number
            return value
        else:
            return "You didn't choose an available option, please try again."
        

    print(calculator(first_number,second_number,operation))
    loop_question = str(input("Would you like to continue calculating with your number?\nYes (y) or No (n) ? \n"))
    if loop_question == 'y':
        accumulated_value += calculator().value
    if loop_question == 'n':
        accumulated_value += calculator().value
        continue_calculating == False
        
