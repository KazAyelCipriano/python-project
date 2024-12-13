login = input("Login: ")
senha = input("Senha: ")

def loginver(login, senha):
    if login == "pedro" and senha == "1234":
        print("Logado!")
    else:
        print("Não logado!")

def imprimir_dados(nome = ""):
    print(f"Meu nome é {nome}")

imprimir_dados(login)
loginver(login, senha)