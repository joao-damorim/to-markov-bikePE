#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 15:43:53 2019

@author: joao
"""

import numpy as np

def criar_matriz_de_transicao(l1_l1, l1_l2, l1_l3, l2_l1, l2_l2, l2_l3, l3_l1, l3_l2, l3_l3):
    
    a11 = l1_l1
    a12 = l1_l2
    a13 = l1_l3
    a21 = l2_l1
    a22 = l2_l2
    a23 = l2_l3
    a31 = l3_l1
    a32 = l3_l2
    a33 = l3_l3
    
    matriz = np.matrix([
        [a11, a12, a13],
        [a21, a22, a23],
        [a31, a32, a33]
    ])
    
    return matriz
    
def calcular_total_de_bicicletas_por_lugar_porcentagem(total_de_bicicletas, qtd_bicicleta_local_1, qtd_bicicleta_local_2, qtd_bicicleta_local_3):

    a11 = (qtd_bicicleta_local_1 / float(total_de_bicicletas)) * 100
    a12 = (qtd_bicicleta_local_2 / float(total_de_bicicletas)) * 100
    a13 = (qtd_bicicleta_local_3 / float(total_de_bicicletas)) * 100

    matriz = np.matrix([
        [a11, a12, a13],
    ])

    return [matriz, total_de_bicicletas]
    
def criar_array_futuro(distribuicao_de_bicicleta_atual, matriz_de_transicao_passada):

    array_futuro = np.dot(distribuicao_de_bicicleta_atual[0], matriz_de_transicao_passada)

    local_1 = array_futuro.item(0)

    local_2 = array_futuro.item(1)

    local_3 = array_futuro.item(2)
    
    return [local_1, local_2, local_3, distribuicao_de_bicicleta_atual[0].item(0), distribuicao_de_bicicleta_atual[0].item(1), distribuicao_de_bicicleta_atual[0].item(2), distribuicao_de_bicicleta_atual[1]]

def mostrar_quantidade_por_local(distribuicao_final):
    qtd_l1 = round(distribuicao_final[6]*(distribuicao_final[0]/100),1)
    qtd_l2 = round(distribuicao_final[6]*(distribuicao_final[1]/100),1)
    qtd_l3 = round(distribuicao_final[6]*(distribuicao_final[2]/100),1)

    return [qtd_l1, qtd_l2, qtd_l3]

def arredondar_qtd(lista_qtd_bicicleta):
    lista_qtd = []
    for i in lista_qtd_bicicleta:
        i = str(i)
        i = list(map(int, i.split(".")))
#
#        i = str(i)
#        i = i.split(".")
        
        lista_qtd.append(i)
    lista_dec = []
    for index, item in enumerate(lista_qtd):
            lista_dec.append(item[1])
            
    print(lista_dec)
    pos_mais_um = lista_dec.index(min(lista_dec))
    print(pos_mais_um)
#    lista_qtd[pos_mais_um][0] += 1 
    lista_ar = []
    for qtd in lista_qtd_bicicleta:
        lista_ar.append(round(qtd))
    
    lista_ar[pos_mais_um] -= 1
    
    return lista_ar
    
def definir_equipe(equipe_1, equipe_2, equipe_3, lista_qtd_locais):
    lista_equipe = []
    lista_equipe.append(equipe_1)
    lista_equipe.append(equipe_2)
    lista_equipe.append(equipe_3)
    
    lista_oti = []
   
    for i in range(len(lista_qtd_locais)):
        lista_est_eq = []
        max_eq = max(lista_equipe)
        rem_eq = lista_equipe.index(max(lista_equipe))
        lista_equipe.pop(rem_eq)
        max_est = max(lista_qtd_locais)
        rem_est = lista_qtd_locais.index(max(lista_qtd_locais))
        lista_qtd_locais.pop(rem_est)
        lista_est_eq.append(max_eq)
        lista_est_eq.append(max_est)
        lista_oti.append(lista_est_eq)
        
    return lista_oti
        
        
def definir_pares(lista_pares):
        print(lista_pares)
        print("Boulevard Rio Branco:\n - Quantidade de Bicicletas: %s\n - Quantidade de Integrantes da Equipe Responsavel: %s" % (str(lista_pares[0][1]), str(lista_pares[0][0])))
        print("Porto Digital:\n - Quantidade de Bicicletas: %s\n - Quantidade de Integrantes da Equipe Responsavel: %s" % (str(lista_pares[1][1]), str(lista_pares[1][0])))
        print("Praça do Arsenal:\n - Quantidade de Bicicletas: %s\n - Quantidade de Integrantes da Equipe Responsavel: %s" % (str(lista_pares[2][1]), str(lista_pares[2][0])))


matriz_transicao = criar_matriz_de_transicao(0.08, 0.90, 0.02, 0.67, 0.23, 0.10, 0.33, 0.64, 0.03)
distribuicao_comeco_dia = calcular_total_de_bicicletas_por_lugar_porcentagem(28, 10, 12, 6)
distribuicao_final_dia = criar_array_futuro(distribuicao_comeco_dia, matriz_transicao)
qtd_bicicleta_local_final_dia = mostrar_quantidade_por_local(distribuicao_final_dia)
print(qtd_bicicleta_local_final_dia)

qtd_bicicleta_local_final_dia_ar = arredondar_qtd(qtd_bicicleta_local_final_dia)

res_eq_est = (definir_equipe(10,20,5,qtd_bicicleta_local_final_dia_ar))

definir_pares(res_eq_est)


