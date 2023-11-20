from art import logo

print(logo)
continue_calculating = True
accumulated_value = ''

first_number = float(input("What is the first number?\n"))

while continue_calculating == True:

    operation = str(input("What is the Operation?\n+ : addition\n- : subtraction\n/ : division\n* : multiplication\n"))
    second_number = float(input("What is your next number?\n"))

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
        accumulated_value = float(calculator(first_number,second_number, operation))
    
    if loop_question == 'n':
        print("Bye Bye, have a nice day!")
        accumulated_value = float(calculator(first_number,second_number, operation))
        continue_calculating = False
