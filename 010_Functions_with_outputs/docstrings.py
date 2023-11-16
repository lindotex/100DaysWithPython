def format_name(f_name, l_name):
    """Take a first and last name and formate it to First Letter Caps. """
    
    formated_name = f_name.title()
    formated_last_name = l_name.title()
    
    # Prevent in case of empty strings:
    if formated_name == "" or formated_last_name == "":
        return "You didn't filled the form properly."
    
    return(f" {formated_name} {formated_last_name}")

formated_string = format_name(input("What is your first name?\n"), input("What is your last name?\n"))
print(formated_string)