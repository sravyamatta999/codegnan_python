Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#set
#to define empty set -->set()
n={}
type(n)
<class 'dict'>
n=set()
type(n)
<class 'set'>
n=set(1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    n=set(1,2,3,4,5)
TypeError: set expected at most 1 argument, got 5
n=set([1,2,50,4,90]
      print(n)
      
SyntaxError: '(' was never closed
KeyboardInterrupt
n=set([1,2,50,4,90])
      
print(n)
      
{1, 2, 4, 50, 90}
n=set([30,3,10,46,58])
      
print(n)
      
{3, 10, 46, 58, 30}
#so the o/p is inordered , no indexing ,it doesn't allow duplicates.
      
x={True,1}
      
print(x)
      
{True}
x={1,True}
      
print(x)
      
{1}
#soo the o/p will be the first element
      
n=set((1,2,3,4,5))
      
print(n)
      
{1, 2, 3, 4, 5}
n=set ({1,2,3,4,5})
      
print(n)
      
{1, 2, 3, 4, 5}
#so in set() we can give flower brackets,square brackets or tuple it gives the o/p
      
#i can check that using type()
      
print(type(n))
      
<class 'set'>
n=set((1,2,3,4,5))
      
print(type(n))
      
<class 'set'>
x={1,45,60}
      
print(type(x))
      
<class 'set'>

========== RESTART: C:/Users/sravya/Desktop/Codegnan_python/1st_oct_script.py =========
{1, 2, 3}

========== RESTART: C:/Users/sravya/Desktop/Codegnan_python/1st_oct_script.py =========
{1, 2, 3}
Traceback (most recent call last):
  File "C:/Users/sravya/Desktop/Codegnan_python/1st_oct_script.py", line 9, in <module>
    print(n.remove(4))
KeyError: 4

========== RESTART: C:/Users/sravya/Desktop/Codegnan_python/1st_oct_script.py =========
{1, 2, 3}
Traceback (most recent call last):
  File "C:/Users/sravya/Desktop/Codegnan_python/1st_oct_script.py", line 9, in <module>
    print(n.remove(4))
KeyError: 4

========== RESTART: C:/Users/sravya/Desktop/Codegnan_python/1st_oct_script.py =========
{1, 2, 3}
1

========== RESTART: C:/Users/sravya/Desktop/Codegnan_python/1st_oct_script.py =========
{1, 2, 3}
1
{2, 3}

========== RESTART: C:/Users/sravya/Desktop/Codegnan_python/1st_oct_script.py =========
{1, 2, 3}
1
{2, 3}
Traceback (most recent call last):
  File "C:/Users/sravya/Desktop/Codegnan_python/1st_oct_script.py", line 15, in <module>
    print(n.discard(5))
AttributeError: 'list' object has no attribute 'discard'

========== RESTART: C:/Users/sravya/Desktop/Codegnan_python/1st_oct_script.py =========
{1, 2, 3}
1
{2, 3}
None

========== RESTART: C:/Users/sravya/Desktop/Codegnan_python/1st_oct_script.py =========
{1, 2, 3}
1
{2, 3}
None
{1, 2, 3, 4, 30}

========== RESTART: C:/Users/sravya/Desktop/Codegnan_python/1st_oct_script.py =========
{1, 2, 3}
1
{2, 3}
None
{1, 2, 3, 4, 30}
Traceback (most recent call last):
  File "C:/Users/sravya/Desktop/Codegnan_python/1st_oct_script.py", line 20, in <module>
    n.update(30,40)
TypeError: 'int' object is not iterable

========== RESTART: C:/Users/sravya/Desktop/Codegnan_python/1st_oct_script.py =========
{1, 2, 3}
1
{2, 3}
None
{1, 2, 3, 4, 30}
{1, 2, 3, 4, 40, 30}

========== RESTART: C:/Users/sravya/Desktop/Codegnan_python/1st_oct_script.py =========
{1, 2, 3}
1
{2, 3}
None
{1, 2, 3, 4, 30}
{1, 2, 3, 4, 40, 30}

========== RESTART: C:/Users/sravya/Desktop/Codegnan_python/1st_oct_script.py =========
{1, 2, 3}
1
{2, 3}
None
{1, 2, 3, 4, 30}
{1, 2, 3, 4, 40, 30}
{1, 2, 3, 4, 40, 30}

========== RESTART: C:/Users/sravya/Desktop/Codegnan_python/1st_oct_script.py =========
{1, 2, 3}
1
{2, 3}
None
{1, 2, 3, 4, 30}
{1, 2, 3, 4, 40, 30}
{1, 2, 3, 4, 40, 30}

========== RESTART: C:/Users/sravya/Desktop/Codegnan_python/1st_oct_script.py =========
{1, 2, 3}
1
{2, 3}
None
{1, 2, 3, 4, 30}
{1, 2, 3, 4, 40, 30}
{1, 2, 3, 4, 40, 30}
{1, 2, 3, 4, 70, 40, 60, 30}
n=[1,2,3,4]
      
n.add(40)
      
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    n.add(40)
AttributeError: 'list' object has no attribute 'add'
n.add([40])
      
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    n.add([40])
AttributeError: 'list' object has no attribute 'add'
n.add({40}]
      
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
n.add({40})
      
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    n.add({40})
AttributeError: 'list' object has no attribute 'add'
>>> n=set({1,2,3,4})
...       
>>> n.add(5)
...       
>>> print(n)
...       
{1, 2, 3, 4, 5}
>>> n.add(5,7,8)
...       
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    n.add(5,7,8)
TypeError: set.add() takes exactly one argument (3 given)
>>> n.add((5,6,7,8))
...       
>>> print(n)
...       
{1, 2, 3, 4, 5, (5, 6, 7, 8)}
>>> n.add([9,1,5,9])
...       
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    n.add([9,1,5,9])
TypeError: unhashable type: 'list'
>>> 
========== RESTART: C:/Users/sravya/Desktop/Codegnan_python/1st_oct_script.py =========
{1, 2, 3}
1
{2, 3}
None
{1, 2, 3, 4, 30}
{1, 2, 3, 4, 40, 30}
{1, 2, 3, 4, 40, 30}
{1, 2, 3, 4, 70, 40, 60, 30}
False
>>> 
========== RESTART: C:/Users/sravya/Desktop/Codegnan_python/1st_oct_script.py =========
5 1 5 15
[1, 2, 3, 4, 5]
{1, 2, 3, 4, 5}
>>> 
========== RESTART: C:/Users/sravya/Desktop/Codegnan_python/1st_oct_script.py =========
1,2,3,4,5
>>> 
========== RESTART: C:/Users/sravya/Desktop/Codegnan_python/1st_oct_script.py =========
1,2,3,4,5
[1, 2, 3, 4, 5]
>>> 
========== RESTART: C:/Users/sravya/Desktop/Codegnan_python/1st_oct_script.py =========
1 2 3 4 5
Traceback (most recent call last):
  File "C:/Users/sravya/Desktop/Codegnan_python/1st_oct_script.py", line 53, in <module>
    n=list(map(int,input().split(",")))
ValueError: invalid literal for int() with base 10: '1 2 3 4 5'
