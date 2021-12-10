from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.common.action_chains import ActionChains
import re

bombs=99              #usar global para alterar estas variaveis dentro de funcoes
max_lin=16
max_col=30

#class base da matriz que representa o tabuleiro do jogo
class square:
    def __init__(self):
        self.value=-1                              #-1:valor de inicialização(square por abrir);0:aberto sem nada adjacente;1-8: bombas adjacentes
        self.subtract=0
        self.flag=False                            #True-Falgged; False-not Flaggged

#da update da matriz squares(representa o tabuleiro de jogo em valores numericos)
def update(squares):
    for l in range(1,max_lin+1):   #nao esquecer que para a matriz tera que ser l-1 para começar em 0, o mesmo para o c <--------------------
        for c in range(1,max_col+1):
            id=str(l)+"_"+str(c)
            args=(By.ID, id)
            element=driver.find_element(*args)
            val_sq=element.get_attribute("class")                 #obtem o argumento referente ao valor que o square apresenta
            if val_sq!="square blank":
                squares[l-1][c-1].value=re.sub("\D", "", val_sq)     #retira apenas a parte numerica do argumento do square e mete na matriz (se demorar muito tempo podera ser possivel verificar se o valor novo e diferente do ja presente na matriz mas n sei se ajuda muito)

#def maxProb(squares):



#variave iter indica se se trata da primiera iteracão (iter=1) ou nãp (iter=0)
def solver(iter):

    #selecionar primeiro square id="x_y"
    x=random.randint(1,max_lin)
    y=random.randint(1,max_col)

    id=str(x)+"_"+str(y)
    print(id)
    args=(By.ID, id)

    if iter==1:
        first=driver.find_element(*args) #necessario garantir que o first ja n esta aberto (por causa da recursão)
        squares=[[-1]*max_col]*max_lin   #inicializa a lista na primeira iteracão
        for L in range(0,max_lin):
            for C in range(0,max_col):
                squares[L][C]=square()

    else:
        if condition:
            pass
        pass
    #clicka no first
    actions=ActionChains(driver)
    actions.move_to_element(first).click()
    actions.perform()

    #update dos valores no squares abertos
    update(squares)

    for L in range(0,max_lin):
        for C in range(0,max_col):
            print(squares[L][C].value)
    #enontrar um 1 num canto
    #dar flag nele (retirando ao valor do total de bombas) e retirar 1 a cada square adjacente (possivelmente necessario criar uma class para os squares com os seus valores que vao sendo atualizados e com o valor a reirar proveninete de bombas adjacentes)
    #repete se o processo varias vezes, se n encontrar um 1 num canto entao voltar a chamar a funcao solver (recusao) de forma a obter um novo first

    #while face!=facedead && bombas>=0:



        #solver()

#abrir o browser
driver=webdriver.Firefox()

#abrir o site
driver.get('https://minesweeperonline.com')

solver(1)


#return element.get_attribute("class")
