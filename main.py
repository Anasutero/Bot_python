#Importe da melhor biblioteca para realizar RPA , e tempo que quero para fazer as tarefas.
import  pyautogui
import time
pyautogui.PAUSE=1


# 1- passo entrar no site da empresa:

# comando press para precionar uma tecla automaticamente (nesse caso o windows)    
pyautogui.press("win") 

# comando write ,  para escrever o nome do programa que queremos entrar 
pyautogui.write("chrome")

# comando utilizado para entrar no chrome
pyautogui.press("enter")

#para ele entrar no link de cadastramento da "empresa"
link= "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)

pyautogui.press("enter")

time.sleep(2)      


# 2- passo fazer login no site:

#encontrando a posição para digitar o e-mail
pyautogui.click(x=767, y=371)

pyautogui.write("python.automation@gmail.com")

#slecionando o tab para ele ir para baixo e escrever a senha
pyautogui.press("tab")

pyautogui.write("minha senha")

#encontrando a posição para clicar no botao de logar e ir para a proxima tela
pyautogui.click(x=954, y=532)

#3-passo importando a base de dados:
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

#4-passo cadastrando  os produtos:
for linha in tabela.index:
    pyautogui.click(x=869, y=244)

    #pegando os dados da tabela , para nao reptir sempre com o mesmo
    codigo=tabela.loc[linha,"codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha,"marca"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha,"tipo"])
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")

    obs=tabela.loc[linha,"obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
 
    #clicar no enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)

   


















