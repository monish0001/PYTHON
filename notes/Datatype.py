x = 10      # positive integer
y = -5      # negative integer
z = 0       # zero is also an integer



print(type(x))  # <class 'int'>


a = 3.14
b = -2.5
c = 0.0

print(type(a))  # <class 'float'>


name = "Monish"
greeting = 'Hello'
sentence = "Python is fun!"

print(type(name))  # <class 'str'>


print("Hi " + "there!")   # concatenation
print("Ha" * 3)           # repetition → HaHaHa


is_python_fun = True
is_raining = False

print(type(is_python_fun))  # <class 'bool'>

if is_python_fun:
    print("Yes, Python is awesome!")
    
    
    
print(id(is_python_fun))
