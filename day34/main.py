# age: int
# name: str
# height: float
# is_human: bool

# `-> bool` means that the expected output type is a bool. It is called a `Type Hint`
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


print(police_check(21))