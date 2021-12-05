from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.common.action_chains import ActionChains
import re

#class square:
    #value=                              #0:aberto sem nada adjacente;-1:flag;1-8: bombas adjacentes
    #subtract=


def update(squares):
    for l in 16:
        for c in 30:
            id=str(l)+"_"+str(c)
            args=(By.ID, id)
            element=driver.find_element(*args)
            val_sq=element.get_attribute("class")
            squares.value=re.sub("\D", "", val_sq)



#variave iter indica se se trata da primiera iteracão (iter=1) ou nãp (iter=0)
def solver(iter):

    max_lin=16
    max_col=30

    #selecionar primeiro square id="x_y"
    x=random.randint(1,max_lin)
    y=random.randint(1,max_col)

    id=str(x)+"_"+str(y)
    print(id)
    args=(By.ID, id)

    if iter==1:
        first=driver.find_element(*args) #necessario garantir que o first ja n esta aberto (por causa da recursão)
        squares=[[-1]*max_col]*max_lin   #inicializa a lista na primeira iteracão (tenho que mudar para que inicialize logo com a class)
        print(str(squares))
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
