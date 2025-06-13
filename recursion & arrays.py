Python 3.13.3 (v3.13.3:6280bb54784, Apr  8 2025, 10:47:54) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Enter "help" below or click "Help" above for more information.
def add(a, b):
    return a + b
result = add(5, 6)
SyntaxError: invalid syntax
print(result)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(result)
NameError: name 'result' is not defined

============== RESTART: /Users/rutikagaonkar/Desktop/Functions .py =============
11
def add(a, b)
SyntaxError: expected ':'
def add(a, b):
    return a + b
result = add(7, 9)
SyntaxError: invalid syntax
print(result)
11
def add(a, b):
    return a + b

result = add(7, 9)
print(result)
16

result = add(15, 25)
print (result)
40

def my_function(fname):
    print(fname + "Refsnes")

    
my_function("Emil")
EmilRefsnes
my_function("Rufus")
RufusRefsnes
my_function("Linus")
LinusRefsnes
LinusRefsnes
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    LinusRefsnes
NameError: name 'LinusRefsnes' is not defined
def my_function(fname, lname):
    print(fname + "" + lname)

    
my_function("emil","refsnes")
emilrefsnes
def my_function(fname, lname):
    print(fname + " " + lname)

    
my_function("Rinif", "Larnaca")
Rinif Larnaca

def countdown(n):
    if n == 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)

        
n = 5
result = countdown(n)
5
4
3
2
1
Done!

x = lambs
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    x = lambs
dNameError: name 'lambs' is not defined
x = lambda a, b:
    
SyntaxError: invalid syntax
x = lambda a, b: a * b
print(5, 6)
5 6
print(x(5, 6))
30
30
30
for x in cars:
    print(x)

    
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    for x in cars:
NameError: name 'cars' is not defined. Did you mean: 'vars'?
>>> cars = ["ford", "volvo", "bmw"]
>>> x = len(cars)
>>> print(x)
3
>>> for x in cars:
...     print(x)
... print(x)
SyntaxError: invalid syntax
>>> 
>>> cars.append("Honda:)
...             
SyntaxError: unterminated string literal (detected at line 1)
>>> cars.append("honda")
...             
>>> print(x)
...             
3
>>> print(cars)
...             
['ford', 'volvo', 'bmw', 'honda']
>>> for x in cars:
...             print(x)
... 
...             
ford
volvo
bmw
honda
>>> cars.pop(2)
...             
'bmw'
>>> cars.pop(1)
...             
'volvo'
>>> cars.sort()
...             
>>> print(cars)
...             
['ford', 'honda']
