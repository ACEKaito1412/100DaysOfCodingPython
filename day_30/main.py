# file not found
# with open('as.txt') as file:
#     print(file.read())


# keyerror
# a_dictionary = {"key": "value"}
# value = a_dictionary['no_key']

# indexerror
# fruitlist = ['apple', 'grapes', 'strawberry']
# fruitlist[12]

# typeerror
# text = 'abc'
# print(text+5)

def try_exception():
    try:
        file = open("text.txt")
        a_dictionary = {"key" : "value"}
        print(a_dictionary["aosas"])
    except FileNotFoundError:
        file = open("text.txt", "w")
        file.write("something")
        print('somehing wrong')
    except KeyError as err_message:
        print(f"key error: {err_message}")
    else:
        content = file.read()
        print(content)
    finally:
        file.close()
        print("file is close")


def raise_exception():
    height = int(input("Height: "))
    weight = int(input("Weight: "))

    if height > 3:
        raise ValueError("Human height shouldn't be greater than 3 meters")
    
    bmi = weight / height ** 2
    print(f"BMI: {bmi}")
    
raise_exception()