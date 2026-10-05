Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 0 and 4 or 5 and 6 or 1
6
>>> 10 and 4 or 5 and 6 or 1
4
>>> 16 and 4 and 3 or 2 and 7 or 7
3
>>> 1 and 4 or (not 10) or and 5
SyntaxError: invalid syntax
>>> 1 and 4 or (not 10) and 5
4
>>> not 5 and 4 or 0
0
>>> 10 & 1
0
>>> bin(20)
'0b10100'
>>> bin(69)
'0b1000101'
>>> bin(10)
'0b1010'
>>> n="1010"
>>> print(int(n))
1010
>>> n="1010"
... print(int(n,2))
SyntaxError: multiple statements found while compiling a single statement
>>> n="1010"
>>> print(int(n,2))
10
>>> oct(42)
'0o52'
>>> oct(35)
'0o43'
>>> hex(35)
'0x23'
>>> oct(42)
'0o52'
>>> hex(42)
'0x2a'
>>> 7<<2
28
