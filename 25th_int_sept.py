Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

============ RESTART: C:\Users\sravya\Desktop\Codegnan_python\25th_sept.py ============

============ RESTART: C:\Users\sravya\Desktop\Codegnan_python\25th_sept.py ============
10.0
>>> 
============ RESTART: C:\Users\sravya\Desktop\Codegnan_python\25th_sept.py ============
10.0
10
>>> x="sravya"
>>> int(x)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    int(x)
ValueError: invalid literal for int() with base 10: 'sravya'
>>> float(x)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    float(x)
ValueError: could not convert string to float: 'sravya'
>>> bool(x)
True
>>> complex(x)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    complex(x)
ValueError: complex() arg is a malformed string
>>> x="101"
>>> type(x)
<class 'str'>
>>> int(x)
101
>>> float(x)
101.0
>>> complex(x)
(101+0j)
>>> c=10+5j
>>> int(4.0)
4
>>> 10>20
False
>>> 1<=1
True
>>> x=10;y=20;z=30
>>> x==10 and y==20
True
>>> x>0 and y<100
True
>>> x!=10 and z==30
False
>>> 1 and 0
0
>>> 1 and 10 and 20
20
>>> 1 and 0 and 20
0
>>> not (true)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    not (true)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> not (True)
False
