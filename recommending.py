# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 14:23:57 2018

@author: Eduar
"""
from scipy.stats.mstats import pearsonr
import numpy as np
import pandas as pd
#import math 

def correlacaoPearson(usuarioA,usuarioB):
    #-----------------------------DEBUG----------------------------------
    #print(usuarioA)
    #print(usuarioB)
    #-----------------------------DEBUG----------------------------------

    #Para fazer a correlaçao de Pearson é necessario comparar os itens avaliados pelos dois usuarios
    #ou seja, remover do vetor de comparacao os "?"    
    for idx,i in enumerate(usuarioA):
            if(i=="?"):                    
                usuarioA=np.delete(usuarioA, idx);
                usuarioB=np.delete(usuarioB, idx);
    for idx,j in enumerate(usuarioB):
            if(j=="?"):
                usuarioA=np.delete(usuarioA, idx);
                usuarioB=np.delete(usuarioB, idx);
    
    usuarioA = usuarioA.astype(int)
    usuarioB = usuarioB.astype(int)
    
    #-----------------------------DEBUG----------------------------------
    #print(usuarioA)
    #print(usuarioB)
    #-----------------------------DEBUG----------------------------------
    
    #chama a biblioteca PearsonR passando 2 vetores
    return pearsonr(usuarioA,usuarioB)[0];


def media(vetor):
    for idx,i in enumerate(vetor):
        if(i=="?"):                    
            vetor=np.delete(vetor, idx);
    return np.mean(vetor.astype(int));


def main():
    
    #Lê o arquivo csv usando a biblioteca Pandas    
    data = pd.read_csv("Dataset-grad.csv", header=0, sep=";").drop("Users/Items",axis=1);
    
    #Recolhe input do usuario
    usuarioX = input("Digite 'Usuário X': ")
    itemY = input("Digite 'Item Y': ")
    print("\n")
    
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
    totalItens = 0;
    for i in linhaUsuario:
        if(i!="?"):
            totalItens += 1;
    print("--> Total itens avaliados por Usuario("+usuarioX+"): "+str(totalItens))
    print("\n")
    
    
    
    #-----------------------------DEBUG----------------------------------
    #print("Usarios que avaliaram o item("+itemY+"): \n")
    #print(colunaItem)
    #-----------------------------DEBUG----------------------------------
    
    #O número de usuários que avaliaram o Item Y
    totalUsuarios = 0;
    for j in colunaItem:
        if(j!="?"):
            totalUsuarios += 1;
    print("--> Total usuarios que avaliaram o Item("+itemY+"): "+str(totalUsuarios))
    print("\n")
    
    
    #Se o Usuário X avaliou o Item Y
    if(linhaUsuario[int(itemY)]=="?"):
        print("--> O usuário NÃO avaliou o item("+itemY+")");
    else:
        print("--> O usuário avaliou o item("+itemY+")");

    
    #DICA:   Usar pearsonr para realizar a correlacao Pearson de dois vetores
    #print("\n")    
    #print("Exemplo de correlação de Pearson entre 2 usuários quaisquer: ")
    #print(correlacaoPearson(data.iloc[8].values,data.iloc[2].values))
     
    #Para cada item nao avaliado dar uma predicao baseada nos Usuarios
    naoAvaliados = []    
    for idx,i in enumerate(linhaUsuario):
        if(i=="?"):
            naoAvaliados.append(idx);
  
    # Soma 1 aos indices para identificar os itens, indice 0 == item 1
    print("Itens nao avaliados: "+str(np.array(naoAvaliados)+1))
    
    for j in naoAvaliados:
        #Implementacao Predicao "User-Based"
        somatorioNumerador = 0
        somatorioDenominador = 0
        for i in data.index:
            linhaUsuarioAtual =  data.iloc[i].values
            
            if(i!=int(usuarioX) and linhaUsuarioAtual[int(j)]!="?"):
                pearsonTemp = correlacaoPearson(data.iloc[int(usuarioX)].values,data.iloc[i].values);
                
                somatorioDenominador += pearsonTemp
                
                rbp = int(linhaUsuarioAtual[int(j)]);
                
                mediaUsuarioAtual = media(linhaUsuarioAtual);
                
                subtractvalue = rbp - mediaUsuarioAtual
                
                somatorioNumerador += pearsonTemp * subtractvalue
                
        print(somatorioNumerador);
        print(somatorioDenominador);
        print("\n");
        
        print(linhaUsuario.values)
        print(media(linhaUsuario.values))
        razao = somatorioNumerador / somatorioDenominador
        print(razao)
        predict = media(linhaUsuario.values) + razao
        print("Predicao do Item("+str(j+1)+") para o Usuario("+usuarioX+"): " +str(predict));
        
        
            
        
        
    

            
        
    
    