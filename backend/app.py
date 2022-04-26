from tkinter import *


menu_inicia =Tk()
menu_inicia.title("Trabalho de logica")
menu_inicia.geometry("500x250+200+200")
menu_inicia.resizable(True,False)
menu_inicia.iconbitmap("imagem/icon.ico")

#---------------------dimensão da janela----------------#
largura = 800
altura = 400
#-----------------resolução da janela-----------#
largura_screen = menu_inicia.winfo_screenwidth()
altura_screen = menu_inicia.winfo_screenheight()

#-------------------posição da janela-------------------#
posx = largura_screen/2-largura/2
posy = altura_screen/2 - altura/2

#---------------------definir a geometry-------------------#
menu_inicia.geometry("%dx%d+%d+%d" % (largura, altura, posx,posy))


#---------------------label-------------------#
label = Label(menu_inicia, text="Digite o seu nome:").grid(row=0, sticky=W)

#-------------------text---------------------#
text = Entry(menu_inicia).grid(row=0, column=1)

#-----------------------button------------------#
btn = Button(menu_inicia, text="Entrar")
#---------------------Funcões-------------------#
def bubble_sorted(array):
    n = int(input("Insere os numeros:"))
    if n in array: 
        array.append(n)
        print("Adicionado")
        array.append(n)
        print(array)
        menu = str(input("Quer continuar?[s/n]"))
        if menu in 'Nn':
            print(array)

    for current in range(len(array)-1,0,-1):
        for i in range(current):
            if array[i]>array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp

def shortBubble_sorted(array):
    exchanges = True
    current = len(array)-1
    while current >0 and exchanges:
        exchanges = False
        for i in range(current):
            if array[i]> array[i+1]:
                exchanges = True
                temp = array[i]
                array[i] = array[i+1]
                array[i+1]= temp
                current = current -1

def inserted_sorted(array):
    for i in range(1, len(array)):
        current_value = array[i]
        current_position = i
        while current_position > 0 and array[current_position - 1] > current_value:
                array[current_position] = array[current_position - 1]
                current_position = current_position - 1
                array[current_position] = current_value

def select_position(array):
    current = len(array)
    for i in range(current):
        min = i #min = minimo
        for j in range(i +1, current):
            if array[min] > array[j]:
                min = j
        (array[i],array[min]) = (array[min], array[i])





#---------packs--------------#
label.pack()
btn.pack()
menu_inicia.mainloop()