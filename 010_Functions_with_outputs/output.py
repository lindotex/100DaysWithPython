
# Function without output (no return)
def format_name(f_name, l_name):
    formated_name = f_name.title()
    formated_last_name = l_name.title()
    
    print(f" {formated_name} {formated_last_name}")

format_name("AlISson", "lindOTE")


# Function with output 
def format_name2(f_name, l_name):
    formated_name2 = f_name.title()
    formated_last_name2 = l_name.title()
    
    return(f" {formated_name2} {formated_last_name2}")

formated_string = format_name2("CaSSiO", "lindOTE")
print(formated_string)

# Explain the parts of function with return:
#  output = function(input)

def format_name3(f_name, l_name):
    # Prevent in case of empty strings:
    if formated_name3 == "" or formated_last_name3 == "":
        return "You didn't filled the form properly."
    
    formated_name3 = f_name.title()
    formated_last_name3 = l_name.title()
    
    return(f" {formated_name3} {formated_last_name3}")

formated_string = format_name2(input("What is your first name?\n"), input("What is your last name?\n"))
print(formated_string)