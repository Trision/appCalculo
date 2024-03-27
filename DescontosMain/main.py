import streamlit as st
import math
import mysql

#declarando página
st.image('DescontosMain/logo.png', '',100)
st.title('Cálcular desconto')
carteira = st.radio('Carteira', ['Lendico', 'Consig', 'Help'], horizontal = True)
valor = st.number_input('Digite o valor em aberto: ')
parcelas = st.number_input('Digite a quantidade de parcelas', 1, 36)



#----------------------------------------------Inicio da lógica----------------------------------------------

#Listas de desconto
lendico = [[65, 60, 55, 52.5, 50, 45, 40, 35],
           [70, 65, 60, 57.5, 55, 50, 45, 40],
           [75, 70, 65, 62.5, 60, 55, 50, 45]
        ]

consig = [[40, 30, 20, 15, 10, 0, 0, 0],
           [45, 45, 35, 32.2, 30, 25, 20, 15],
           [57, 53, 51, 49, 45, 41, 37, 29],
           [70, 65, 60, 57.5, 55, 50, 45, 40]
        ]

help = [[50, 40, 30, 0, 0, 0, 0, 0],
           [50, 46.7, 43.6, 41.8, 40, 36.4, 32.8, 0],
           [67, 63, 59, 57, 55, 51, 47, 43],
           [80, 72, 72, 70, 68, 64, 0, 0]
        ]
#fim das listas

#defs para calcular o desconto                  -----inicio------

