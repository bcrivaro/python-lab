#Задание 1

numbers = []
for i in range(0,10):
    for i in input('Insert numbers: ').split():
        numbers.append(int(i))
print(numbers)
print(sum(numbers))


#Задание 2

numbers = []
for i in input('Insert numbers, separated by spaces: ').split():
    numbers.append(int(i))
num_of_0 = numbers.count(0)
print(num_of_0)


#Задание 3

n = int(input('Insert natural number: '))
a = ''
for i in range(1, n+1):
    a = a + str(i)
    print(a)


#Задание 4

n = int(input('Insert natural number: '))
for i in range(1, n+1):
    for a in range(1, n+1-i):
        print(' ', end = '')
    for b in range(1, i+1):
        print(b, end = '')
    for c in range(i-1, 0, -1):
        print(c, end = '')
    print()