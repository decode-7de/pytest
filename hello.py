from tokenize import Name


def print_hello():
    return "hello world"

A='A'
def check_assert():
    try :
        assert print_hello() == "hello world"
        print(int(A))
    except AssertionError:
        print ("Assertion failed")
    except NameError:
        print("some other error ...!")
    except :
        print("junk something else")

check_assert()