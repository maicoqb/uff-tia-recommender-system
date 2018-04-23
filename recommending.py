# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 14:23:57 2018

@author: Eduar
"""
from scipy.stats.mstats import pearsonr
import numpy as np
import pandas as pd
import math 

def correlacaoPearson(vetA,vetB):
    usuarioA = vetA
    usuarioB = vetB
    #-----------------------------DEBUG----------------------------------
    #print("Pearson init")
    #print(str(len(usuarioA)))
    #print(usuarioA)
    #print(str(len(usuarioB)))
    #print(usuarioB)
    #-----------------------------DEBUG----------------------------------
    
    indexRemove = []
    for i in range(len(usuarioA)):
        if(usuarioA[i]=="?"):
            indexRemove.append(i)
             
    for j in range(len(usuarioB)):
        if(usuarioB[j]=="?"):
             indexRemove.append(j)
        

    indexRemove.sort(reverse=True)
    
    #Para fazer a correlaçao de Pearson é necessario comparar os itens avaliados pelos dois usuarios
    #ou seja, remover do vetor de comparacao os "?"    

    for k in indexRemove:
        usuarioA=np.delete(usuarioA, k)
        usuarioB=np.delete(usuarioB, k)
   
    #-----------------------------DEBUG----------------------------------
    #print("Pearson after")
    #print(usuarioA)
    #print(usuarioB)
    #-----------------------------DEBUG----------------------------------
    
    usuarioA = usuarioA.astype(int)
    usuarioB = usuarioB.astype(int)
   
    #chama a biblioteca PearsonR passando 2 vetores
    return pearsonr(usuarioA,usuarioB)[0];


def similaridadeItem(itemA,itemB):
    soma=0 
    for idx,i in enumerate(itemA):
         soma += itemA[idx]*itemB[idx]
    
    moduloA = aux(itemA)
    
    print("ModuloA")
    print(moduloA)
    moduloB = aux(itemB)
    print("ModuloB")
    print(moduloB)
    
    resp = soma / (moduloA * moduloB)
    
    return resp
    

def aux(vet):
    soma =0
    for idx,i in enumerate(vet):
        soma+= math.pow(vet[idx],2)    
    return math.sqrt(soma)
        

def media(vetor):
    for idx,i in enumerate(vetor):
        if(i=="?"):                    
            vetor=np.delete(vetor, idx)
    return np.mean(vetor.astype(int))


#FUNCAO TEST PARA AVALIAR O RESULTADO DE CADA PREDICAO
def test():
    for i in range(1,30):
        print(i)
        resp = main(i,8)
        if(resp==-1):
            print("============================================>ERROR")
            break
    
#CHAMAR ESSA FUNCAO PARA ENTRADA COM VALORES DO USUARIO    
def user():
    #Recolhe input do usuario
    usuarioX = input("Digite 'Usuário X': ")
    itemY = input("Digite 'Item Y': ")
    main(usuarioX,itemY)

def main(x,y):
    
    #Lê o arquivo csv usando a biblioteca Pandas    
    data = pd.read_csv("Dataset-grad.csv", header=0, sep=";").drop("Users/Items",axis=1);
    
    
    print("\n")
    
    usuarioX=x
    itemY=y
    
    usuarioX=str(int(usuarioX)-1)
    itemY=str(int(itemY)-1)
    
    
    linhaUsuario = []
    colunaItem = []
    
    #Seleciona a linha e coluna desejada em vetores para manipulacao
    linhaUsuario = data.iloc[int(usuarioX)]
    colunaItem = data.iloc[:,int(itemY)]

    
    #-----------------------------DEBUG----------------------------------
    #print("Itens avaliados pelo usuario("+usuarioX+"): \n")
    #print(linhaUsuario.values)
    #print("\n "+linhaUsuario[0])
    #-----------------------------DEBUG----------------------------------
    
    #O número de itens avaliados pelo Usuário X
    totalItens = 0
    for i in linhaUsuario:
        if(i!="?"):
            totalItens += 1
    print("--> Total itens avaliados por Usuario("+str(int(usuarioX)+1)+"): "+str(totalItens))
    print("\n")
    
    
    
    #-----------------------------DEBUG----------------------------------
    #print("Usarios que avaliaram o item("+itemY+"): \n")
    #print(colunaItem)
    #-----------------------------DEBUG----------------------------------
    
    #O número de usuários que avaliaram o Item Y
    totalUsuarios = 0
    for j in colunaItem:
        if(j!="?"):
            totalUsuarios += 1
    print("--> Total usuarios que avaliaram o Item("+str(int(itemY)+1)+"): "+str(totalUsuarios))
    print("\n")
    
    
    #Se o Usuário X avaliou o Item Y
    if(linhaUsuario[int(itemY)]=="?"):
        print("--> O usuário NÃO avaliou o item("+str(int(itemY)+1)+")")
    else:
        print("--> O usuário avaliou o item("+str(int(itemY)+1)+")")

    
    #Para cada item nao avaliado dar uma predicao baseada nos Usuarios
    naoAvaliados = []    
    for idx,i in enumerate(linhaUsuario):
        if(i=="?"):
            naoAvaliados.append(idx)
            
  
    # Soma 1 aos indices no print pois indice 0 == item 1
    print("\n")
    print("--> Itens nao avaliados: "+str(np.array(naoAvaliados)+1))
    
    
    #Para cada item não avaliado pelo Usuario
    for j in naoAvaliados:
        
        #Predicao "User-Based"
        somatorioNumerador = 0
        somatorioDenominador = 0
        #Varrer todos os usuarios
        for i in data.index:
            #Ratings do usuario atual
            linhaUsuarioAtual =  data.iloc[i].values     
            
            #Apenas faço o calculo para outros usuarios AND se eles tiverem avaliado o item que queremos fazer a predição
            if(i!=int(usuarioX) and linhaUsuarioAtual[int(j)]!="?"):
                
                #Formula matematica da predicao (slide 38)
                pearsonTemp = correlacaoPearson(data.iloc[int(usuarioX)].values,data.iloc[i].values)
                if(pearsonTemp > float(0.4)):               
                    somatorioDenominador += pearsonTemp                
                    rbp = int(linhaUsuarioAtual[int(j)])                
                    mediaUsuarioAtual = media(linhaUsuarioAtual)                
                    subtractvalue = rbp - mediaUsuarioAtual                            
                    somatorioNumerador += pearsonTemp * subtractvalue        
            
        
        razao = somatorioNumerador / somatorioDenominador    
        
        #-----------------------------DEBUG----------------------------------
        #print(somatorioNumerador)
        #print(somatorioDenominador)
        #print(media(linhaUsuario.values))
        #-----------------------------DEBUG----------------------------------
        
        predict = media(linhaUsuario.values) + razao
        
        print("     -->Predicao do Item("+str(j+1)+") para o Usuario("+str(int(usuarioX)+1)+"): " +str(predict))
        if(predict>5 or predict<0):
            return -1        
        
    return 0
        
            
        
        
    

            
        
    
    