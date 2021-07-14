import graphviz as gv
from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import filedialog as FileDialog
from functools import partial
import tkinter as tk
from tkinter import ttk

import PIL
import PIL.Image
import PIL.ImageFont
import PIL.ImageOps
import PIL.ImageDraw
PIXEL_ON = 0  # PIL color to use for "on"
PIXEL_OFF = 255  # PIL color to use for "off"

def draw(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2): #Funcion para dibujar los automatas
    d = gv.Digraph(filename='rank_same')
    d.node('ini1', shape="point")
    d.node('ini2', shape="point")
    d.graph_attr['rankdir'] = 'LR'
    d.graph_attr['center'] = 'true'
    d.graph_attr['size'] = "4,5"
    d.graph_attr['ratio'] = "fill"
    
    with d.subgraph() as s:
    
     for e in estados1:
        if e in final1:
            s.node(e, shape="doublecircle")
        else:
            s.node(e)
        if e in inicio1:
            s.edge('ini1',e)

     for t in transiciones1:
        if t[2] not in alfabeto1:
            return 0
        s.edge(t[0], t[1], label=str(t[2]))

    with d.subgraph() as c:
    
     for e in estados2:
        if e in final2:
            c.node(e, shape="doublecircle")
        else:
            c.node(e)
        if e in inicio2:
            c.edge('ini2',e)

     for t in transiciones2:
        if t[2] not in alfabeto2:
            return 0
        c.edge(t[0], t[1], label=str(t[2]))
    d.render(filename='T_Automatas',format='png')
def draw_simplificado1(alfabeto1_simplificado,estados1_simplificado,transiciones1_simplificado,inicio1_simplificado,final1_simplificado):
    g = gv.Digraph(filename='Automata_Q0_Simplificado')
    g.node('ini', shape="point")
    g.graph_attr['rankdir'] = 'LR'
    g.graph_attr['center'] = 'true'
    g.graph_attr['size'] = "4,5"
    g.graph_attr['ratio'] = "fill"
    
    for e in estados1_simplificado:
        if e in final1_simplificado:
            g.node(e, shape="doublecircle")
        else:
            g.node(e)
        if e in inicio1_simplificado:
            g.edge('ini',e)

    for t in transiciones1_simplificado:
        if t[2] not in alfabeto1_simplificado:
            return 0
        g.edge(t[0], t[1], label=str(t[2]))
    g.render(filename='Automata_Q0_Simplificado',format='png')

def text_image(text_path, font_path=None):  #Funcion para convertir txt a png encontrado en Internet

    grayscale = 'L'
    # parse the file into lines
    with open(text_path) as text_file:  # can throw FileNotFoundError
        lines = tuple(l.rstrip() for l in text_file.readlines())

    # choose a font 
    large_font = 20  # get better resolution with larger size
    font_path = font_path or 'cour.ttf'  # Courier New. works in windows.
    try:
        font = PIL.ImageFont.truetype(font_path, size=large_font)
    except IOError:
        font = PIL.ImageFont.load_default()
        print('Could not use chosen font. Using default.')

    # make the background image based on the combination of font and lines
    pt2px = lambda pt: int(round(pt * 96.0 / 72))  # convert points to pixels
    max_width_line = max(lines, key=lambda s: font.getsize(s)[0])
    # max height is adjusted down because it's too large visually for spacing
    test_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    max_height = pt2px(font.getsize(test_string)[1])
    max_width = pt2px(font.getsize(max_width_line)[0])
    height = max_height * len(lines)  # perfect or a little oversized
    width = int(round(max_width + 40))  # a little oversized
    image = PIL.Image.new(grayscale, (width, height), color=PIXEL_OFF)
    draw = PIL.ImageDraw.Draw(image)

    # draw each line of text
    vertical_position = 5
    horizontal_position = 5
    line_spacing = int(round(max_height * 0.8))  # reduced spacing seems better
    for line in lines:
        draw.text((horizontal_position, vertical_position),
                  line, fill=PIXEL_ON, font=font)
        vertical_position += line_spacing
    # crop the text
    c_box = PIL.ImageOps.invert(image).getbbox()
    image = image.crop(c_box)
    return image

def automata_nuevo1():
    alfabeto = [0,1]
    estados = ["Q0"]
    transiciones = [("Q0","Q0", 0)]
    inicio = ["Q0"]
    final = ["Q0"]
    return alfabeto,estados,transiciones,inicio,final
def automata_nuevo2():
    alfabeto = [0,1]
    estados = ["q0"]
    transiciones = [("q0","q0", 0)]
    inicio = ["q0"]
    final = ["q0"]
    return alfabeto,estados,transiciones,inicio,final

def agregar_nodos1(alfabeto1,estados1,transiciones1,inicio1,final1): 
    numero=0
    bloqueo=1 
    while bloqueo==1:                                               #while que se repetira hasta que se ingrese un Nodo
      secuencia=0
      if len(estados1)!=0:                                  #If que detecta si hay nodos en el grafo
          for k in range(len(estados1)):                    #for que busca en k posiciones de la lista de nodos
           if secuencia!=1:
                actual=estados1[k].replace('Q','')
                if numero==int(actual):                     #Si el numero es igual que el de la lista, detecta que el numero Nodo ya existe y vuelve a ejecutar el while
                     numero=numero+1                             #Esto es para verificar que no se agreguen nodos iguales
                     secuencia=1
                elif k == (len(estados1))-1:                #En caso que la lista no posea el numero que se quiere ingresar, se añade ese mismo Nodo
                 estados1.append('Q'+str(numero))
                 bloqueo=0                                       #Cuando se ingrese el Nodo nuevo efectuara que bloqueo rompa el ciclo while
      else:
           estados1.append("Q0")
           transiciones1.append("Q0","Q0", 0)
           transiciones1.append("Q0","Q0", 1)
           inicio1.append("Q0")
           final1.append("Q0")                                        #En caso que la lista no tenga nodos, se agregara el nodo 0 por defecto
           bloqueo=0
    return alfabeto1,estados1,transiciones1,inicio1,final1       
