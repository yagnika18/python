#printing function 
def format_name(f_name,l_name):
    formatted_f_name=f_name.title()
    formatted_l_name=l_name.title()
    print(f"{formatted_f_name}{formatted_l_name}")
format_name("yagnika","SIVAPURAM")# Yagnika Sivapuram

#returning function
def format_name(f_name,l_name):
    formatted_f_name=f_name.title()
    formatted_l_name=l_name.title()
    return f"{formatted_f_name}{formatted_l_name}"
print(format_name("yagnika","SIVAPURAM"))# Yagnika Sivapuram
