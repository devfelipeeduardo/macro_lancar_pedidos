 # from os import system
import os
import sys
import keyboard
import pyautogui as pg
from tkinter import *

#Transformar em EXECUTÁVEL:
#pyinstaller macro_lancar_pedidos_tk.py --noconsole --onefile --icon=icone_macro.ico

janela = Tk()
janela.title('Legenda') #Título
janela.geometry('500x100') #Dimensão
janela.config(bg='white') #Configura a cor do Fundo
janela.resizable(width=False, height=False) # Não permite alteração na Largura e Altura
# janela.iconphoto(False, PhotoImage(file='icone_macro.ico')) # Ícone

fonte_geral = ('Arial 10 bold')
class Labels:
    def __init__(self, largura_cmd,
                        altura_cmd,
                        cmd,
                        pos_x_cmd,
                        pos_y_cmd,
                        largura_texto,
                        altura_texto,
                        texto,
                        fonte_texto,
                        pos_x_texto,
                        pos_y_texto
                        ):
        
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

    def cria_label(self):
        label = Label(janela, width=self.largura_cmd, height=self.altura_cmd, text=self.cmd)
        label.place(x=self.pos_x_cmd, y=self.pos_y_cmd)
        label_texto = Label(janela, width=self.largura_texto, height=self.altura_texto, text=self.texto, font=self.fonte_texto)
        label_texto.place(x=self.pos_x_texto, y=self.pos_y_texto)


label_baixa = Labels(largura_cmd=5, 
                             altura_cmd = 2,
                             cmd ='F1',
                             pos_x_cmd=10,
                             pos_y_cmd=10,
                             largura_texto= 5,
                             altura_texto=1,
                             texto= 'Baixa',
                             fonte_texto= fonte_geral,
                             pos_x_texto=10,
                             pos_y_texto= 50)

label_sobe = Labels(largura_cmd=5,
                              altura_cmd = 2,
                              cmd ='F2', 
                              pos_x_cmd=60,
                              pos_y_cmd=10, \
                              largura_texto= 5,
                              altura_texto=1,
                              texto= 'Sobe',
                              fonte_texto=fonte_geral, 
                              pos_x_texto=60,  
                              pos_y_texto= 50)

label_caixa_pesos = Labels(largura_cmd=5,
                              altura_cmd = 2,
                              cmd ='F3', 
                              pos_x_cmd=110,
                              pos_y_cmd=10, \
                              largura_texto= 5,
                              altura_texto=1,
                              texto= 'Caixa',
                              fonte_texto=fonte_geral, 
                              pos_x_texto=110, 
                              pos_y_texto= 50)

label_conclui = Labels(largura_cmd=5,
                              altura_cmd = 2,
                              cmd ='F5', 
                              pos_x_cmd=165,
                              pos_y_cmd=10, \
                              largura_texto= 6,
                              altura_texto=1,
                              texto= 'Conclui',
                              fonte_texto=fonte_geral, 
                              pos_x_texto=160,
                              pos_y_texto= 50)

label_lanca = Labels(largura_cmd=5,
                              altura_cmd = 2,
                              cmd ='F6', 
                              pos_x_cmd=215,
                              pos_y_cmd=10, \
                              largura_texto= 5,
                              altura_texto=1,
                              texto= 'Lança',
                              fonte_texto=fonte_geral, 
                              pos_x_texto=215,
                              pos_y_texto= 50)

label_pendente = Labels(largura_cmd=6,
                              altura_cmd = 2,
                              cmd ='CRLT+F', 
                              pos_x_cmd=270,
                              pos_y_cmd=10, \
                              largura_texto= 7,
                              altura_texto=1,
                              texto= 'Pendente',
                              fonte_texto=fonte_geral, 
                              pos_x_texto=265,
                              pos_y_texto= 50)

label_cliente_retira = Labels(largura_cmd=6,
                              altura_cmd = 2,
                              cmd ='"', 
                              pos_x_cmd=330,
                              pos_y_cmd=10, \
                              largura_texto= 5,
                              altura_texto=1,
                              texto= 'Retira',
                              fonte_texto=fonte_geral, 
                              pos_x_texto=335,
                              pos_y_texto= 50)

