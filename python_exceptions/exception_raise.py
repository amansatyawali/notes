try:
    raise ZeroDivisionError("Hi there")  # Raise Error
    raise NameError("Hi there from name")  # Raise Error
except:
    print("An exception")
    raise  # To determine whether the exception was raised or not