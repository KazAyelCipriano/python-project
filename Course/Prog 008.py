
'''
-   OS : Windows 10
-   CPU : Intel Core i9
-   Armazenamento : 4
-   Memória : 64

-   OS : Windows 10
-   CPU : Intel Core i9
-   Armazenamento : 8
-   Memória : 64

-   OS : Windows 11
-   CPU : Intel Core i7
-   Armazenamento : 2
-   Memória : 12

print(f"Configurações do Computador\n\t- Sistema Operacional: {os1}\n\t- CPU: {cpu1}\n\t- Armazenamento: {armazen1}T"\n\t- Memória: {memoria1}G)
print(f"Configurações do Computador\n\t- Sistema Operacional: {os2}\n\t- CPU: {cpu2}\n\t- Armazenamento: {armazen2}T"\n\t- Memória: {memoria2}G)
print(f"Configurações do Computador\n\t- Sistema Operacional: {os3}\n\t- CPU: {cpu3}\n\t- Armazenamento: {armazen3}T"\n\t- Memória: {memoria3}G)

'''
import os


def montar_computador(os = "", cpu = "", armazenamento = "", memoria = ""):
    print(f"Configurações do Computador\n\t- Sistema Operacional: {os}\n\t- CPU: {cpu}\n\t- Armazenamento: {armazenamento}\n\t- Memória: {memoria}\n\n")

montar_computador("Windows 10", "Intel i9", 4, 64)
montar_computador("Windows 10", "Intel i9", 8, 64)
montar_computador("Windows 11", "Intel i7", 2, 12)