CHECK_1 = "true"
CHECK_2 = "love"
def calculate_love_score(name1, name2):
    combine = name1 + name2
    n_check_1 = checker(combine, CHECK_1)
    n_check_2 = checker(combine, CHECK_2)
    print(f"{n_check_1}{n_check_2}")
    
def checker(combineName, strCheck):
    n_check_1 = 0
    for i in combineName:
        for j in strCheck:
            if str.lower(i) == str.lower(j):
                n_check_1 += 1
    
    return n_check_1
    

calculate_love_score("jhun carlo macdon", "catherine de venecia")