#1ª def, calculcar desconto Lendico
def calLen():
    if parcelas == 1:
        if valor < 4000:
            acordo = (lendico[0][0]/100) * valor
            valoracordo = valor - acordo
            st.text(f'R$ {valoracordo:.2f}')
        elif 4000 <= valor < 10000:
            acordo = (lendico[1][0]/100) * valor
            valoracordo = valor - acordo
            st.text(f'R$ {valoracordo:.2f}')
        elif valor >= 10000:
            acordo = (lendico[2][0]/100) * valor
            valoracordo = valor - acordo
            st.text(f'R$ {valoracordo:.2f}')
    elif  1 < parcelas <= 6:
            if valor < 4000:
                acordo = (lendico[0][1]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            elif 4000 <= valor < 10000:
                acordo = (lendico[1][1]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            elif valor >= 10000:
                acordo = (lendico[2][1]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
    elif  6 < parcelas <= 12:
            if valor < 4000:
                acordo = (lendico[0][2]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            elif 4000 <= valor < 10000:
                acordo = (lendico[1][2]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            elif valor >= 10000:
                acordo = (lendico[2][2]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
    elif  12 < parcelas <= 15:
            if valor < 4000:
                acordo = (lendico[0][3]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            elif 4000 <= valor < 10000:
                acordo = (lendico[1][3]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            elif valor >= 10000:
                acordo = (lendico[2][3]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
    elif  15 < parcelas <= 18:
            if valor < 4000:
                acordo = (lendico[0][4]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            elif 4000 <= valor < 10000:
                acordo = (lendico[1][4]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            elif valor >= 10000:
                acordo = (lendico[2][4]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
    elif  18 < parcelas <= 24:
            if valor < 4000:
                acordo = (lendico[0][5]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            elif 4000 <= valor < 10000:
                acordo = (lendico[1][5]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            elif valor >= 10000:
                acordo = (lendico[2][5]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
    elif  24 < parcelas <= 30:
            if valor < 4000:
                acordo = (lendico[0][6]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            elif 4000 <= valor < 10000:
                acordo = (lendico[1][6]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            elif valor >= 10000:
                acordo = (lendico[2][6]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
    elif  30 < parcelas <= 36:
            if valor < 4000:
                acordo = (lendico[0][7]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            elif 4000 <= valor < 10000:
                acordo = (lendico[1][7]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            elif valor >= 10000:
                acordo = (lendico[2][7]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
    else:
            if valor < 4000:
                acordo = (lendico[0][7]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            elif 4000 <= valor < 10000:
                acordo = (lendico[1][7]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            elif valor >= 10000:
                acordo = (lendico[2][7]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')            

#2ª def, calcular HY e consig
def calot():
    if parcelas == 1:
        if valor <= 1000:
            if carteira == 'Help':
                acordo = (help[0][0]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[0][0]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
        elif 1000 < valor <= 3000:
            if carteira == 'Help':
                acordo = (help[1][0]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[1][0]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
        elif 3000 < valor <= 5000:
            if carteira == 'Help':
                acordo = (help[2][0]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[2][0]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
        elif valor > 5000:
            if carteira == 'Help':
                acordo = (help[3][0]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[3][0]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
    elif 1 < parcelas <= 6:
        if valor <= 1000:
            if carteira == 'Help':
                acordo = (help[0][1]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[0][1]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
        elif 1000 < valor <= 3000:
            if carteira == 'Help':
                acordo = (help[1][1]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[1][1]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
        elif 3000 < valor <= 5000:
            if carteira == 'Help':
                acordo = (help[2][1]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[2][1]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
        elif valor > 5000:
            if carteira == 'Help':
                acordo = (help[3][1]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[3][1]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
    elif 6 < parcelas <= 12:
        if valor <= 1000:
            if carteira == 'Help':
                acordo = (help[0][2]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[0][2]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
        elif 1000 < valor <= 3000:
            if carteira == 'Help':
                acordo = (help[1][2]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[1][2]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
        elif 3000 < valor <= 5000:
            if carteira == 'Help':
                acordo = (help[2][2]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[2][2]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
        elif valor > 5000:
            if carteira == 'Help':
                acordo = (help[3][2]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[3][2]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
    elif 12 < parcelas <= 15:
        if valor <= 1000:
            if carteira == 'Help':
                acordo = (help[0][3]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[0][3]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
        elif 1000 < valor <= 3000:
            if carteira == 'Help':
                acordo = (help[1][3]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[1][3]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
        elif 3000 < valor <= 5000:
            if carteira == 'Help':
                acordo = (help[2][3]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[2][3]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
        elif valor > 5000:
            if carteira == 'Help':
                acordo = (help[3][3]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[3][3]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
    elif 15 < parcelas <= 18:
        if valor <= 1000:
            if carteira == 'Help':
                acordo = (help[0][4]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[0][4]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
        elif 1000 < valor <= 3000:
            if carteira == 'Help':
                acordo = (help[1][4]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[1][4]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
        elif 3000 < valor <= 5000:
            if carteira == 'Help':
                acordo = (help[2][4]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[2][4]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
        elif valor > 5000:
            if carteira == 'Help':
                acordo = (help[3][4]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[3][4]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
    elif 18 < parcelas <= 24:
        if valor <= 1000:
            if carteira == 'Help':
                acordo = (help[0][5]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[0][5]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
        elif 1000 < valor <= 3000:
            if carteira == 'Help':
                acordo = (help[1][5]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[1][5]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
        elif 3000 < valor <= 5000:
            if carteira == 'Help':
                acordo = (help[2][5]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[2][5]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
        elif valor > 5000:
            if carteira == 'Help':
                acordo = (help[3][5]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[3][5]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
    elif 24 < parcelas <= 30:
        if valor <= 1000:
            if carteira == 'Help':
                acordo = (help[0][6]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[0][6]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
        elif 1000 < valor <= 3000:
            if carteira == 'Help':
                acordo = (help[1][6]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[1][6]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
        elif 3000 < valor <= 5000:
            if carteira == 'Help':
                acordo = (help[2][6]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[2][6]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
        elif valor > 5000:
            if carteira == 'Help':
                acordo = (help[3][6]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[3][6]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
    elif 30 < parcelas <= 36:
        if valor <= 1000:
            if carteira == 'Help':
                acordo = (help[0][7]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[0][7]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
        elif 1000 < valor <= 3000:
            if carteira == 'Help':
                acordo = (help[1][7]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[1][7]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
        elif 3000 < valor <= 5000:
            if carteira == 'Help':
                acordo = (help[2][7]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[2][7]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
        elif valor > 5000:
            if carteira == 'Help':
                acordo = (help[3][7]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')
            else:
                acordo = (consig[3][7]/100) * valor
                valoracordo = valor - acordo
                st.text(f'R$ {valoracordo:.2f}')                         

#defs para calcular o desconto                   ------fim------

#chamar as def. De fato dá pra melhorar e muito tudo, mas eu fiz com pressa, então é isso.
#Poderia ter colocar uma def só, e no final no código chamar essa def
if carteira == 'Lendico':
    calLen()
else:
    calot()
#------------------------------------------------Fim da lógica-------------------------------------------------
