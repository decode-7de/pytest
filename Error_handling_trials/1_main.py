'''
try:
Code block1
except:
Executes if any type of exception happens .. can have multiple excepts
else:
If there is no exception then execute this block
finally:
    what ever the error or not finally block will get executed..!
'''



def try_error1(a):
    try:
        print(int(a))
    except:
        print("some error...")
    else:
        print("No error")
        print("its converted..!")

#try_error1('A')

def try_error2(a):
    try:
        print(int(a))
    except ValueError:
        print("some Value Error...")     
    except :
        print("some error..!")   
    else:
        print("No error")
        print("its converted..!")
#try_error2('A')


def try_error3(a):
    try:
        print(int(a))
    except ValueError:
        print("some Value Error...")     
    except :
        print("some error..!")   
    else:
        print("No error")
        print("its converted..!")
try_error3('1')
