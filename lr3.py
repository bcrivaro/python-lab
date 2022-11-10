
#Задание 1

list_a = ['MAI', 'Sukhoi', 'MiG', 'Boeing', 'Airbus']
list_mod = []

def pares(list_a):
    for i in range(0, len(list_a), 2):
        list_mod.append(list_a[i])
    return(list_mod)

print(list_a)
pares(list_a)
print(list_mod)

#Задание 2

numbers2 = [1, 4, 3, 6, 5, 0, 9]
max_numbers = []

def num_may(numbers2):
    iprev = numbers2[0]
    for i in (numbers2):
     if i > iprev:
        max_numbers.append(i)
     iprev = i
    return(max_numbers)
    

print(numbers2)
num_may(numbers2)
print(max_numbers)



#Задание 3

numbers = [1, 0, 5, 6, 2, 3, 4, 1, 5, 6, 3, 92, 3, 4, 5, 105]


def changepos(numbers):
    maxnum = max(numbers)
    minnum = min(numbers)
    indexmax = numbers.index(maxnum)
    indexmin = numbers.index(minnum)
    numbers[indexmax] = minnum
    numbers[indexmin] = maxnum
    return(numbers)

print(numbers)
changepos(numbers)
print(numbers)

#Задание 4

dict = {}
dict['bruno'] = 'crivaro'
dict['fran'] = 'araoz'
dict['ariel'] = 'gaona'

def func(dict, key):
    value = dict[key]
    return value

key = input('insert name')
print(func(dict, key))

