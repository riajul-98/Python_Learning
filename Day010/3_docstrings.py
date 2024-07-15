# Functions with outputs

def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""
    # The above will display when hovering over the format_name to tell others what it does.
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    else:
        formated_f_name = f_name.title()
        formated_l_name = l_name.title()
        return f"{formated_f_name} {formated_l_name}"
        print("This got printed") # Anything after the return has been executed will be ignored


print(format_name(input("What is your first name? "), input("What is your last name? ")))