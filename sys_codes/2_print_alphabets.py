import string

alphabets = string.ascii_letters
print(alphabets)
print(len(alphabets))

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase

print(lower_case)
print(upper_case)
print(len(lower_case))
print(len(upper_case))

### using ord 

print(range(ord('a'),ord('z')))

for i in range(ord('a'),ord('z')):
    print (chr(i))

k=[map(chr,range(ord('a'),ord('z')))]
print(k)


def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon'))
print(list(x))