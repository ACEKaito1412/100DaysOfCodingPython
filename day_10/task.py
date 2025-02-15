def format_name(f_name, l_name):
    """Takes two string and format it into a title case version of two string"""
    fname = f_name.title()
    lname = l_name.title()

    name = fname + " " + lname
    # print(f"{fname} {lname}")
    return name

print(format_name("acE", "kAitO"))


# leap year

def is_leap_year(year):
    """Takes a year and checks if its a leapyear or not"""
    
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
        
print(is_leap_year(1989))


    