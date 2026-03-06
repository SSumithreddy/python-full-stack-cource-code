Python 3.14.3 (v3.14.3:323c59a5e34, Feb  3 2026, 11:41:37) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
name = input()
python
name
'python'
type(name)
<class 'str'>
name = input("Enter the Name:")
Enter the Name:sumith
name
'sumith'
age = input("Enter the age: ")
Enter the age: 22
age
'22'
age = int(input("Enter the age: "))
Enter the age: 22
age
22
type(age)
<class 'int'>
price = input("Enter the price: ")
Enter the price: 99.99
price
'99.99'
price = float(input("Enter the price: "))
Enter the price: 99.99
price
99.99
type(price)
<class 'float'>
'sumith teja bhanu'
'sumith teja bhanu'
'sumith teja bhanu'.split()
['sumith', 'teja', 'bhanu']
'sumith teja bhanu'.split(',')
['sumith teja bhanu']
names = input("Enter the name: ")
Enter the name: sumith teja bhanu
names
'sumith teja bhanu'
names = input("Enter the names: ").split()
Enter the names: sumith teja bhanu
names
['sumith', 'teja', 'bhanu']
numbers = input("Enter the numbers: ")
Enter the numbers: 2 3 4 5 
numbers
'2 3 4 5 '
numbers = list(map(int,input("Enter the numbers: ").split()))
Enter the numbers: 1 2 3 4 55
numbers
[1, 2, 3, 4, 55]
numbers = list(map(float,input("Enter the numbers: ").split()))
Enter the numbers: 1 2 3 44
nubers
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    nubers
NameError: name 'nubers' is not defined. Did you mean: 'numbers'?
numbers
[1.0, 2.0, 3.0, 44.0]
numbers = tuple(map(float,input("Enter the numbers: ").split()))
Enter the numbers: 1.2 2.3 4.5
numbers
(1.2, 2.3, 4.5)
numbers = set(map(int,input("Enter the numbers: ").split()))
Enter the numbers: 1 2 3 45
numbers
{1, 2, 3, 45}
username,pasword = ['py','py123']
username
'py'
pasword
'py123'
username,pasword = input("Enter the username and pasword; ").split()
Enter the username and pasword; sumith sumith123
uswename
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    uswename
NameError: name 'uswename' is not defined. Did you mean: 'username'?
username
'sumith'
pasword
'sumith123'
a,b,c = list(map(int,input("Enter the sides: ").split()))
Enter the sides: 3 4 5 
a
3
b
4
c
5
>>> numbers = tuple(map(int,input("Enter the number:").split()))
Enter the number:1 2 3 4 5
>>> numbers
(1, 2, 3, 4, 5)
>>> names = tuple(input("Enter the name:").split())
Enter the name:sumith tejs bhanu
>>> names
('sumith', 'tejs', 'bhanu')
>>> names = set(input("Enter the names:").split())
Enter the names:sumith teja bhanu
>>> names
{'bhanu', 'sumith', 'teja'}
>>> numbers = list(map(float,input("Enter the numbers: ").split()))
Enter the numbers: 6543
>>> numbers
[6543.0]
>>> numbers = tuple(map(int,input("Enter the numbers: ")split()))
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> numbers = tuple(map(int,input("Enter the numbers: ").split()))
Enter the numbers: 2 3 4 5 6 7
>>> numbers
(2, 3, 4, 5, 6, 7)
>>> d = eval(input("Enter the input: "))
Enter the input: {1:1,2:3,4:16}
>>> d
{1: 1, 2: 3, 4: 16}
>>> d = eval(input("Enter the input:"))
Enter the input:[1,2,3,4,5,6,7]
>>> d
[1, 2, 3, 4, 5, 6, 7]
>>> a,b,c = list(map(int,input("Enter the sides:").split()))
Enter the sides:5 6 7 
>>> a
5
>>> b
6
>>> c
7
