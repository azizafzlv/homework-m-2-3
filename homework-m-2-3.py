"""
1) Найти среднее арифметическое списка чисел:
Пусть дан список чисел. Найти среднее арифметическое всех
чисел в списке, используя reduce.
"""

# from functools import reduce

# numbers = [1, 2, 3, 4, 5]

# length_of_num = len(numbers)
# numbers = reduce(lambda x, y: x + y, numbers)

# print(f'Среднее ариф-ое списка чисел = {numbers / length_of_num}')


"""
2) Возвести каждое число в список в квадрат:
Пусть дан список чисел. Возвести каждое число в список в
квадрат, используя map. numbers = [1, 2, 3, 4, 5]
"""

# numbers = [1, 2, 3, 4, 5]

# numbers = list(map(lambda x: pow(x, 2), numbers))

# print(numbers)


"""
3) Найти наименьший элемент в списке:
Пусть дан список чисел. Найти наименьший элемент в списке,
используя reduce. numbers = [4, 7, 2, 9, 1]
"""

# from functools import reduce

# numbers = [4, 7, 2, 9, 1]

# numbers = reduce(lambda x, y: y if (x > y) else x, numbers)

# print(numbers)


"""
4) Преобразовать список чисел из строки в числа:
Пусть дан список строк, представляющих числа. Преобразовать
список строк в список чисел, используя map. 
strings = ['1', '2', '3', '4', '5']
"""

# strings = ['1', '2', '3', '4', '5']

# result = list(map(int, strings))

# print(result)


"""
5) Отфильтровать слова, содержащие определенную подстроку:
Пусть дан список строк. Отфильтровать только те строки,
которые содержат определенную подстроку, используя filter.
strings = ['apple', 'banana', 'cherry', 'grape', 'watermelon']
substring = 'an'
"""

# strings = ['apple', 'banana', 'cherry', 'grape', 'watermelon']
# substring = 'an'

# result = list(filter(lambda x: substring in x, strings))

# print(result)


"""
6) Отфильтровать числа, которые делятся на определенное число:
Пусть дан список чисел. Отфильтровать только те числа, которые
делятся на определенное число, используя filter.
numbers = [15, 20, 25, 30, 35, 40]
divisor = 5
"""

#они же все делятся на 5, поэтому я сделаю еще задачу с другими числами
#1)
# numbers = [15, 20, 25, 30, 35, 40]
# divisor = 5

# print(list(filter(lambda x: x % divisor == 0, numbers)))

#2)
# numbers1 = [10, 13, 20, 44, 12]
# divisor1 = 2

# print(list(filter(lambda x: x % divisor1 == 0, numbers1)))


"""
7) Сложить цифры числа:
Пусть дано число. Сложить все его цифры, используя
map и разложение на цифры.
num = 12345
"""

# num = 12345
# result = sum(map(int, str(num)))

# print(result)