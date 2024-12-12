
login = input("Login: ")
senha = input("Senha: ")

if login == "pedro" and senha == "1234":
    print("Logado!")
else:
    print("Não logado!")



import PySimpleGUI as sg

def janela():
    titulo = [[sg.T('PORTE SCAN')]]
    janela = sg.Window('mey',titulo)
    while True:
        value, event = janela.read()
        if event == sg.WIN_CLOSED:
            break
        janela.close()

#janela()