label_altera= Labels(largura_cmd=6,
                              altura_cmd = 2,
                              cmd = '\\', 
                              pos_x_cmd =390,
                              pos_y_cmd =10, \
                              largura_texto = 7,
                              altura_texto =1,
                              texto = 'Altera',
                              fonte_texto= fonte_geral, 
                              pos_x_texto= 380,
                              pos_y_texto= 50)

label_escreve_devolucao= Labels(largura_cmd = 6,
                              altura_cmd = 2,
                              cmd = 'F12',
                              pos_x_cmd = 450,
                              pos_y_cmd =10, \
                              largura_texto = 7,
                              altura_texto= 1,
                              texto = 'Devol.',
                              fonte_texto= fonte_geral, 
                              pos_x_texto= 440,
                              pos_y_texto= 50)


label_baixa.cria_label()
label_sobe.cria_label()
label_caixa_pesos.cria_label()
label_conclui.cria_label()
label_lanca.cria_label()
label_pendente.cria_label()
label_cliente_retira.cria_label()
label_altera.cria_label()
label_escreve_devolucao.cria_label()


def fecha_programa():
    sys.exit()

botao_fechar = Button(janela, 
                      text='Fechar', 
                      command=fecha_programa)

botao_fechar.place(x=390, y= 75)

var1 = IntVar()
check_lanca_pen = Checkbutton(janela,
                              text="Dia Seg",
                              variable=var1,
                              onvalue=1, offvalue=0)

check_lanca_pen.place(x=207, y=75)

var2 = IntVar()
check_baixa_ent = Checkbutton(janela,
                              text="f1_ent",
                              variable=var2, 
                              onvalue=1, offvalue=0)

check_baixa_ent.place(x=0, y=75)

print('Macro Ligado...')

def clica1(x  , y  , dur ):
    pg.leftClick(x, y, duration=dur)

def clica2(x  , y  , dur ):
    pg.doubleClick(x, y, duration=dur)
    
def comando(key, function):
    keyboard.add_hotkey(key, function)

def baixa_item():

    if var2.get() == 0:
        clica1(930, 235, 0)
    elif var2.get() == 1:
        clica1(653, 342, 0)
    

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

def escreve_devolucao():
    pg.write("DEVOLUCAO PARCIAL REFERENTE A NOTA FISCAL N°  EMISSAO:  ")
     
def marca_10_quadrados_cte():
    pg.hotkey('space')
    pg.hotkey('down')
    pg.hotkey('space')
    pg.hotkey('down')
    pg.hotkey('space')
    pg.hotkey('down')
    pg.hotkey('space')
    pg.hotkey('down')
    pg.hotkey('space')
    pg.hotkey('down')
    pg.hotkey('space')
    pg.hotkey('down')
    pg.hotkey('space')
    pg.hotkey('down')
    pg.hotkey('space')
    pg.hotkey('down')
    pg.hotkey('space')
    pg.hotkey('down')
    pg.hotkey('space')
    pg.hotkey('down')
    

# def reinicia_macro():
#     python = sys.executable
#     os.execl(python, python, * sys.argv)


comando('f1', baixa_item) # Baixa um item no pedido
comando('f2', sobe_item)  # Sobe item no pedido
comando('f3', abre_caixa_de_pesos) # Abre a caixa de pesos
comando('\\', altera_pedido) # Altera Pedido
comando('f5', fecha_pedido_com_peso) # Autodescritivo
comando('f6', fecha_pedido_com_preco_novo) # Autodescritivo
comando('ctrl+f', fecha_pedido_com_preco_pendente) # Autodescritivo
comando('f12', escreve_devolucao) # Autodescritivo
comando('\'', cliente_retira) # Cliente Retira 
# comando('f10', reinicia_macro) # Teste para reiniciar o macro, mas não reinicia! 
comando('f11', marca_10_quadrados_cte) # Cliente Retira 
# comando('f7', abre_pedido) # Abre pedido clicando duas vezes 


janela.mainloop()
keyboard.wait()
