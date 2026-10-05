Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name="pardhu"
print("name take some break")
name take some break
print(f"{name} take some break")
pardhu take some break
wish="Good morning"
print(f"{name} {wish})
      
SyntaxError: unterminated string literal (detected at line 1)
print(f"{name} {wish}")
      
pardhu Good morning
name="neha"
      
wish=
      
SyntaxError: invalid syntax
name="babu"
      
salary="200000
      
SyntaxError: unterminated string literal (detected at line 1)
name="babu"
      
salary="200000"
      
print(f"{name} your salary is {salary}")
      
babu your salary is 200000
print("%s your salary is %d%"(name,salary)")
      
SyntaxError: unterminated string literal (detected at line 1)
print("%s your salary is %d%"(name,salary))
      
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print("%s your salary is %d%"(name,salary))
TypeError: 'str' object is not callable
print("%s your salary is %d%"%(name,salary))
      
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print("%s your salary is %d%"%(name,salary))
TypeError: %d format: a real number is required, not str
w="python"
      
print(w+"developer")
      
pythondeveloper
w*"python"
      
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    w*"python"
TypeError: can't multiply sequence by non-int of type 'str'
w*5
      
'pythonpythonpythonpythonpython'
"a">"b"
      
False
a>b
      
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a>b
NameError: name 'a' is not defined
a=10
      
b=20
      
a>b
      
False
name="xyz"
      
salary="2345"
      
#collection datatypes
      

====== RESTART: C:/Users/sravya/Desktop/Codegnan_python/30thsept_collection_dt.py =====
[1, 'john', 2]
n=[1,1,1,1,1]
      
n
      
[1, 1, 1, 1, 1]
l=[]
      
type(l)
      
<class 'list'>
l=[1,"ashish"]
      
#append,insert,extend
      
#append means adds in the list
      
l.append("python")
      
l
      
[1, 'ashish', 'python']
l.append("bsc",2)
      
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    l.append("bsc",2)
TypeError: list.append() takes exactly one argument (2 given)
TypeError: list.append() takes exactly one argument (2 given)
      
SyntaxError: invalid syntax
l.append(["bsc",2])
      
>>> l
...       
[1, 'ashish', 'python', ['bsc', 2]]
>>> #if we have to add more than one argument and don't need nested list
...       
>>> l.extend(["bsc",2])
...       
>>> l
...       
[1, 'ashish', 'python', ['bsc', 2], 'bsc', 2]
>>> l.insert(1,"pes")
...       
>>> l
...       
[1, 'pes', 'ashish', 'python', ['bsc', 2], 'bsc', 2]
>>> 
>>> #pop
...       
>>> l
...       
[1, 'pes', 'ashish', 'python', ['bsc', 2], 'bsc', 2]
>>> l.pop()
...       
2
>>> l
...       
[1, 'pes', 'ashish', 'python', ['bsc', 2], 'bsc']
>>> #pop removes the last element of list
...       
>>> l.pop(0)
...       
1
>>> l
...       
['pes', 'ashish', 'python', ['bsc', 2], 'bsc']
>>> #if we pass inderx value to the pop method it removes that particualr index value element
...       
>>> #if we don't know the index value but want to remove particular element then use remove #()
...       
>>> x=[10,20,20,30,40]
...       
>>> a=[10,20,30,40,20,50]
...       
>>> x=20
...       
>>> i=a.index(x)
...       
>>> a.remove(x)
...       
>>> a.remove(x)
...       
>>> a.insert(i,x)
...       
>>> print(a)
...       
[10, 20, 30, 40, 50]
