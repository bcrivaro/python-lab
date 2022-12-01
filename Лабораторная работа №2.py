# Задание 1

# a = True
# b = False

#1 a and b = False
#2 (a and b) or b = False
#3 (a and b) or not (a and b) = True
#4 a and b or not (a or b) or b = True
#5 b and b or not a and (a or b or a) or not (a or b) = False
#6 1 << 2 = 4
#7 1 & 0 | 1 >> 1 = 0
#8 1 & 0 | 1 >> 0 = 1
#9 0b101 & 0b111 ^ 0b111 |  = False


# Задание 2

a = (input("Insert number A:"))
b = (input("Insert number B:"))

if a == b:
    print("A and B are equals")
elif a>b:
    print("A is bigger than B")
elif b>a:
    print("B is bigger than A")


# Задание 3

a3 = (input("Insert number A"))
b3 = (input("Insert number B"))
c3 = (input("Insert number C"))

list3 = [a3, b3, c3]
print("The maximum number is", max(list3))

# Задание 4

a4 = (input("Insert number A"))
b4 = (input("Insert number B"))
c4 = (input("Insert number C"))

list4 = [a4, b4, c4]

set = set(list4)
cant = len(set)

print("The amount of unique values is:", (cant))
