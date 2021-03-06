# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк
#  и сохраните в переменные, выведите на экран.

print ("Задание 1.")
s = "qwert"
print(s)

q1 = input("Введите число 1: ")
q2 = input("Введите число 2: ")
q3 = input("Как Вас зовут? ")

print("Привет, " + q3 + "!")
print("Ты ввел числа " + q1 + " и " + q2)
print("*****************")

# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

print ("Задание 2.")
x = int(input("Введите время в секундах: "))

hours = x // 360
minutes = (x - hours * 360) // 60
seconds = (x - hours * 360) % 60

print(f"{hours}:{minutes}:{seconds}")

print("*****************")

# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369

print ("Задание 3.")
n = input("Введите число: ")
print(int(n)+int(n*2)+int(n*3))
print("*****************")

# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

print ("Задание 4.")
n = str(input("Введите число: "))
max_n = n[0]
for i in n:
    if int(i) > int(max_n):
        max_n = i
print(max_n)
print("*****************")

# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

print ("Задание 5.")
revenue = int(input("Введите сумму выручки: "))
expenses = int(input("Введите сумму расходов: "))
if revenue > expenses:
    print("Финансовый результат - прибыль")
    emp = int(input("Введите количество сотрудников: "))
    print("Рентабельность на одного сотрудника " + str( revenue / expenses / emp))
elif revenue == expenses:
    print("Финансовый результат = 0")
else:
    print("Финансовый результат - убыток")

print("*****************")

# 6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
#
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

print ("Задание 6.")
a = int(input("Введите количество км первой пробежки: "))
b = int(input("Введите количество км - цель: "))
i = 1
while a < b:
    a = 1.1 * a
    i += 1
print("на " + str(i) + "-й день спортсмен достиг результата - не менее " + str(b) + " км")
print("*****************")