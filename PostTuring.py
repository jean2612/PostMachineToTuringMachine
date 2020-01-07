import csv
import math

TranscricaoMP = []

# Leitura do arquivo.csv com separacao por virgulas
with open('teste1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    
    # Verificar o numero de linhas do arquivo lido
    linhas = 0
    for line in reader:
        TranscricaoMP.append(line)
        linhas = linhas + 1
    
    # Mostra o arquivo lido
    for i in TranscricaoMP:
        print(i)
    

    simbolosAlfabeto = []
    estados = []
    estadosTotal = []
    
    for linha in TranscricaoMP:
        if (linha[2] not in simbolosAlfabeto):
            simbolosAlfabeto.append(linha[2])

        if (linha[0] not in estados):
            estados.append(linha[0])

    quantidadeSimbolosMP = len(simbolosAlfabeto)
    #simbolosAlfabeto = simbolos
   # print("Quantidade de simbolos =", quantidadeSimbolosMP)

    quantidadeEstadosMP = len(estados)
    #print("Quantidade de estados =", quantidadeEstadosMP)

    estadosTotalMP = len(TranscricaoMP)
   # print("Quantidade de estados totais =", estadosTotalMP)


# Recebe algum simbolo um simbolo em MP e transcreve para MT
def traduzSimbolo(simbolo):
    
    quantidadeSimbolosMP = len(simbolosAlfabeto)
    #print("Quantidade de simbolos =", quantidadeSimbolosMP)

    # Calculo para ver quantos simbolos serão gerados na MT
    quantidadeSimbolosMT = round(math.log(quantidadeSimbolosMP, 2)+0.5)

    #print("Número de símbolos da máquina de turing = ", quantidadeSimbolosMT)

    marcaInicio = "a"

    simboloMT = marcaInicio + bin(simbolo)[2:].zfill(quantidadeSimbolosMT)  


    return simboloMT

def traduzEstado(estado):

    quantidadeEstadosMP = len(estados)+1
    #+1 para os dois novos estados quando há escrita
    #print("Quantidade de estados de MP =", quantidadeEstadosMP)

    quantidadeEstadosMT = round(math.log(int(quantidadeEstadosMP), 2)+0.5)

    #print("Número de estados de MT =", quantidadeEstadosMT)

    marcaInicioEstado = "q"
        
    #Estou criando um estado de escrita no final da fita da máquina de turing
    estadoMT = marcaInicioEstado + bin(estado)[2:].zfill(quantidadeEstadosMT)
    
    return estadoMT


teste1 = []
teste2 = []
teste1 = traduzSimbolo(int (9)) 
teste2 = traduzEstado (int (16))
#print("traducao simbolo =", teste1)
#print("traducao estado =", teste2)

contador = [0,0,0,0,0]
maquinaTuring = []
alfabeto = []

for i in range(0, quantidadeSimbolosMP):
    alfabeto.append(simbolosAlfabeto[i])
print(alfabeto)

for elemento in TranscricaoMP:
    #LEITURA
    if('R' in elemento[1]):
        #Faz tradução do estado atual, proximo estado, simbolo lido, simbolo escrito
        estadoAtual = traduzEstado(int(elemento[0]))
        #print(estadoAtual)
        proximoEstado = traduzEstado(int(elemento[3]))
        #print(proximoEstado)

        for simbolo in alfabeto:
            if(simbolo == elemento[2]):
                simboloLido = traduzSimbolo(contador[0])
                #print(simboloLido)
            else:
                contador[0] = contador[0] + 1

        for simbolo in alfabeto:
            if(simbolo == '8'):
                simboloEscrito = traduzSimbolo(contador[1])
                #print(simboloEscrito)
            else:
                contador[1] = contador[1] + 1
        contador[0] = 0
        contador[1] = 0
        ##
        maquinaTuring.append(estadoAtual + ', ' + simboloLido + ', ' +  proximoEstado + ', ' +  simboloEscrito + ', ' +  'd')

        
    #ESCRITA
    elif ('W' in elemento[1]):
        #Faz tradução do estado atual, proximo estado, simbolo lido, simbolo escrito
        estadoAtual = traduzEstado(int(elemento[0]))
        #print(estado_atual)
        proximoEstado = traduzEstado(int(elemento[3]))
        #print(proximo_estado)
        for simbolo in alfabeto:
            if(simbolo == elemento[2]):
                simboloEscrito = traduzSimbolo(contador[2])
                #print(simboloEscrito)
            else:
                contador[2] = contador[2] + 1
        contador[2] = 0
        estadoFim = traduzEstado(len(estados))
        estadoInicio = traduzEstado(len(estados)+1)
        #estados auxiliares que rodam até o fim e ao inicio respectivamente
        for simbolo in alfabeto:
            for s in alfabeto:
                if(s == simbolo):
                    simboloLido = traduzSimbolo(contador[3])
                else:
                    contador[3] = contador[3] + 1
    
            contador[3] = 0
            if(simbolo != '8'):
                maquinaTuring.append(estadoAtual + ', ' + simboloLido + ', ' +  estadoFim + ', ' + simboloLido + ', ' +  'd')
        for simbolo in alfabeto:
            for s in alfabeto:
                if(s == simbolo):
                    simboloLido = traduzSimbolo(contador[3])
                else:
                    contador[3] = contador[3] + 1
    
            contador[3] = 0
            if(simbolo == '8'):
                cont = 0
                for s in alfabeto:
                    if(s == elemento[2]):
                        simb = traduzSimbolo(cont)
                    else:
                        cont = cont + 1
                maquinaTuring.append(estadoFim + ', ' + simboloLido + ', ' +  estadoInicio + ', ' + simb + ', ' +  'e')
            else:
                # para rebobinar a esquerda
                maquinaTuring.append(estadoFim + ', ' + simboloLido + ', ' +  estadoFim + ', ' + simboloLido + ', ' +  'd') 
        for simbolo in alfabeto:
            for s in alfabeto:
                if(s == simbolo):
                    simboloLido = traduzSimbolo(contador[3])
                else:
                    contador[3] = contador[3] + 1
    
            contador[3] = 0
    
            if(simbolo == '8'):
                maquinaTuring.append(estadoInicio + ', ' + simboloLido + ', ' +  proximoEstado + ', ' + simboloLido + ', ' +  'd')
            else:
                maquinaTuring.append(estadoInicio + ', ' + simboloLido + ', ' +  estadoInicio + ', ' + simboloLido + ', ' +  'e')      
            
        
    
    # DESVIO
    else:
        #Faz tradução do estado atual, proximo estado, simbolo lido, simbolo escrito
        estadoAtual = traduzEstado(int(elemento[0]))
        #print(estadoAtual)
        proximoEstado = traduzEstado(int(elemento[3]))
        #print(proximoeEstado)
        
        for simbolo in alfabeto:
            for s in alfabeto:
                if(s == simbolo):
                    #print(traduzSimbolo(contador[4]))
                    simboloLido = traduzSimbolo(contador[4])
                else:
                    contador[4] = contador[4] + 1

            contador[4] = 0
            maquinaTuring.append(estadoAtual + ', ' + simboloLido + ', ' +  proximoEstado + ', ' +  simboloLido + ', ' +  'f')
              

# Gravação da maquina de turing traduzida para um aquivo txt

arquivo = open('MaquinaTuring.txt', 'w')

for i in maquinaTuring:
    arquivo.write(i+'\n')
    print(i)
arquivo.close()