def agregar_nodos2(alfabeto2,estados2,transiciones2,inicio2,final2): 
    numero=0
    bloqueo=1 
    while bloqueo==1:                                               #while que se repetira hasta que se ingrese un Nodo
      secuencia=0
      if len(estados2)!=0:                                  #If que detecta si hay nodos en el grafo
          for k in range(len(estados2)):                    #for que busca en k posiciones de la lista de nodos
           if secuencia!=1:
                actual=estados2[k].replace('q','')
                if numero==int(actual):                     #Si el numero es igual que el de la lista, detecta que el numero Nodo ya existe y vuelve a ejecutar el while
                     numero=numero+1                             #Esto es para verificar que no se agreguen nodos iguales
                     secuencia=1
                elif k == (len(estados2))-1:                #En caso que la lista no posea el numero que se quiere ingresar, se añade ese mismo Nodo
                 estados2.append('q'+str(numero))
                 bloqueo=0                                       #Cuando se ingrese el Nodo nuevo efectuara que bloqueo rompa el ciclo while
      else:
           estados2.append("q0")
           transiciones2.append("q0","q0", 0)
           transiciones2.append("q0","q0", 1)
           inicio2.append("q0")
           final2.append("q0")                                        #En caso que la lista no tenga nodos, se agregara el nodo 0 por defecto
           bloqueo=0
    return alfabeto2,estados2,transiciones2,inicio2,final2     

def eliminar_nodos1(alfabeto1,estados1,transiciones1,inicio1,final1,combobox1):
    if(len(combobox1))!=0:
     if combobox1 != 'Q0':
        aux1=len(transiciones1)
        for i in range(aux1):
         if combobox1 != transiciones1[(i-(aux1-1))*-1][0]:
            if combobox1 == transiciones1[(i-(aux1-1))*-1][1]:
                transiciones1.remove(transiciones1[(i-(aux1-1))*-1])
         else:
            if combobox1 == transiciones1[(i-(aux1-1))*-1][0]:
                transiciones1.remove(transiciones1[(i-(aux1-1))*-1])
        estados1.remove(combobox1)
    return alfabeto1,estados1,transiciones1,inicio1,final1
def eliminar_nodos2(alfabeto2,estados2,transiciones2,inicio2,final2,combobox1):
    if(len(combobox1))!=0:
     if combobox1 != 'Q0':
        aux1=len(transiciones2)
        for i in range(aux1):
         if combobox1 != transiciones2[(i-(aux1-1))*-1][0]:
            if combobox1 == transiciones2[(i-(aux1-1))*-1][1]:
                transiciones2.remove(transiciones2[(i-(aux1-1))*-1])
         else:
            if combobox1 == transiciones2[(i-(aux1-1))*-1][0]:
                transiciones2.remove(transiciones2[(i-(aux1-1))*-1])
        estados2.remove(combobox1)
    return alfabeto2,estados2,transiciones2,inicio2,final2

def agregar_enlace1(alfabeto1,estados1,transiciones1,inicio1,final1,combobox2,combobox3,comboboxz1):
    if len(combobox2) != 0:
        if len(combobox3) != 0:
            for i in range(len(alfabeto1)):
                if comboboxz1 == str(alfabeto1[i]):
                    for i in range(len(transiciones1)):
                        if transiciones1[i][0] == combobox2:
                            if transiciones1[i][2] == int(comboboxz1):
                                MessageBox.showinfo("Aviso: ",(combobox2,' Ya tiene arista',int(comboboxz1)))
                                return alfabeto1,estados1,transiciones1,inicio1,final1
            if len(comboboxz1)!=0:
                transiciones1.append((combobox2,combobox3, int(comboboxz1)))
    return alfabeto1,estados1,transiciones1,inicio1,final1
def agregar_enlace2(alfabeto2,estados2,transiciones2,inicio2,final2,combobox2,combobox3,comboboxz1):
    if len(combobox2) != 0:
        if len(combobox3) != 0:
            for i in range(len(alfabeto2)):
                if comboboxz1 == str(alfabeto2[i]):
                    for i in range(len(transiciones2)):
                        if transiciones2[i][0] == combobox2:
                            if transiciones2[i][2] == int(comboboxz1):
                                MessageBox.showinfo("Aviso: ",(combobox2,' Ya tiene arista',int(comboboxz1)))
                                return alfabeto2,estados2,transiciones2,inicio2,final2
            if len(comboboxz1)!=0:
                transiciones2.append((combobox2,combobox3, int(comboboxz1)))
    return alfabeto2,estados2,transiciones2,inicio2,final2

def eliminar_enlace1(alfabeto1,estados1,transiciones1,inicio1,final1,combobox4,combobox5,comboboxz2):
    if len(combobox4) != 0:
        if len(combobox5) != 0:
            for i in range(len(alfabeto1)):
                if comboboxz2 == str(alfabeto1[i]):
                    for i in range(len(transiciones1)):
                        if transiciones1[i][0]==combobox4:
                            if transiciones1[i][1]==combobox5:
                                if transiciones1[i][2]==int(comboboxz2):
                                    transiciones1.remove((transiciones1[i][0],transiciones1[i][1],transiciones1[i][2]))
                                    return alfabeto1,estados1,transiciones1,inicio1,final1,combobox4,combobox5
    MessageBox.showinfo("Aviso: ",(combobox4,' Y ',combobox5,'\n No tienen esa aristas en común'))
    return alfabeto1,estados1,transiciones1,inicio1,final1,combobox4,combobox5
def eliminar_enlace2(alfabeto2,estados2,transiciones2,inicio2,final2,combobox4,combobox5,comboboxz2):
    if len(combobox4) != 0:
        if len(combobox5) != 0:
            for i in range(len(alfabeto2)):
                if comboboxz2 == str(alfabeto2[i]):
                    for i in range(len(transiciones2)):
                        if transiciones2[i][0]==combobox4:
                            if transiciones2[i][1]==combobox5:
                                if transiciones2[i][2]==int(comboboxz2):
                                    transiciones2.remove((transiciones2[i][0],transiciones2[i][1],transiciones2[i][2]))
                                    return alfabeto2,estados2,transiciones2,inicio2,final2
    MessageBox.showinfo("Aviso: ",(combobox4,' Y ',combobox5,'\n No tienen esa aristas en común'))
    return alfabeto2,estados2,transiciones2,inicio2,final2

def editar_termino1(alfabeto1,estados1,transiciones1,inicio1,final1,combobox7,combobox8):
    if len(combobox7) != 0:
        if len(combobox8) != 0:
            if combobox8 == 'SI':
                for i in range(len(final1)):
                    if final1[i]==combobox7:
                        return alfabeto1,estados1,transiciones1,inicio1,final1
                final1.append(combobox7)
                return alfabeto1,estados1,transiciones1,inicio1,final1
            if combobox8 == 'NO':
                for i in range(len(final1)):
                    if final1[i]==combobox7:
                        final1.remove(combobox7)
                        return alfabeto1,estados1,transiciones1,inicio1,final1
    return alfabeto1,estados1,transiciones1,inicio1,final1
