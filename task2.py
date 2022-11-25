#Задайте список из n чисел последовательности (1 + 1/n)^n. Вывестив консоль сам список и сумму его элементов.

n = int(input('Ввести количество чисел в списке: '))
def numbers(n):
    summ = 0
    for i in range(n):
        a = int(input(f'Введите число {i+1}'))
        a= (1+1/a)**a
        summ = a+summ
        i+= 1
    return summ
print('Сумма чисел равна', round(numbers(n), 2))




