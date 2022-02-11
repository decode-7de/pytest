name='Smith'
def test_func(name):
    try:
        print("Hello" " "+ name)
    except NameError:
        print("Name is not denoted")
    else:
        print("ding gong..!")
    finally:
        print("Have a nice day")

test_func(name)

del name

def new_func2(name):
    try:
        print("Hello " + name)
    except NameError:
        print("Name is not denoted")

# new_func2(name)