from tkinter import *


menu_inicia =Tk()
menu_inicia.title("Trabalho de logica")
menu_inicia.geometry("500x250+200+200")
menu_inicia.resizable(True,False)
menu_inicia.iconbitmap("imagem/icon.ico")

chckBox = IntVar()


#-----function----#
def verificar_usuario():
    l1['text']= text_usuario.get()
    
def menu():
    print(chckBox.get())

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

####fim



#---------------------dimensão da janela----------------#
largura = 800
altura = 500
#-----------------resolução da janela-----------#
largura_screen = menu_inicia.winfo_screenwidth()
altura_screen = menu_inicia.winfo_screenheight()

#-------------------posição da janela-------------------#
posx = largura_screen/2-largura/2
posy = altura_screen/2 - altura/2

#---------------------definir a geometry-------------------#
menu_inicia.geometry("%dx%d+%d+%d" % (largura, altura, posx,posy))

#---------------------Widgets-------------------------------#
frame_login=Frame(menu_inicia)

label_usuario=Label(frame_login, text="Usuario:")
text_usuario=Entry(frame_login)
l1 = Label(frame_login)
label_qtd=Label(frame_login, text="Quantidade:")
text_qtd=Entry(frame_login)
l2 = Label(frame_login)
btn_acesso=Button(frame_login, text="executar", command=verificar_usuario)

#check box
check = Checkbutton(
    menu_inicia,
    variable=chckBox,
    text="bubble sorted",
    command= menu
)
check1 = Checkbutton(
    menu_inicia,
    variable=chckBox,
    text="short Bubble sorted",
    command= menu
)
check2 = Checkbutton(
    menu_inicia,
    variable=chckBox,
    text="inserted sorted",
    command= menu
)
check3 = Checkbutton(
    menu_inicia,
    variable=chckBox,
    text="select position",
    command= menu
)





#---layout--#
label_usuario.grid(row=1, column=1)
text_usuario.grid(row=0, column=1)
btn_acesso.grid(row=3,column=3)
label_qtd.grid(row=0, column=0)
text_qtd.grid(row=1, column=1)
l2.grid(row=1, column=5)
check.grid(row=5, column=5)
check1.grid(row=5, column=6)
check2.grid(row=5, column=7)
check3.grid(row=5, column=8)

l1.grid()
frame_login.grid()

#---------packs--------------#
menu_inicia.mainloop()