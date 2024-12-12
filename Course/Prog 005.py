Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

#Condicionais, tipos e variáveis

lista = ["Pedro", "Cipriano", "Silva"]
lista.remove("Silva")
lista.remove("Pedro")
lista.append("Santos")
lista.append("SILVA")
print(lista[0:3])
['Cipriano', 'Santos', 'SILVA']

#Comparação
#  == !=  >=  <=  >  <
# and   or

1 == 1
True
9>11
False
1!=2
True
1<=2
True
1<=1
True
lista[0]==lista[1]
False
lista,append("Silva")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    lista,append("Silva")
NameError: name 'append' is not defined
lista.append("Silva")
print(lista[0:4])
['Cipriano', 'Santos', 'SILVA', 'Silva']
lista[3]==lista[4]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    lista[3]==lista[4]
IndexError: list index out of range
print(lista[2])
SILVA
print(lista[3])
Silva
lista[2]==lista[3]
False

valor_1 = True
valor_2 = False

if 2 == 2:
    print(valor_1)
else:
    print(valor_2)

True
if 2 == 1:
    print(valor_1)
else:
    print(valor_2)

False
numero_1 = input("Digite um numero: ")
Digite um numero: 45
numero_2 = input("Digite um outro numero: ")
Digite um outro numero: 57
if numero_1 == numero_2:
    print(valor_1)
else:
    print(valor_2)

False
if numero_1 != numero_2 :
    print(valor_1)
else:
    print(valor_2)

True

idade = input("Digite uma idade")
Digite uma idade32
if idade <= str(12):
    print("Você é uma criança")
elif idade <= str(18):
    print("Você é um adolescente")
elif idade <= str(50):
    print("Você é um adulto")
else:
    print("Você é um velho")

Você é um adulto
print(idade)
32

valor = 20
porcentagem = 100
valor_total = 30
resultado = (valor/porcentagem)*valor_total
print(resultado)
6.0
>>> 
>>> nota = input("Digite sua nota: ")
Digite sua nota: 9
>>> 
>>> if nota >= 6:
...     print("Aprovado")
... else
SyntaxError: expected ':'
>>> else:
...     
SyntaxError: invalid syntax
>>> 
>>> 
>>> if nota >= 6:
...     print("Aprovado")
... else:
...     print("Reprovado")
... 
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    if nota >= 6:
TypeError: '>=' not supported between instances of 'str' and 'int'
>>> 
>>> if nota >= str(6):
...     print("Aprovado")
... else:
...     print("Reprovado")
... 
Aprovado
>>> 
>>> nota = int(nota)
>>> print(nota)
9
>>> if nota >= 6:
...     print("Aprovado")
... else:
...     print("Reprovado")
... 
Aprovado
>>> 
>>> login = "kaz"
>>> senha = "123456"
>>> 
>>> of login == "kaz" and senha == "123456":
...     
SyntaxError: invalid syntax
>>> 
>>> if login == "kaz" and senha == "123456":
...     print("Logado")
... else:
...     print("Não logado")
... 
Logado
>>> 
>>> login = input("Login: ")
Login: KAZ
>>> senha = input("Senha: ")
Senha: 654321
>>> 
