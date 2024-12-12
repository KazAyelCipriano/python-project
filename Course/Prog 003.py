Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> n1 = 1
>>> n2 = 1
>>> if n1==n2: print("Verdadeiro") else print("Falso")
SyntaxError: invalid syntax
>>> if n1==n2:
...     print("Verdadeiro")
... else :
...     print("Falso")
... 
Verdadeiro
>>> if n1=!n2:
...     
SyntaxError: invalid syntax
>>> n2=2
>>> for n in n1:
...     print(n1)
... 
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    for n in n1:
TypeError: 'int' object is not iterable
>>> n1=(80,443)
>>> for n in n1:
...     print(n)
... 
80
443
>>> n1=80,443,445)
SyntaxError: unmatched ')'
>>> n1 = (80,443,445)
>>> for n in n1:
...     print(f"Open: {n}")
... 
Open: 80
Open: 443
Open: 445
