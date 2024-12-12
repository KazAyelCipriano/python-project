Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # Strings e Listas
>>> nome = "Pedro"
>>> print(type(nome))
<class 'str'>
>>> print(nome)
Pedro
>>> print(nome[0])
P
>>> print(nome[1])
e
>>> print(nome[0:5])
Pedro
>>> print(nome[2:4])
dr
>>> print(nome[-1])
o
>>> print(nome[-5:4])
Pedr
>>> 
>>> list = [80, 443, 445]
>>> print(type(list))
<class 'list'>
>>> lista = [80, 443, 445 , 999 ]
>>> print(type(lista))
<class 'list'>
>>> lista2 = ["Pedro", "Silva", "Cipriano"]
>>> print(lista2[1])
Silva
>>> print(lista2[0])
Pedro
>>> print(lista2[3])
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(lista2[3])
IndexError: list index out of range
>>> print(lista2[0:2])
['Pedro', 'Silva']
>>> print(lista2[0:3])
['Pedro', 'Silva', 'Cipriano']
>>> lista2.remove("Silva")
>>> print(lista2[0:3])
['Pedro', 'Cipriano']
>>> lista2.append("Santos", "Pinheiro")
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    lista2.append("Santos", "Pinheiro")
TypeError: list.append() takes exactly one argument (2 given)
>>> lista2.append("Pinheiro")
>>> print(lista2[0:3])
['Pedro', 'Cipriano', 'Pinheiro']
