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
    for l in range(1,max_lin+1):   #nao esquecer que para a matriz tera que ser l-1 para começar em 0, o mesmo para o c <-------------------- (matriz no site começa em 1 inves de 0)
        for c in range(1,max_col+1):
            id=str(l)+"_"+str(c)
            args=(By.ID, id)
            element=driver.find_element(*args)
            val_sq=element.get_attribute("class")                    #obtem o argumento referente ao valor que o square apresenta
            if val_sq!="square blank":
                squares[l-1][c-1].value=re.sub("\D", "", val_sq)     #retira apenas a parte numerica do argumento do square e mete na matriz (se demorar muito tempo podera ser possivel verificar se o valor novo e diferente do ja presente na matriz mas n sei se ajuda muito)
            if val_sq=="square bombflagged":
                squares[][].subtract+=1
                squares[][].subtract+=1
                squares[][].subtract+=1
                squares[][].subtract+=1
                squares[][].subtract+=1
                squares[][].subtract+=1
                squares[][].subtract+=1

#encontra na matriz os squares abertos que têm squares adjacentes por abrir que verifiquem self.value/(squares por if x!=l && y!=c && squares[x][y].value==-1 && squares[x][y].flag==False:
#not_open_adj+=1;abrir adjacentes) =1 indicando que estes contem bomba e tem de ser flagged (self.flag=TRUE e bombs-=1)
def maxProb(squares,l,c):  #(n sei se deve ser l ou l-1 e c ou c-1) porvavelmente necessita de uma flag para saber se encontrou algum com prob=1 porque senao abre se outro square random
    x=l-1;                 #tem que se ter global bombas-=1
    y=c-1;

    toti_bomba=squares[l][c].value-squares[l][c].subtract;

    not_open_adj=0;
    while x<=(l+1):
        while y<=(c+1):
            if x!=l && y!=c && squares[x][y].value==-1 && squares[x][y].flag==False:
                not_open_adj+=1;
            c+=1
        x+=1

    #condicao para toti_bomb>0?
    prob=not_open_adj/toti_bomba;

    

#obter o numero de bombas ainda por detetar, ou seja, sera o value do square - o numero de flagged squares adjacentes
def realvalue(squares):

    for l in range(max_lin):
        for c in range(max_col):
            if squares[l][c].value!=-1 && squares[l][c].value!=0:
                    while x<=(l+1):
                        while y<=(c+1):

#variave iter indica se se trata da primiera iteracão (iter=1) ou não (iter=0)
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

        #clicka no first
        actions=ActionChains(driver)
        actions.move_to_element(first).click()
        actions.perform()

        #update dos valores no squares abertos
        update(squares)

    else:
        if condition:
            #abrir o novo "first"
            #update dos valores no squares abertos
            #update(squares)
            #realvalue(squares) (acho que e preciso caso a nova abertura seja junto de flagged squares)
            pass
        pass

    for L in range(0,max_lin):
        for C in range(0,max_col):
            print(squares[L][C].value)

    #enontrar um 1 num canto
    #dar flag nele (retirando ao valor do total de bombas) e retirar 1 a cada square adjacente (possivelmente necessario criar uma class para os squares com os seus valores que vao sendo atualizados e com o valor a reirar proveninete de bombas adjacentes)
    #repete se o processo varias vezes, se n encontrar um 1 num canto entao voltar a chamar a funcao solver (recusao) de forma a obter um novo first

    #while face!=facedead && bombas>=0:

        #maxProb
        #if newbombs(saida de maxProb que indica novas bombas foram encontradas)!=0 (indica que n se encontrou)
            #solver(0)
        #else
            #abrir os com realvalue=0 && value!=0 para n tar a abrir squares no meio do nada
            #update(squares)
            #face=



#abrir o browser
driver=webdriver.Firefox()

#abrir o site
driver.get('https://minesweeperonline.com')

solver(1)


#return element.get_attribute("class")

#..............................................................

# 1 passo- abrir o primeiro squares
# 2 passo- update dos valores da grid
# 3 passo- encontrar os squares com o maxProb=1
# 4 passo- baseado no passo anterior dar flag aos devidos squares
# 5 passo- fazer o realvalue dos squares
# 6 passo- abrir os squares que ficam com 0 de realvalue
