Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
myvar=10
my_var=10
My_var=10
my var =10
SyntaxError: invalid syntax
my@var=10
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
My_Var=10
my_var=10
_myvar=10
12myvar=10
SyntaxError: invalid decimal literal
myvar12=10
myvar=10
Myvar=20
myvar
10
Myvar
20
if = 20
SyntaxError: invalid syntax
followers=1000
followers
1000
type(followers)
<class 'int'>
likes_cnt=56
type(likes_cnt)
<class 'int'>
followers = 15.6
type(followers)
<class 'float'>
price = 67.356
type(price)
<class 'float'>
a= 3+6j
type(a)
<class 'complex'>
a= 5+7J
type(a)
<class 'complex'>
s = 'python programming'
s
'python programming'
s="Python"
s
'Python'
type(s)
<class 'str'>
product_name="laptop"
s
'Python'
s[0]
'P'
s[5]
'n'
s[1]
'y'
s[2]
't'
s[3]
'h'
s[4]
'o'
s[5]
'n'
names = ['venu','tarun','bhuvan','manoj']
names
['venu', 'tarun', 'bhuvan', 'manoj']
names[0]
'venu'
names[1]
'tarun'
names[2]
'bhuvan'
names[3]
'manoj'
names.append('manoj')
names
['venu', 'tarun', 'bhuvan', 'manoj', 'manoj']
t=(1,1,1,1,2,3,4,5)
t
(1, 1, 1, 1, 2, 3, 4, 5)
t[0]
1
t[2]
1
t.append(0)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    t.append(0)
AttributeError: 'tuple' object has no attribute 'append'
type(t)
<class 'tuple'>
type(names)
<class 'list'>
s={56789,5467,123,34,1,387,7}
s
{1, 34, 387, 5467, 56789, 7, 123}
s.add(1)
s
{1, 34, 387, 5467, 56789, 7, 123}
products={'product_id':1,"product_name":"laptop","price":75000}
products
{'product_id': 1, 'product_name': 'laptop', 'price': 75000}
status = True
type(status)
<class 'bool'>
type(s)
<class 'set'>
type(products)
<class 'dict'>
s = False
a = None
a=10
float(a)
10.0
str(a)
'10'
complex(a)
(10+0j)
list(a)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
a=12.3
int(a)
12
str(a)
'12.3'
complex(a)
(12.3+0j)
list(a)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    list(a)
TypeError: 'float' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    tuple(a)
TypeError: 'float' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    set(a)
TypeError: 'float' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    dict(a)
TypeError: 'float' object is not iterable
bool(a)
True
a=4+2j
int(a)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(a)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'complex'
str(a)
'(4+2j)'
list(a)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    list(a)
TypeError: 'complex' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    tuple(a)
TypeError: 'complex' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    set(a)
TypeError: 'complex' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    dict(a)
TypeError: 'complex' object is not iterable
bool(a)
True
l=[1,2,3,4,4,5,6]
l
[1, 2, 3, 4, 4, 5, 6]
int(l)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
tuple(l)
(1, 2, 3, 4, 4, 5, 6)
set(l)
{1, 2, 3, 4, 5, 6}
dict(l)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(a)
True
t=(1,2,3,4)
int(t)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(t)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    complex(t)
TypeError: complex() first argument must be a string or a number, not 'tuple'
list(t)
[1, 2, 3, 4]
set(t)
{1, 2, 3, 4}
dict(t)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(t)
True
s={1,2,3,4,5,6}
int(s)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(s)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
complex(s)
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    complex(s)
TypeError: complex() first argument must be a string or a number, not 'set'
list(s)
[1, 2, 3, 4, 5, 6]
tuple(s)
(1, 2, 3, 4, 5, 6)
dict(s)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    dict(s)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(s)
True
d= {1:1,2:4,3:9,4:16,5:25}
int(d)
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(d)
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
str(d)
'{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}'
list(d)
[1, 2, 3, 4, 5]
tuple(d)
(1, 2, 3, 4, 5)
set(d)
{1, 2, 3, 4, 5}
bool(d)
True
a = True
int(a)
1
flaot(a)
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    flaot(a)
NameError: name 'flaot' is not defined. Did you mean: 'float'?
float(a)
1.0
str(a)
'True'
list(a)
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    list(a)
TypeError: 'bool' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    tuple(a)
TypeError: 'bool' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    dict(a)
TypeError: 'bool' object is not iterable
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    set(a)
TypeError: 'bool' object is not iterable
>>> bool(a)
True
