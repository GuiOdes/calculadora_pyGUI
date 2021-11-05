# GUI
from PySimpleGUI import PySimpleGUI as sg

# funcao verifica se é numero
def isint(num):
    try:
        float(num)
    except:
        return False
    return True

# layout
class janela:
    def __init__(self):
        sg.theme('DarkAmber')

        layout = [
            [sg.Text("Número X: "), sg.Input(key="a", size=(10, 0))],
            [sg.Text("Número Y: "), sg.Input(key="b", size=(10, 0))],
            [sg.Radio('Somar', "op", default=True, key="Somar"), sg.Radio('Subtrair', "op", default=False, key="Subtrair"), sg.Radio('Multiplicar', "op", default=False, key="Multiplicar"), sg.Radio('Dividir', "op", default=False, key="Dividir")],
            [sg.Text('"Um pequeno passo para um homem."')],
            [sg.Button("Calcular")],
            [sg.Output(size=(20, 2), key='resp')]
        ]
        
        self.janela = sg.Window(title="Calculadora - Guilherme", layout=layout)

        # dados da tela

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.read()
            a = self.values['a']
            b = self.values['b']
            self.janela.FindElement('resp').Update('')
            if (a != "" and b != "" and isint(a) and isint(b)):
                # limpa output antes da operação

                # transformando dados em inteiros
                a = int(a)
                b = int(b)

                # pegando valores do radio
                somar = self.values['Somar']
                subtrair = self.values['Subtrair']
                multiplicar = self.values['Multiplicar']
                dividir = self.values['Dividir']
                
                # verificando operação
                if somar == True:
                    print(f'Resultado: {a+b}')
                elif subtrair == True:
                    print(f'Resultado: {a-b}')
                elif multiplicar == True:
                    print(f'Resultado: {a*b}')
                elif dividir == True:
                    print(f'Resultado: {a/b}')

            # caso o usuario nao tenha digitado algo
            else:
                print("Digite números válidos")


# escopo do projeto
tela = janela()
tela.Iniciar()