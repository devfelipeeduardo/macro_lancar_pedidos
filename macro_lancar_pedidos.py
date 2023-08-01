import os
import keyboard
import pyautogui as pg

os.system('cls')

print('Macro Ligado...')

def clica1(x  , y  , dur ):
    pg.leftClick(x, y, duration=dur)

def clica2(x  , y ,  dur ):
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


comando('f1', baixa_item) # Baixa um item no pedido
comando('f2', sobe_item)  # Sobe item no pedido
comando('f3', abre_caixa_de_pesos) # Abre a caixa de pesos
comando('\\', altera_pedido) # Altera Pedido
comando('f5', fecha_pedido_com_peso) # Autodescritivo
comando('f6', fecha_pedido_com_preco_novo) # Autodescritivo
comando('ctrl+f', fecha_pedido_com_preco_pendente) # Autodescritivo
comando('\'', cliente_retira) # Cliente Retira 



keyboard.wait()
