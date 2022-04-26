from time import time
import time
tamanho = int(input("insere o tamanho"))
array = []

for v in range(tamanho):
    array.append(int(input("insere:")))
    print(array)


print("|","-"*50,"|")
print("|                                                    |")
print("|                                                    |")
print("|                 Seja bem vindo!                    |")
print("|                                                    |")
print("|                                                    |")
print("|","-"*50,"|")
menu_options = {
    1: "Bubble Sorted",
    2: "Short Bubble sorted",
    3: "Inserted Sorted",
    4: "Select Position",
    5:"str int",
    6: "Shell sort",
    7: "Quick sort",
    8: "Merge Sort",
    9: "Sair"
}   
def print_menu():
    for key in menu_options.keys():
        print(key,'--',menu_options[key])



def bubble_sorted(array):
    start = time.time()
    time.sleep(0.0000000000001)    
    for current in range(len(array)-1,0,-1):
        for i in range(current):
            if array[i]>array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
    timef= time.time()
    start_fin = timef-start

    print(array, "Esse é o tempo:",start_fin)

def shortBubble_sorted(array):
    start = time.time()
    time.sleep(0.0000000000001)   
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
    timef= time.time()
    start_fin = timef-start

    print(array, "Esse é o tempo:",start_fin)
        
def inserted_sorted(array):
    start = time.time()
    time.sleep(0.0000000000001) 
    for i in range(1, len(array)):
        current_value = array[i]
        current_position = i
        while current_position > 0 and array[current_position - 1] > current_value:
                array[current_position] = array[current_position - 1]
                current_position = current_position - 1
                array[current_position] = current_value
    timef= time.time()
    start_fin = timef-start

    print(array, "Esse é o tempo:",start_fin)

def select_position(array):
    start = time.time()
    time.sleep(0.0000000000001) 
    current = len(array)
    for i in range(current):
        min = i #min = minimo
        for j in range(i +1, current):
            if array[min] > array[j]:
                min = j
        (array[i],array[min]) = (array[min], array[i])
    timef= time.time()
    start_fin = timef-start

    print(array, "Esse é o tempo:",start_fin)

def str_int(array):
   a=array.split()
   list=[]
   for i in range(len(a)):
      b = a[i]
      array.append(int(b))
   print(array)

def shell_sort_help(array, n):
    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo, n):
            temp = array[i]
            j = i
            while j >= intervalo and array[j - intervalo] > temp:
                array[j] = array[j - intervalo]
                j -= intervalo

            array[j] = temp
        intervalo //= 2
def shell_sort(array):
    timei = time.time()
    time.sleep(0.0000000000001)
    n1=len(array)
    shell_sort_help(array,n1)
    timef = time.time()
    timeend = timef - timei

    print(array,"Tempo gastado:",timeend)


def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1

from time import time
import time
def quick_sort_help(array, low, high):

  if low < high:

    pi = partition(array, low, high)

    quick_sort_help(array, low, pi - 1)
    quick_sort_help(array, pi + 1, high)


def quick_sort(array):
  start = time.time()
  time.sleep(0.0000000000001)
  quick_sort_help(array, 0, len(array) - 1)
  start_fin = time.time()
  timeend = start_fin - start

  print(array,"Tempo gastado",timeend)

def mergeSort(array):
    start = time.time()
    time.sleep(0.0000000000001)
    if len(array) > 1:

        
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
    start_fin = time.time()
    timeend = start - start_fin
    print(array,"Tempo gasto:",timeend)



if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Errado . Por favor! entra a numero ...')
    
        if option == 1:
           bubble_sorted(array)
        elif option == 2:
            shortBubble_sorted(array)
        elif option == 3:
            inserted_sorted(array)
        elif option==4:
           select_position(array)
        elif option==5:
            str_int(array)
        elif option ==6:
            shell_sort(array)
        elif option ==7:
            quick_sort(array)
        elif option==8:
            mergeSort(array)
        elif option ==9:
            print('Obrigadoo')
            exit()
        else:
            print('Opção invalida.')
