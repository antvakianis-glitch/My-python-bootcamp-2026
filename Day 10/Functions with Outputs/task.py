def format_name(f_name, l_name):
    formated_name = f_name.title() + " " + l_name.title()
    return formated_name

name = input("Enter your name: ")
surname = input("Enter your surname: ")
print (format_name(name, surname))
