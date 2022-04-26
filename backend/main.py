print("-"*42)
print("|                                        |")
print("|                                        |")
print("|                Bem Vindo               |")
print("|                                        |")
print("-"*42)
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

#---------------> Menu <--------------------#
array_tamanho = int(input("Qual o tamanho que vai ter?:"))
array = []

for i in range(array_tamanho):
    array.append(int(input("insira os numeros")))
    print(array)
ans = True
while ans:
    choice = input("Escolha: 1. Bubble sorte \n 2. short Bubble sorted \n 3. Inserted sorted 4. select_position \n escolha: ")
    choice = int(choice)
    if choice == 1:
        bubble_sorted()
    elif choice == 2:
        shortBubble_sorted()
    elif choice == 3:
        inserted_sorted()
    elif choice == 4:
        select_position()
        break
    else:
        print("Doido doidão")
    

# if next =="s":
#     while n>0: 
#         n = int(input("Insere os numeros:"))
#         next =  input ("Deseja continuar [s/n]...?")
#         array.append(n)
#         print(array)
#         if next =="s":
#             n = int(input("Insere os numeros:"))
#             next =  input ("Deseja continuar [s/n]...?")
#             array.append(n)
#         elif next =="n":
#             while True:
#                 choice = input("Escolha: 1. Bubble sorte \n 2. short Bubble sorted \n 3. Inserted sorted 4. select_position \n escolha: ")
#                 choice = int(choice)
#                 if choice == 1:
#                     bubble_sorted(array)
#                 elif choice == 2:
#                     shortBubble_sorted(array)
#                 elif choice == 3:
#                     inserted_sorted(array)
#                 elif choice == 4:
#                    select_position(array)

#                 else:
#                     print("fim")
#         else:
#             print("fim")
# else:
#     print("fim")
   