# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
#
# If the function is passed a valid PIN string, return true, else return false.

def validate_pin(pin):
    # return true or false
    checker = str(pin)
    if len(checker) == 4 or len(checker) == 6:
        if checker.isdigit():
            return True
        else:
            return False
    else:
        return False


print(validate_pin("324gg"))