def editar_termino2(alfabeto2,estados2,transiciones2,inicio2,final2,combobox7,combobox8):
    if len(combobox7) != 0:
        if len(combobox8) != 0:
            if combobox8 == 'SI':
                for i in range(len(final2)):
                    if final2[i]==combobox7:
                        return alfabeto2,estados2,transiciones2,inicio2,final2
                final2.append(combobox7)
                return alfabeto2,estados2,transiciones2,inicio2,final2
            if combobox8 == 'NO':
                for i in range(len(final2)):
                    if final2[i]==combobox7:
                        final2.remove(combobox7)
                        return alfabeto2,estados2,transiciones2,inicio2,final2
    return alfabeto2,estados2,transiciones2,inicio2,final2


def sumar_alfabeto1(alfabeto1,estados1,transiciones1,inicio1,final1):
    alfabeto1.append(len(alfabeto1))
    return alfabeto1,estados1,transiciones1,inicio1,final1
def sumar_alfabeto2(alfabeto2,estados2,transiciones2,inicio2,final2):
    alfabeto2.append(len(alfabeto2))
    return alfabeto2,estados2,transiciones2,inicio2,final2

def restar_alfabeto1(alfabeto1,estados1,transiciones1,inicio1,final1):

    if len(alfabeto1) == 2:
        MessageBox.showinfo("Aviso: ",('No se puede quitar más'))
        return alfabeto1,estados1,transiciones1,inicio1,final1
    else:
        aux1=len(transiciones1)
        for i in range(aux1):
         if (len(alfabeto1)-1) == transiciones1[(i-(aux1-1))*-1][2]:
                transiciones1.remove(transiciones1[(i-(aux1-1))*-1])
        alfabeto1.remove(len(alfabeto1)-1)
        return alfabeto1,estados1,transiciones1,inicio1,final1
def restar_alfabeto2(alfabeto2,estados2,transiciones2,inicio2,final2):

    if len(alfabeto2) == 2:
        MessageBox.showinfo("Aviso: ",('No se puede quitar más'))
        return alfabeto2,estados2,transiciones2,inicio2,final2
    else:
        aux1=len(transiciones2)
        for i in range(aux1):
         if (len(alfabeto2)-1) == transiciones2[(i-(aux1-1))*-1][2]:
                transiciones2.remove(transiciones2[(i-(aux1-1))*-1])
        alfabeto2.remove(len(alfabeto2)-1)
        return alfabeto2,estados2,transiciones2,inicio2,final2

def matriz_automata1(alfabeto1,estados1,transiciones1,inicio1,final1):
    matriz=[]
    matriz_aux=[]
    matriz_aux.append('~')
    for i in range(len(estados1)):
        matriz_aux.append(estados1[i])
    matriz.append(matriz_aux)
    matriz_aux=[]
    for i in range(len(alfabeto1)):
        matriz_aux.append(alfabeto1[i])
        for j in range(len(estados1)):
            matriz_aux.append('~~')
            for k in range(len(transiciones1)):
                if estados1[j] == transiciones1[k][0]:
                    if alfabeto1[i] == transiciones1[k][2]:
                        matriz_aux.pop(j+1)
                        matriz_aux.append(transiciones1[k][1])
        matriz.append(matriz_aux)
        matriz_aux=[]               

    with open('Matriz_Q0.txt', 'w') as f:
        for line in matriz:
            for valor in line:
                f.write('  ')
                f.write(str(valor))
                f.write(' | ')
            f.write('\n')

    image = text_image('Matriz_Q0.txt')
    image.save('Matriz_Q0.png')
    image.close()

    return alfabeto1,estados1,transiciones1,inicio1,final1
def matriz_automata2(alfabeto2,estados2,transiciones2,inicio2,final2):
    matriz=[]
    matriz_aux=[]
    matriz_aux.append('~')
    for i in range(len(estados2)):
        matriz_aux.append(estados2[i])
    matriz.append(matriz_aux)
    matriz_aux=[]
    for i in range(len(alfabeto2)):
        matriz_aux.append(alfabeto2[i])
        for j in range(len(estados2)):
            matriz_aux.append('~~')
            for k in range(len(transiciones2)):
                if estados2[j] == transiciones2[k][0]:
                    if alfabeto2[i] == transiciones2[k][2]:
                        matriz_aux.pop(j+1)
                        matriz_aux.append(transiciones2[k][1])
        matriz.append(matriz_aux)
        matriz_aux=[]               

    with open('Matrizq0.txt', 'w') as f:
        for line in matriz:
            for valor in line:
                f.write('  ')
                f.write(str(valor))
                f.write(' | ')
            f.write('\n')

    image = text_image('Matrizq0.txt')
    image.save('Matrizq0.png')
    image.close()

    return alfabeto2,estados2,transiciones2,inicio2,final2

