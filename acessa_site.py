'''
Código de teste para uso do pyautogui, criado por thiagotsim em 13/06/2021
Este código foi criado para acessar de forma automática
sites quaisquer que necessitam de um login e senha.

Lembre-se:
1-Substituir os seusElementos correspondentes nas linhas requeridas
2-Enquanto o pyautogui estiver rodando não mexer em mouse ou teclado.
3-Este código pode não funcionar com qualquer site, pois as regiões
onde as informações de login e password devem ser inseridas
são diferentes para os diferentes sites, assim você terá que explorar
os recursos do pyautogui para ajustar ao seu caso em particular.

'''

# Importação das bibliotecas
import pyautogui as pyg
import time #módulo do python para funções de tempo

#0-opções de teclas para uso no pyautogui
#print(pyg.KEYBOARD_KEYS) 
# tire o # e execute a linha acima para ver as opções
# de teclas usáveis pelo pyautogui

print("Seu computador está em controle pelo python!!!")
#1- Pressionar tecla windows a esquerda
pyg.press('winleft')#meu caso a tecla win fica à esquerda
#2- Escreve chrome
pyg.write('chrome')
#3- Pressione enter
pyg.press('enter')
#3- Acessar gmail
time.sleep(1)
pyg.write("www.seuSite.com")#coloque o nome do site no lugar de seuSite
pyg.press('enter')
time.sleep(2)
#4-Mover o mouse para o icone do login
#print(pyg.position())
# executar a linha acima mostra a posição onde o mouse está
pyg.moveTo(767,216) # esta coordenada é um exemplo para a minha tela
pyg.click()
time.sleep(2)
#5- Digitar o email
pyg.write('seuEmail@xxxxx.com',interval=0.10)
# na linha acima digite qualquer email de seu uso
pyg.press('enter')
time.sleep(2)
#6- Digitar a senha
pyg.write('suaSenha',interval=0.10)
#substituir suaSenha pela senha de acesso ao site de interesse
pyg.press('enter')
print("Seu computador está de volta!!!")