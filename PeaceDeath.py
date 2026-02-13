import random as rnd
import time
print("Задание №1\n")
max = int(input("Введите максимальное число для элемента списка\n"))
list = [rnd.randint(0, max) for i in range(0, int(input("Введите количество элементов списка\n")))]
list.sort() #Сортируем список для корректной работы бинарного поиска

#задание 1 и 4
def linear(lys, element):
    for i in range(0, len(lys)):
        if lys[i] == element :
            return i
    return -1
def Binary(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while(first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid - 1
            else:
                first = mid+1
    return index
search = int(input("Введите искомый элемент\n"))
print("Линейный поиск")
start = time.process_time() #Задаем начало отсчёта
print("Индекс искомого элемента: ", linear(list, search))
end = time.process_time() #Считываем конец отсчёта
print("Время выполнения поиска: ", end-start) #Выводим время выполнения
print("Бинарный поиск")
start = time.process_time() #Задаем начало отсчёта
print("Индекс искомого элемента: ",Binary(list, search))
end = time.process_time() #Считываем конец отсчёта
print("Время выполнения поиска: ", end-start, '\n')  #Выводим время выполнения
#В случае когда искомый элемент небольшой (Стоит в начале списка) линейный поиск
#справляется примерно одинаково с бинарным, но если элемент большой (стоит в конце списка),
#то бинарный поиск справляется в разы быстрее, тк линейному приходится перебирать все элементы
#списка, чтобы найти искомый. В итоге, я считаю бинарный поиск более эффективной чем линейный,
#Но и тот, и другой имеет явные минусы: для корректной работы бинарного требуется, чтобы список
#Был сортирован, а для линейной сортировки, чтобы искомый элемент находился в начале списка
#Итоговый ответ: Вычислительная сложность линейного поиска больше

#Задание 2
print("Задание №2\n")
maximum = int(input("Введите максимальное число для элемента списка\n"))
n = [rnd.randint(0, maximum)for j in range(0, int(input("Введите количество элементов списка\n")))]
lenght = len(n)
matrix = []
print(n)
count = 0
for i in range(0, lenght):
    for j in range(0, lenght):
        if [j, i] in matrix or i == j:
            pass
        else:
            matrix.append([i, j])
print(matrix)

for i in range(0, len(matrix)):
    summ = (n[matrix[i][0]] + n[matrix[i][1]])

    if summ/2 != int(summ/2):
        print(summ)
        count+=1
print(count)

#Задание №3 не выполнено