def matriz_distinguible1(alfabeto1,estados1,transiciones1,inicio1,final1):
    matriz_aux=[]
    matriz_aux2=[]
    matriz_distinguibles=[]
    estados_inversos=[]
    matriz_despliegue=[]
    for i in range(len(estados1)-1):
        estados_inversos.append(estados1[(i-(len(estados1)-1))*-1])
    for i in range(len(estados1)):
        for j in range(len(estados_inversos)):
            if estados1[i] in final1:
                if estados_inversos[j] in final1:
                    matriz_aux=[]
                else:
                    matriz_aux.append(estados1[i])
                    matriz_aux.append(estados_inversos[j])
                    matriz_distinguibles.append(matriz_aux)
                    matriz_aux=[]
            else:
                if estados_inversos[j] in final1:
                    matriz_aux.append(estados1[i])
                    matriz_aux.append(estados_inversos[j])
                    matriz_distinguibles.append(matriz_aux)
                    matriz_aux=[]
    matriz_aux=[]
    for bucles in range(len(estados1)+1):
     for i in range(len(estados1)):
        for j in range(len(estados_inversos)):
            for k in range(len(alfabeto1)):
                matriz_aux=[]
                for h in range(len(transiciones1)):
                    if estados1[i]==transiciones1[h][0]:
                        if alfabeto1[k]==transiciones1[h][2]:
                            auxiliar_estado=estados1[i]
                            matriz_aux.append(transiciones1[h][1])     
                for m in range(len(transiciones1)):
                    if estados_inversos[j]==transiciones1[m][0]:
                        if alfabeto1[k]==transiciones1[m][2]:
                            if len(matriz_aux) > 0:
                                matriz_aux.append(transiciones1[m][1])
                                for t in range(len(matriz_distinguibles)):
                                    if matriz_aux[0]==matriz_distinguibles[t][0]:
                                        if matriz_aux[1]==matriz_distinguibles[t][1]:
                                                matriz_aux2=[]
                                                matriz_aux2.append(auxiliar_estado)
                                                matriz_aux2.append(estados_inversos[j])
                                        else:
                                            matriz_aux2=[]
                                    else:
                                        matriz_aux2=[]
                                    if len(matriz_aux2) >0:
                                        if matriz_aux2 in matriz_distinguibles:
                                             matriz_aux2=[]
                                        else:
                                            matriz_distinguibles.append(matriz_aux2)
                                        matriz_aux2=[]
    matriz_aux=[]
    matriz_aux.append('~~')
    for i in range(len(estados_inversos)):
        matriz_aux.append(estados_inversos[i])
    matriz_despliegue=[]
    matriz_despliegue.append(matriz_aux)
    matriz_aux=[]
    matriz_aux2=[]
    matriz_aux3=[]
    m=(len(estados1)-2)
    for i in range(len(estados1)-1):
        matriz_aux.append(estados1[i])
        for j in range(len(estados_inversos)):
            if j <= m:
             matriz_aux2.append(estados1[i])
             matriz_aux2.append(estados_inversos[j])
             matriz_aux.append('OO')
             for k in range(len(matriz_distinguibles)):
                if estados1[i]==matriz_distinguibles[k][0]:
                    if estados_inversos[j]==matriz_distinguibles[k][1]:
                        matriz_aux2=[]
                        matriz_aux.pop(j+1)
                        matriz_aux.append('XX')
            matriz_aux3.append(matriz_aux2)
            matriz_aux2=[]
        m=m-1
        matriz_despliegue.append(matriz_aux)
        matriz_aux=[]
    cont=0
    for i in matriz_aux3:
     if i ==[]:
        cont=cont+1
    for i in range(cont):
        matriz_aux3.remove([])
    k=len(matriz_despliegue[0])
    with open('Automata_Q0_Simplificado_Matriz.txt', 'w') as f:
     for i in range(len(matriz_despliegue)):
        for j in range(len(matriz_despliegue[i])):
            if j <= k:
                f.write('  ')
                f.write(str(matriz_despliegue[i][j]))
                f.write(' | ')
        f.write('\n')
        k=k-1
    image = text_image('Automata_Q0_Simplificado_Matriz.txt')
    image.save('Automata_Q0_Simplificado_Matriz.png')
    image.close()
    alfabeto1_simplificado=[]
    estados1_simplificado=[]
    transiciones1_simplificado=[]
    inicio1_simplificado=[]
    final1_simplificado=[]
    for i in range(len(alfabeto1)):
        alfabeto1_simplificado.append(alfabeto1[i])
    for i in range(len(estados1)):
        estados1_simplificado.append(estados1[i])
    for i in range(len(transiciones1)):
        transiciones1_simplificado.append(transiciones1[i])
    for i in range(len(inicio1)):
        inicio1_simplificado.append(inicio1[i])
    for i in range(len(final1)):
        final1_simplificado.append(final1[i])
    matriz_estados_simplificados=[]
    lista_matriz_estados_simplificados=[]
    if len(matriz_aux3) >0:
        for i in range(len(matriz_aux3)):
            #print(matriz_estados_simplificados)
            aux_11=matriz_aux3[i][0]
            aux_12=matriz_aux3[i][1]
            nombre_nuevo=aux_11+aux_12
            if len(lista_matriz_estados_simplificados) != 0:
                for i in range(len(lista_matriz_estados_simplificados)):
                    if aux_11 in lista_matriz_estados_simplificados[i][0]:
                        aux_11=lista_matriz_estados_simplificados[i][1]
                    if aux_12 in lista_matriz_estados_simplificados[i][0]:
                        aux_12=lista_matriz_estados_simplificados[i][1]
            if aux_11 == aux_12:
                nombre_nuevo=aux_11
            else:
                nombre_nuevo=aux_11+aux_12
            matriz_estados_simplificados.append((aux_11,aux_12))
            matriz_estados_simplificados.append(nombre_nuevo)
            lista_matriz_estados_simplificados.append(matriz_estados_simplificados)
            matriz_estados_simplificados=[]
            if nombre_nuevo not in estados1_simplificado:
                estados1_simplificado.append(nombre_nuevo)
            for j in range(len(transiciones1_simplificado)):
                if transiciones1_simplificado[(j-(len(transiciones1_simplificado)-1))*-1][0]==aux_11:
                    aux2=transiciones1_simplificado[(j-(len(transiciones1_simplificado)-1))*-1][1]
                    aux3=transiciones1_simplificado[(j-(len(transiciones1_simplificado)-1))*-1][2]
                    if (aux_11,aux2,aux3) in transiciones1_simplificado:
                        transiciones1_simplificado.remove((aux_11,aux2,aux3))
                    if aux2 == aux_11:
                        aux2=nombre_nuevo
                    if (nombre_nuevo,aux2,aux3) not in transiciones1_simplificado:
                        transiciones1_simplificado.append((nombre_nuevo,aux2,aux3))
                if transiciones1_simplificado[(j-(len(transiciones1_simplificado)-1))*-1][1]==aux_11:
                    aux2=transiciones1_simplificado[(j-(len(transiciones1_simplificado)-1))*-1][0]
                    aux3=transiciones1_simplificado[(j-(len(transiciones1_simplificado)-1))*-1][2]
                    if (aux2,aux_11,aux3) in transiciones1_simplificado:
                        transiciones1_simplificado.remove((aux2,aux_11,aux3))
                    if (aux2,nombre_nuevo,aux3) not in transiciones1_simplificado:
                        transiciones1_simplificado.append((aux2,nombre_nuevo,aux3)) 
                if transiciones1_simplificado[(j-(len(transiciones1_simplificado)-1))*-1][0]==aux_12:
                    aux2=transiciones1_simplificado[(j-(len(transiciones1_simplificado)-1))*-1][1]
                    aux3=transiciones1_simplificado[(j-(len(transiciones1_simplificado)-1))*-1][2]
                    if (aux_12,aux2,aux3) in  transiciones1_simplificado:
                        transiciones1_simplificado.remove((aux_12,aux2,aux3))
                    if aux2 == aux_12:
                        aux2=nombre_nuevo
                    if (nombre_nuevo,aux2,aux3) not in transiciones1_simplificado:
                        transiciones1_simplificado.append((nombre_nuevo,aux2,aux3))
                if transiciones1_simplificado[(j-(len(transiciones1_simplificado)-1))*-1][1]==aux_12:
                    aux2=transiciones1_simplificado[(j-(len(transiciones1_simplificado)-1))*-1][0]
                    aux3=transiciones1_simplificado[(j-(len(transiciones1_simplificado)-1))*-1][2]
                    if (aux2,aux_12,aux3) in transiciones1_simplificado:
                        transiciones1_simplificado.remove((aux2,aux_12,aux3))
                    if (aux2,nombre_nuevo,aux3) not in transiciones1_simplificado:
                        transiciones1_simplificado.append((aux2,nombre_nuevo,aux3))
            if aux_11 in final1_simplificado:
                if nombre_nuevo in final1_simplificado:
                    aux_11=aux_11
                    final1_simplificado.remove(aux_11)
                else:
                    final1_simplificado.remove(aux_11)
                    final1_simplificado.append(nombre_nuevo)
            if aux_12 in final1_simplificado:
                if nombre_nuevo in final1_simplificado:
                    aux_12=aux_12
                    final1_simplificado.remove(aux_12)
                else:
                    final1_simplificado.remove(aux_12)
                    final1_simplificado.append(nombre_nuevo)
            for j in range(len(transiciones1_simplificado)):
                print('aca',matriz_aux3)
                print(aux_11,matriz_aux3[i][0])
                if aux_11 == matriz_aux3[i][0]:
                    if aux_11 in transiciones1_simplificado[(j-(len(transiciones1_simplificado)-1))*-1]:
                        transiciones1_simplificado.pop((j-(len(transiciones1_simplificado)-1))*-1)
                else:
                    if matriz_aux3[i][0] in transiciones1_simplificado[(j-(len(transiciones1_simplificado)-1))*-1]:
                        transiciones1_simplificado.pop((j-(len(transiciones1_simplificado)-1))*-1) 
            for j in range(len(transiciones1_simplificado)):
                print(aux_12,matriz_aux3[i][1])
                if aux_12 == matriz_aux3[i][1]:
                    if aux_12 in transiciones1_simplificado[(j-(len(transiciones1_simplificado)-1))*-1]:
                        transiciones1_simplificado.pop((j-(len(transiciones1_simplificado)-1))*-1)
                else:
                    if matriz_aux3[i][1] in transiciones1_simplificado[(j-(len(transiciones1_simplificado)-1))*-1]:
                        transiciones1_simplificado.pop((j-(len(transiciones1_simplificado)-1))*-1)
            if aux_11 in inicio1_simplificado:
                inicio1_simplificado.append(nombre_nuevo)
                inicio1_simplificado.remove(aux_11)
            if aux_11 != aux_12:
             if aux_11 in estados1_simplificado:
                estados1_simplificado.remove(aux_11)
            if aux_11 != aux_12:
             if aux_12 in estados1_simplificado:
                estados1_simplificado.remove(aux_12)
        print(alfabeto1)
        print(estados1)
        print(transiciones1)
        print(inicio1)
        print(final1)
        print(' ')
        print(alfabeto1_simplificado)
        print(estados1_simplificado)
        print(transiciones1_simplificado)
        print(inicio1_simplificado)
        print(final1_simplificado)
        draw_simplificado1(alfabeto1_simplificado,estados1_simplificado,transiciones1_simplificado,inicio1_simplificado,final1_simplificado)
    else:
        MessageBox.showinfo("Aviso: ",('No Se Puede Simplificar'))
        draw_simplificado1(alfabeto1,estados1,transiciones1,inicio1,final1)









