 # from os import system
import sys
import keyboard
import pyautogui as pg
from tkinter import *

#Transformar em EXECUTÁVEL:
#pyinstaller macro_lancar_pedidos_tk.py --noconsole --onefile --icon=icone_macro.ico

janela = Tk()
janela.title('Legenda') #Título
janela.geometry('450x100') #Dimensão
janela.config(bg='white') #Configura a cor do Fundo
janela.resizable(width=False, height=False) # Não permite alteração na Largura e Altura
# janela.iconphoto(False, PhotoImage(file='icone_macro.ico')) # Ícone

fonte_geral = ('Arial 10 bold')
class Labels:
    def __init__(self, largura_cmd, altura_cmd, cmd, pos_x_cmd, pos_y_cmd, \
                 largura_texto, altura_texto, texto, fonte_texto, pos_x_texto, pos_y_texto):
        
        self.largura_cmd = largura_cmd
        self.altura_cmd = altura_cmd
        self.cmd = cmd
        self.pos_x_cmd = pos_x_cmd
        self.pos_y_cmd= pos_y_cmd

        self.largura_texto = largura_texto
        self.altura_texto = altura_texto
        self.texto= texto
        self.fonte_texto= fonte_texto
        self.pos_x_texto = pos_x_texto
        self.pos_y_texto = pos_y_texto

    def cria_label_cmd(self):
        label = Label(janela, width=self.largura_cmd, height=self.altura_cmd, text=self.cmd)
        label.place(x=self.pos_x_cmd, y=self.pos_y_cmd)
        label_texto = Label(janela, width=self.largura_texto, height=self.altura_texto, text=self.texto, font=self.fonte_texto)
        label_texto.place(x=self.pos_x_texto, y=self.pos_y_texto)


label_baixa = Labels(5, 2, 'F1', 10, 10, \
                  5, 1, 'Baixa', fonte_geral, 10, 50)

label_sobe = Labels(5, 2, 'F2', 60, 10, \
                  5, 1, 'Sobe', fonte_geral, 60, 50)

label_caixa_pesos = Labels(5, 2, 'F3', 110, 10, \
                  5, 1, 'Caixa', fonte_geral, 110, 50)

label_conclui = Labels(5, 2, 'F5', 165, 10, \
                  6, 1, 'Conclui', fonte_geral, 160, 50)

label_lanca = Labels(5, 2, 'F6', 215, 10, \
                  5, 1, 'Lança', fonte_geral, 215, 50)

label_pendente = Labels(6, 2, 'CRLT+F', 270, 10, \
                  7, 1, 'Pendente', fonte_geral, 265, 50)

label_cliente_retira = Labels(6, 2, '"', 330, 10, \
                  5, 1, 'Retira', fonte_geral, 335, 50)

label_altera= Labels(6, 2, '\\', 390, 10, \
                  7, 1, 'Altera', fonte_geral, 380, 50)


label_baixa.cria_label_cmd()
label_sobe.cria_label_cmd()
label_caixa_pesos.cria_label_cmd()
label_conclui.cria_label_cmd()
label_lanca.cria_label_cmd()
label_pendente.cria_label_cmd()
label_cliente_retira.cria_label_cmd()
label_altera.cria_label_cmd()


def fecha_programa():
    sys.exit()

botao_fechar = Button(janela, text='Fechar', command=fecha_programa)
botao_fechar.place(x=390, y= 75)

def altera_dia_de_lancamento():
    pass

var1 = IntVar()
check_lanca_pen = Checkbutton(janela, text="Dia Seg", variable=var1, onvalue=1, offvalue=0, command=altera_dia_de_lancamento)
check_lanca_pen.place(x=207, y=75)

print('Macro Ligado...')

def clica1(x  , y  , dur ):
    pg.leftClick(x, y, duration=dur)

def clica2(x  , y  , dur ):
    pg.doubleClick(x, y, duration=dur)
    
def comando(key, function):
    keyboard.add_hotkey(key, function)

def baixa_item():
    clica1(930, 235, 0   )
    
def sobe_item():
    clica2(528, 297, 0   )

def abre_caixa_de_pesos():
    clica1(346, 226, 0   )

def altera_pedido():
    clica1(141, 109, 0   )
    clica1(496, 144, 0.1 )

def fecha_pedido_com_peso():
    clica1(147, 578, 0.10)
    clica1(365, 467, 0.25)
    clica1(388, 104, 0.20)
    clica1(857, 512, 0.25)
    clica1(857, 512, 0.25)
    clica1(857, 512, 0.25)
    clica1(902, 103, 0   )

def fecha_pedido_com_preco_novo():
    clica1(388, 104, 0   )
    clica1(857, 512, 0.75)
    clica1(857, 512, 0.25)
    clica1( 64, 106, 0.20)
    
    if (var1.get() == 1):
        pg.hotkey('up')
        pg.hotkey('tab')
        pg.hotkey('tab')

def fecha_pedido_com_preco_pendente():
    clica1(388, 104, 0   )
    clica1(857, 512, 0.75)
    clica1(857, 512, 0.25)
    clica1(893, 109, 0.25)

def cliente_retira():
    clica2(120, 418, 0  )
    pg.hotkey('up')
    clica2(509, 146, 0  )
    clica2( 77, 208, 0  )

def abre_pedido():
    clica2(794, 150, 0  )
    clica2(930, 235, 0  )


comando('f1', baixa_item) # Baixa um item no pedido
comando('f2', sobe_item)  # Sobe item no pedido
comando('f3', abre_caixa_de_pesos) # Abre a caixa de pesos
comando('\\', altera_pedido) # Altera Pedido
comando('f5', fecha_pedido_com_peso) # Autodescritivo
comando('f6', fecha_pedido_com_preco_novo) # Autodescritivo
comando('ctrl+f', fecha_pedido_com_preco_pendente) # Autodescritivo
comando('\'', cliente_retira) # Cliente Retira 
# comando('f7', abre_pedido) # Abre pedido clicando duas vezes 


janela.mainloop()
keyboard.wait()
