from random import randint
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst




def binary_search(find_num, lst):
    pos = 0
    resultOK = False
    first = 0
    last = len(lst) - 1
    while first <= last:
        middle = (first + last) // 2
        if lst[middle] == find_num:
            first = middle
            last = first - 1
            resultOK = True
            pos = middle
        elif find_num > lst[middle]:
            first = middle + 1
        else:
            last = middle - 1
    if resultOK:
        print(f'Число найдено под индексом', pos)
    else:
        print(f'Число не найдено ')

my_list =[]
for num in range(11):
    my_list.append(randint(0, 50))
print('Unsorted list:', my_list)
sorted_list = bubble_sort(my_list)
print('Sorted list:', sorted_list)
search = int(input('Введите ваше число из списка:'))
binary_search(search,sorted_list)



