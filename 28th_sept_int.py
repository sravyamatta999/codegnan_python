Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
b=20
a is b
False
c=10
a is c
True
id (a),id(c)
(1671642415632, 1671642415632)
a=20
a is b
True
a is c
False
a is not b
False
a is not c
True
print ( a is b)
True
bin(16)
'0b10000'
print(what's your name")
      
SyntaxError: unterminated string literal (detected at line 1)
print("what's your name")
      
what's your name
print('what's your name ')
      
SyntaxError: unterminated string literal (detected at line 1)
s='I am a "python developer"'
      
s
      
'I am a "python developer"'
n="codegnan"
      
n[0]
      
'c'
n[5]
      
'n'
n[-3]
      
'n'
n[-1]
      
'n'
n[-4]
      
'g'
n="code gnan"
      
n[5]
      
'g'
n[4]
      
' '
n[-5]
      
' '
x="code gnan"
      
x[0:4]
      
'code'
x[0:4:1]
      
'code'
x[5:9:1]
      
'gnan'
x[5:9]
...       
'gnan'
>>> x[:9]
...       
'code gnan'
>>> x[5:9:2]
...       
'ga'
>>> x[5::1]
...       
'gnan'
>>> x[5::]
...       
'gnan'
>>> x{5:]
...       
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> x[5:]
...       
'gnan'
>>> n="Raghuveer"
...       
>>> n[-5:-10:-1]
...       
'uhgaR'
>>> n[5:-1:-1]
...       
''
>>> n[4:0:-1]
...       
'uhga'
>>> 'uhga'
...       
'uhga'
>>> n[5:-10:-1]
...       
'vuhgaR'
>>> n[4:-10:-1]
...       
'uhgaR'
>>> n[4:-1:-1]
...       
''
>>> ''
...       
''
>>> n[8:-10:-1]
...       
'reevuhgaR'
>>> n[::-1]
...       
'reevuhgaR'
>>> n[::-2]
...       
'reugR'
>>> n[-3::-1]
...       
'evuhgaR'