#################################################################################################################

'''####################### Apartado para el Interfaz ################################'''

def crear_automata_nuevo():                        #despleguara un grafo en blanco//esta se tiene que modificar un poco
      alfabeto1,estados1,transiciones1,inicio1,final1=automata_nuevo1()
      alfabeto2,estados2,transiciones2,inicio2,final2=automata_nuevo2()
      Menu_principal(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)

def Menu_agregar_eliminar(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2):        #Lo mismo que arriba pero con otros botones
      
      draw(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)
      menu=Frame(root,width=750,height=680)
      menu.config(bg=cfondo)

      grafo=tk.PhotoImage(file="T_Automatas.png") 
      imagengrafo=Label(root, image=grafo).place(x=300,y=80)
      
      label1=Label(menu,text="Menu Agregar/Eliminar", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",16))
      label1.place(x=20, y=10)  

      label_grafico=Label(menu,text="Grafico Q0", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",16))
      label_grafico.place(x=400, y=50)  

      menu.pack()
      ##########################################################################
      boton1=Button(menu,text="Añadir Nodo",
                        foreground=cletraboton,bg=cboton, command=lambda:[agregar_nodos1(alfabeto1,estados1,transiciones1,inicio1,final1),menu.destroy(), Menu_agregar_eliminar(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],
                        font=("Arial",10),bd=3)
      boton1.place(x=109,y=80)
      ###########################################################################
      label2=Label(menu,text="Nodo Para Eliminar", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",8))
      label2.place(x=15, y=120)
      combobox1=ttk.Combobox(menu, state="readonly")
      combobox1.pack()
      combobox1.place(x=10,y=140)
      combobox1['values'] = [ (estados1[i]) for i in range(len(estados1))]

      boton2=Button(menu,text=" Eliminar Nodo ",
                        foreground=cletraboton,bg=cboton, command=lambda: [eliminar_nodos1(alfabeto1,estados1,transiciones1,inicio1,final1,combobox1.get()),menu.destroy(),Menu_agregar_eliminar(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],
                        font=("Arial",10),bd=3)
      boton2.place(x=160,y=135)
      ###############################################################################
      label3=Label(menu,text="Nodo Origen", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",8))
      label3.place(x=15, y=180)
      combobox2=ttk.Combobox(menu, state="readonly")
      combobox2.pack()
      combobox2.place(x=10,y=200)
      combobox2['values'] = [ (estados1[i]) for i in range(len(estados1))]
      label4=Label(menu,text="Nodo Destino", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",8))
      label4.place(x=15, y=223)

      combobox3=ttk.Combobox(menu, state="readonly")
      combobox3.pack()
      combobox3.place(x=10,y=240)
      combobox3['values'] = [ (estados1[i]) for i in range(len(estados1))]

      label15=Label(menu,text="Alfabeto", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",8))
      label15.place(x=15, y=263)

      comboboxz1 = ttk.Combobox(menu, state="readonly")
      comboboxz1.pack()
      comboboxz1.place(x=10, y=280)
      comboboxz1['values'] = [(alfabeto1[i]) for i in range(len(alfabeto1))]

      boton3=Button(menu,text=" Agregar Arista ",
                        foreground=cletraboton,bg=cboton, command=lambda: [agregar_enlace1(alfabeto1,estados1,transiciones1,inicio1,final1,combobox2.get(),combobox3.get(),comboboxz1.get()),menu.destroy(),Menu_agregar_eliminar(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],
                        font=("Arial",10),bd=3)
      boton3.place(x=160,y=235)
      ################################################################################
      label5=Label(menu,text="Nodo Origen", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",8))
      label5.place(x=15, y=323)
      combobox4=ttk.Combobox(menu, state="readonly")
      combobox4.pack()
      combobox4.place(x=10,y=340)
      combobox4['values'] = [ (estados1[i]) for i in range(len(estados1))]

      label6=Label(menu,text="Nodo Destino", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",8))
      label6.place(x=15, y=363)
      combobox5=ttk.Combobox(menu, state="readonly")
      combobox5.pack()
      combobox5.place(x=10,y=380)
      combobox5['values'] = [ (estados1[i]) for i in range(len(estados1))]

      label16=Label(menu,text="Alfabeto", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",8))
      label16.place(x=15, y=403)
      comboboxz2 = ttk.Combobox(menu, state="readonly")
      comboboxz2.pack()
      comboboxz2.place(x=10, y=420)
      comboboxz2['values'] = [(alfabeto1[i]) for i in range(len(alfabeto1))]

      boton4=Button(menu,text=" Eliminar Arista ",
                        foreground=cletraboton,bg=cboton, command=lambda: [eliminar_enlace1(alfabeto1,estados1,transiciones1,inicio1,final1,combobox4.get(),combobox5.get(),comboboxz2.get()),menu.destroy(),Menu_agregar_eliminar(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],
                        font=("Arial",10),bd=3)
      boton4.place(x=160,y=373)
      ################################################################################

      label9=Label(menu,text="Nodo", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",8))
      label9.place(x=12, y=463)
      combobox7=ttk.Combobox(menu, state="readonly")
      combobox7.pack()
      combobox7.place(x=10,y=480)
      combobox7['values'] = [ (estados1[i]) for i in range(len(estados1))]

      label10=Label(menu,text="Terminal", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",8))
      label10.place(x=12, y=503)
      combobox8=ttk.Combobox(menu, state="readonly")
      combobox8.pack()
      combobox8.place(x=10,y=520)
      combobox8['values'] = ['SI','NO']


      boton6=Button(menu,text="   Editar Nodo   ",
                        foreground=cletraboton,bg=cboton, command=lambda:[editar_termino1(alfabeto1,estados1,transiciones1,inicio1,final1,combobox7.get(),combobox8.get()),menu.destroy(),Menu_agregar_eliminar(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)] ,
                        font=("Arial",10),bd=3)
      boton6.place(x=160,y=495)
      ################################################################################
      boton_menos=Button(menu,text=" - ",
                        foreground=cletraboton,bg=cboton, command=lambda:[restar_alfabeto1(alfabeto1,estados1,transiciones1,inicio1,final1),menu.destroy(),Menu_agregar_eliminar(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],
                        font=("Arial",10),bd=3)
      boton_menos.place(x=40,y=560)
       
      label11=Label(menu,text=("Cantidad Alfabeto"), 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",10))
      label11.place(x=70, y=560)

      label12=Label(menu,text=len(alfabeto1), 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",10))
      label12.place(x=135, y=580)

      boton_mas=Button(menu,text=" + ",
                        foreground=cletraboton,bg=cboton, command=lambda:[sumar_alfabeto1(alfabeto1,estados1,transiciones1,inicio1,final1),menu.destroy(),Menu_agregar_eliminar(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],
                        font=("Arial",10),bd=3)
      boton_mas.place(x=210,y=560)
      ################################################################################
      boton_volver=Button(menu,text="volver",
                        foreground=cletraboton,bg=cboton, command=lambda:[menu.destroy(),Menu_principal(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],
                        font=("Arial",10),bd=3)
      boton_volver.place(x=130,y=630)
      #################################################################################
      boton_actualizar=Button(menu,text="Cambiar a q0",
                        foreground=cletraboton,bg=cboton, command=lambda:[menu.destroy(),Menu_agregar_eliminar2(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],
                        font=("Arial",10),bd=3)
      boton_actualizar.place(x=460,y=560)
      ################################################################################
      menu.pack()
      imagengrafo.pack()

def Menu_agregar_eliminar2(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2):        #Lo mismo que arriba pero con otros botones
      
      draw(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)
      menu=Frame(root,width=750,height=680)
      menu.config(bg=cfondo)

      grafo=tk.PhotoImage(file="T_Automatas.png") 
      imagengrafo=Label(root, image=grafo).place(x=300,y=80)
      
      label1=Label(menu,text="Menu Agregar/Eliminar", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",16))
      label1.place(x=20, y=10)  

      label_grafico=Label(menu,text="Grafico q0", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",16))
      label_grafico.place(x=400, y=50)  

      menu.pack()
      ##########################################################################
      boton1=Button(menu,text="Añadir Nodo",
                        foreground=cletraboton,bg=cboton, command=lambda:[agregar_nodos2(alfabeto2,estados2,transiciones2,inicio2,final2),menu.destroy(), Menu_agregar_eliminar2(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],
                        font=("Arial",10),bd=3)
      boton1.place(x=109,y=80)
      ###########################################################################
      label2=Label(menu,text="Nodo Para Eliminar", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",8))
      label2.place(x=15, y=120)
      combobox1=ttk.Combobox(menu, state="readonly")
      combobox1.pack()
      combobox1.place(x=10,y=140)
      combobox1['values'] = [ (estados2[i]) for i in range(len(estados2))]

      boton2=Button(menu,text=" Eliminar Nodo ",
                        foreground=cletraboton,bg=cboton, command=lambda: [eliminar_nodos2(alfabeto2,estados2,transiciones2,inicio2,final2,combobox1.get()),menu.destroy(),Menu_agregar_eliminar2(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],
                        font=("Arial",10),bd=3)
      boton2.place(x=160,y=135)
      ###############################################################################
      label3=Label(menu,text="Nodo Origen", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",8))
      label3.place(x=15, y=180)
      combobox2=ttk.Combobox(menu, state="readonly")
      combobox2.pack()
      combobox2.place(x=10,y=200)
      combobox2['values'] = [ (estados2[i]) for i in range(len(estados2))]
      label4=Label(menu,text="Nodo Destino", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",8))
      label4.place(x=15, y=223)

      combobox3=ttk.Combobox(menu, state="readonly")
      combobox3.pack()
      combobox3.place(x=10,y=240)
      combobox3['values'] = [ (estados2[i]) for i in range(len(estados2))]

      label15=Label(menu,text="Alfabeto", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",8))
      label15.place(x=15, y=263)

      comboboxz1 = ttk.Combobox(menu, state="readonly")
      comboboxz1.pack()
      comboboxz1.place(x=10, y=280)
      comboboxz1['values'] = [(alfabeto2[i]) for i in range(len(alfabeto2))]

      boton3=Button(menu,text=" Agregar Arista ",
                        foreground=cletraboton,bg=cboton, command=lambda: [agregar_enlace2(alfabeto2,estados2,transiciones2,inicio2,final2,combobox2.get(),combobox3.get(),comboboxz1.get()),menu.destroy(),Menu_agregar_eliminar2(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],
                        font=("Arial",10),bd=3)
      boton3.place(x=160,y=235)
      ################################################################################
      label5=Label(menu,text="Nodo Origen", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",8))
      label5.place(x=15, y=323)
      combobox4=ttk.Combobox(menu, state="readonly")
      combobox4.pack()
      combobox4.place(x=10,y=340)
      combobox4['values'] = [ (estados2[i]) for i in range(len(estados2))]

      label6=Label(menu,text="Nodo Destino", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",8))
      label6.place(x=15, y=363)
      combobox5=ttk.Combobox(menu, state="readonly")
      combobox5.pack()
      combobox5.place(x=10,y=380)
      combobox5['values'] = [ (estados2[i]) for i in range(len(estados2))]

      label16=Label(menu,text="Alfabeto", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",8))
      label16.place(x=15, y=403)
      comboboxz2 = ttk.Combobox(menu, state="readonly")
      comboboxz2.pack()
      comboboxz2.place(x=10, y=420)
      comboboxz2['values'] = [(alfabeto2[i]) for i in range(len(alfabeto2))]

      boton4=Button(menu,text=" Eliminar Arista ",
                        foreground=cletraboton,bg=cboton, command=lambda: [eliminar_enlace2(alfabeto2,estados2,transiciones2,inicio2,final2,combobox4.get(),combobox5.get(),comboboxz2.get()),menu.destroy(),Menu_agregar_eliminar2(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],
                        font=("Arial",10),bd=3)
      boton4.place(x=160,y=373)
      ################################################################################

      label9=Label(menu,text="Nodo", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",8))
      label9.place(x=12, y=463)
      combobox7=ttk.Combobox(menu, state="readonly")
      combobox7.pack()
      combobox7.place(x=10,y=480)
      combobox7['values'] = [ (estados2[i]) for i in range(len(estados2))]

      label10=Label(menu,text="Terminal", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",8))
      label10.place(x=12, y=503)
      combobox8=ttk.Combobox(menu, state="readonly")
      combobox8.pack()
      combobox8.place(x=10,y=520)
      combobox8['values'] = ['SI','NO']


      boton6=Button(menu,text="   Editar Nodo   ",
                        foreground=cletraboton,bg=cboton, command=lambda:[editar_termino2(alfabeto2,estados2,transiciones2,inicio2,final2,combobox7.get(),combobox8.get()),menu.destroy(),Menu_agregar_eliminar2(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)] ,
                        font=("Arial",10),bd=3)
      boton6.place(x=160,y=495)
      ################################################################################
      boton_menos=Button(menu,text=" - ",
                        foreground=cletraboton,bg=cboton, command=lambda:[restar_alfabeto2(alfabeto2,estados2,transiciones2,inicio2,final2),menu.destroy(),Menu_agregar_eliminar2(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],
                        font=("Arial",10),bd=3)
      boton_menos.place(x=40,y=560)
       
      label11=Label(menu,text=("Cantidad Alfabeto"), 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",10))
      label11.place(x=70, y=560)

      label12=Label(menu,text=len(alfabeto2), 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",10))
      label12.place(x=135, y=580)

      boton_mas=Button(menu,text=" + ",
                        foreground=cletraboton,bg=cboton, command=lambda:[sumar_alfabeto2(alfabeto2,estados2,transiciones2,inicio2,final2),menu.destroy(),Menu_agregar_eliminar2(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],
                        font=("Arial",10),bd=3)
      boton_mas.place(x=210,y=560)
      ################################################################################
      boton_volver=Button(menu,text="volver",
                        foreground=cletraboton,bg=cboton, command=lambda:[menu.destroy(),Menu_principal(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],
                        font=("Arial",10),bd=3)
      boton_volver.place(x=130,y=630)
      #################################################################################
      boton_actualizar=Button(menu,text="Cambiar a Q0",
                        foreground=cletraboton,bg=cboton, command=lambda:[menu.destroy(),Menu_agregar_eliminar(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],
                        font=("Arial",10),bd=3)
      boton_actualizar.place(x=460,y=560)
      ################################################################################
      menu.pack()
      imagengrafo.pack()

def Menu_principal(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2):               #caracts del Menu principal

      menu=Frame(root,width=300,height=300)
      menu.config(bg=cfondo)     
    
      label1=Label(menu,text="Menu", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",16))
      label1.place(x=115, y=10)  
      #menu.pack()

      ###################################################
      boton1=Button(menu,text="Agregar/Eliminar",
                        foreground=cletraboton,bg=cboton, command=lambda:[menu.destroy(),Menu_agregar_eliminar(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)], #Caratcs del boton
                        font=("Arial",10),bd=3)
      boton1.place(x=100,y=90)                                                                                                #Pos boton
      #######################################################################
      boton2=Button(menu,text="    Soluciones    ",
                        foreground=cletraboton,bg=cboton, command=lambda:[menu.destroy(),Menu_soluciones(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)], #Caracts combobox y a que funcion llama al sel clickeado
                        font=("Arial",10),bd=3)
      boton2.place(x=100,y=140)                                                                                                        #Pos combobox
      boton2=Button(menu,text=" Exportar Automata ",
                        foreground=cletraboton,bg=cboton, command=lambda:[exportar_grafo_excel(G,nombres,distancia)],
                        font=("Arial",10),bd=3)
      boton2.place(x=100,y=190)
      ######################################################################
      boton_volver=Button(menu,text="volver",
                        foreground=cletraboton,bg=cboton, command=lambda:[menu.destroy(),iniciador()],
                        font=("Arial",10),bd=3)
      boton_volver.place(x=125,y=240)

      menu.pack()                       #Se empaca la ventana par guardar

def Menu_soluciones(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2):
      
      draw(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)
      menu=Frame(root,width=750,height=600)
      menu.config(bg=cfondo)     

      grafo=tk.PhotoImage(file="T_Automatas.png") 
      imagengrafo=Label(root, image=grafo).place(x=300,y=80)
    
      label1=Label(menu,text="Menu Soluciones", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",16))
      label1.place(x=50, y=10)  

      menu.pack()
      ##########################################################################
      boton1=Button(menu,text="Matriz Transicion Q0",
                        foreground=cletraboton,bg=cboton, command=lambda:[matriz_automata1(alfabeto1,estados1,transiciones1,inicio1,final1),menu.destroy(),Menu_soluciones(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],  #Pongo error al boton que aun no se estabglece su fuioncion
                        font=("Arial",10),bd=3)
      boton1.place(x=80,y=90)
      ###########################################################################
      
      boton2=Button(menu,text="Matriz Transicion q0",
                        foreground=cletraboton,bg=cboton, command=lambda: [matriz_automata2(alfabeto2,estados2,transiciones2,inicio2,final2),menu.destroy(),Menu_soluciones(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],
                        font=("Arial",10),bd=3)
      boton2.place(x=80,y=150)
      ###############################################################################
      
      boton3=Button(menu,text="Simplificar Q0",
                        foreground=cletraboton,bg=cboton, command=lambda:[matriz_distinguible1(alfabeto1,estados1,transiciones1,inicio1,final1),menu.destroy(),Mostrar_simplificado1(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],
                        font=("Arial",10),bd=3)
      boton3.place(x=80,y=210)
      ################################################################################
      
      boton4=Button(menu,text="       Regiones Grafo     ",
                        foreground=cletraboton,bg=cboton, command=lambda: [menu.destroy(),Menu_soluciones(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],
                        font=("Arial",10),bd=3)
      boton4.place(x=80,y=270)
      ################################################################################
      
      boton5=Button(menu,text="    Numero Cromático   ",
                        foreground=cletraboton,bg=cboton, command=lambda: [menu.destroy(),Menu_soluciones(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],
                        font=("Arial",10),bd=3)
      boton5.place(x=80,y=330)
      ################################################################################
      
      label5=Label(menu,text="Nodo Origen", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",8))
      label5.place(x=25, y=370)
      combobox4=ttk.Combobox(menu, state="readonly")
      combobox4.pack()
      combobox4.place(x=20,y=385)
      combobox4['values'] = [0]

      label6=Label(menu,text="Nodo Destino", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",8))
      label6.place(x=25, y=407)
      combobox5=ttk.Combobox(menu, state="readonly")
      combobox5.pack()
      combobox5.place(x=20,y=425)
      combobox5['values'] = [0]
      boton6=Button(menu,text="   Dijkstra   ",
                        foreground=cletraboton,bg=cboton, command=lambda: [menu.destroy(),Menu_soluciones(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],
                        font=("Arial",10),bd=3)
      boton6.place(x=180,y=400)
      ################################################################################
      label5=Label(menu,text="Nodo Origen", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",8))
      label5.place(x=25, y=460)
      combobox6=ttk.Combobox(menu, state="readonly")
      combobox6.pack()
      combobox6.place(x=20,y=475)
      combobox6['values'] = [0]

      label6=Label(menu,text="Nodo Destino", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",8))
      label6.place(x=25, y=497)
      combobox7=ttk.Combobox(menu, state="readonly")
      combobox7.pack()
      combobox7.place(x=20,y=515)
      combobox7['values'] = [0]
      boton7=Button(menu,text="Flujo Máximo",
                        foreground=cletraboton,bg=cboton, command=lambda: [menu.destroy(),Menu_soluciones(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],
                        font=("Arial",10),bd=3)
      boton7.place(x=180,y=490)
      ################################################################################
      boton_volver=Button(menu,text="volver",
                        foreground=cletraboton,bg=cboton, command=lambda:[menu.destroy(),Menu_principal(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],
                        font=("Arial",10),bd=3)
      boton_volver.place(x=130,y=550)
      #################################################################################
      boton_actualizar=Button(menu,text="Actualizar",
                        foreground=cletraboton,bg=cboton, command=lambda:[menu.destroy(),Menu_soluciones(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],
                        font=("Arial",10),bd=3)
      boton_actualizar.place(x=460,y=455)
      #################################################################################
      boton_algoritmo_de_Prim=Button(menu,text=" Algoritmo De Prim ",
                        foreground=cletraboton,bg=cboton, command=lambda:[MessageBox.showinfo("algoritmo_Prim: ", 'Para ejecutar el algoritmo\nEl grafo se transformo'),menu.destroy(),Menu_soluciones(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],
                        font=("Arial",10),bd=3)
      boton_algoritmo_de_Prim.place(x=330,y=110)
      #################################################################################
      boton_algoritmo_de_kruskal=Button(menu,text="Algoritmo De Kruskal",
                        foreground=cletraboton,bg=cboton, command=lambda:[MessageBox.showinfo("algoritmo_kruskal: ", 'Para ejecutar el algoritmo\nEl grafo se transformo'),menu.destroy(),Menu_soluciones(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],
                        font=("Arial",10),bd=3)
      boton_algoritmo_de_kruskal.place(x=535,y=110)
      menu.pack()
      imagengrafo.pack()
  
def Mostrar_simplificado1(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2):
      
      menu=Frame(root,width=750,height=600)
      menu.config(bg=cfondo)     

      grafo=tk.PhotoImage(file="Automata_Q0_Simplificado.png") 
      imagengrafo=Label(root, image=grafo).place(x=300,y=80)
    
      matriz=tk.PhotoImage(file="Automata_Q0_Simplificado_Matriz.png") 
      imagenmatriz=Label(root, image=matriz).place(x=300,y=80)
      label1=Label(menu,text="Automata Q0 Simplificado", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",16))
      label1.place(x=50, y=10)  

      menu.pack()

      boton_volver=Button(menu,text="volver",
                        foreground=cletraboton,bg=cboton, command=lambda:[menu.destroy(),Menu_soluciones(alfabeto1,estados1,transiciones1,inicio1,final1,alfabeto2,estados2,transiciones2,inicio2,final2)],
                        font=("Arial",10),bd=3)
      boton_volver.place(x=130,y=550)
      menu.pack()
      imagengrafo.pack()


def iniciador():
          menu=Frame(root,width=300,height=300,background=cfondo)     #La primera ventana para escojer el Grafo inicial
          label1=Label(menu,text="Aplicación\nAutomatas", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",16))
          label1.place(x=90, y=10)
          boton1=Button(menu,text="   Nuevo Automata    ",
                        foreground=cletraboton,bg=cboton, command=lambda:[crear_automata_nuevo(),menu.destroy() ],
                        font=("Arial",10),bd=3)
          boton1.place(x=90,y=130)
          boton3=Button(menu,text="  Importar Automata  ",
                        foreground=cletraboton,bg=cboton, command=lambda:[empezar_grafo_fichero(),menu.destroy() ],
                        font=("Arial",10),bd=3)
          boton3.place(x=90,y=180)
          menu.pack()

cfondo="wheat3"               #Caracts de la interfaz, mas que nada los colores
ctitulos="gold4"
cboton="gold4"
cletraboton="snow"

root=Tk()                     #Llamado a que se despliuegue la interfaz

root.title("Aplicacion Grafos")    #Nombre de la interfaz
root.resizable(0,0)                #Establece que no se puede modificar la dimension de la interfaz

iniciador()              #Se llama
root.mainloop() 