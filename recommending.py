# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 14:23:57 2018

@author: Eduar
"""

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def main():
    #import numpy as np
    import pandas as pd
    
    #Lê o arquivo csv usando a biblioteca Pandas
    
    #fields=["Users/Items",	"Item1",	"Item2",	"Item3",	"Item4",	"Item5",	"Item6",	"Item7",	"Item8",	"Item9",	"Item10"];
    data = pd.read_csv("C:/Users/Eduar/Documents/github/recommending system/Dataset-grad.csv", header=0, sep=";");
    
    #Recolhe input do usuario
    usuarioX = input("Digite 'Usuário X': ")
    itemY = input("Digite 'Item Y': ")
    print("\n")
    
    linhaUsuario = []
    colunaItem = []
    
    #Seleciona a linha e coluna desejada em vetores para manipulacao
    linhaUsuario = data.iloc[int(usuarioX)]
    colunaItem = data.iloc[:,int(itemY)]
    
    #O número de itens avaliados pelo Usuário X
    
    #-----------------------------DEBUG----------------------------------
    #print("Itens avaliados pelo usuario("+usuarioX+"): \n")
    #print(linhaUsuario)
    #-----------------------------DEBUG----------------------------------
    
    totalItens = 0;
    for i in linhaUsuario:
        if(i!="?" and RepresentsInt(i)):
            totalItens += 1;
    print("--> Total itens avaliados por Usuario("+usuarioX+"): "+str(totalItens))
    
    
    #O número de usuários que avaliaram o Item Y
    print("\n")
    #-----------------------------DEBUG----------------------------------
    #print("Usarios que avaliaram o item("+itemY+"): \n")
    #print(colunaItem)
    #-----------------------------DEBUG----------------------------------
    
    totalUsuarios = 0;
    for j in colunaItem:
        if(j!="?" and RepresentsInt(j)):
            totalUsuarios += 1;
    print("--> Total usuarios que avaliaram o Item("+itemY+"): "+str(totalUsuarios))
    print("\n")
    
    
    #Se o Usuário X avaliou o Item Y
    if(linhaUsuario[int(itemY)]=="?"):
        print("--> O usuário NÃO avaliou o item("+itemY+")");
    else:
        print("--> O usuário avaliou o item("+itemY+")");
