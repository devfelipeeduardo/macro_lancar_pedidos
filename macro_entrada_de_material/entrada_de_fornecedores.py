import pyautogui as pg
import keyboard

vel = 0.1

#Macros
def clica_esq(x, y, z):
    pg.leftClick(x, y, duration = z)
def clica_duas(x, y, z):
    pg.doubleClick(x, y, duration = z)      
def escreve(x, y, z):
    pg.write(x, y, interval = z)
#

#Conjuntos

def preco():
    clica_esq(664, 350, 0) #clica no preço

def codigo():
    clica_esq(52, 343, 0) #Clica para inserir código


def num_notafiscal():
    clica_esq(645, 247, 0) #Clica para inserir código

def inclui():
    clica_esq(71, 109, vel) #inclui
    clica_esq(650, 197, vel) #contabil
    clica_esq(786, 198, vel) #imposto não
    clica_duas(425, 256, vel) #produto/revenda
    pg.hotkey('down') #
    clica_duas(177, 167, vel) #Mini-Nome

def valor_produto1():
    clica_duas(88, 292, vel) #Valor Produto 1

def valor_produto2():
    clica_duas(809, 293, vel) #Valor Produto 2


keyboard.add_hotkey('f1', preco) 
keyboard.add_hotkey('f2', codigo) 
keyboard.add_hotkey('f3', num_notafiscal)
keyboard.add_hotkey('\'', inclui)
keyboard.add_hotkey('f5', valor_produto1)
keyboard.add_hotkey('f6', valor_produto2)

keyboard.wait()