


# handling exceptions
from distutils.log import error


try:
    # something that might cause an exception
    pass
except:
    # do this if there was an exception
    pass
else:
    # do this if there were no exceptions
    pass
finally:
    # do this no matter what happens
    pass


# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError: 
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("this is an error I made up")


height = float(input("Height: "))
weight = int(input("weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)
