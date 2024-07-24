import re
import test_calculator

operations_symbols = "+","-","/","*","pow","root"
input_for_exit = "exit"
break_flag = False

# Исполняемый файл выполнения определенной операции над конкретными вводимыми значениями реализован в виде цикла
# с запросами на входные данные с возможностью прервать этот цикл в любой из 3-х стадий запросов.
# (Первое вводимое число, конкретная операция, второе вводимое число).
# ВНИМАНИЕ:
# Результат выполнения определнных операций (конкретно "возведение в степень" и "извлечение корня")
# над ОТРИЦАТЕЛЬНЫМ значением может быть неточным из-за особенности выполнения операций
# над числами типа данных float из-за ошибки представления чисел с плавающей точкой в Python.
# (Во всех остальных случаях для получения корректных результатов доступных операций используется тип данных Decimal)

i = 0
while i == 0:
    float_1 = input(f"""
Введите первое число (или "exit" для выхода):
""")
    if float_1 == input_for_exit:
        break
    else:
        while re.fullmatch(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?',float_1) == None:
                 # Функция, которая проверяет, подходит ли строка str под шаблон (под регулярку).
                 # Регулярное выражение для всех целых (отрицательных и положительных) чисел и чисел с плавающей точкой
                 # (Возможно в экспоненциальной записи - "-3.17е-14")
            while float_1 == input_for_exit:
                break_flag = True
                break
            if break_flag:
                break
            print ('Неверный формат числа! Попробуй ещё раз:')
            float_1 = input(f"""

Введите первое число (или "exit" для выхода):
""")

    if break_flag:
        break
    else:
        float_1 = float(float_1)
        operation = input(f"""
Введите один оператор из 6-ти доступных: 
"+", 
"-", 
"/", 
"*", 
"pow", (возведение в степень N, N - второе число) 
"root", (корень N-ой степени, N - второе число)
(либо "exit" - для выхода).

""")
        if operation == input_for_exit:
            break
        else:
            while operation not in operations_symbols:
                if operation == input_for_exit:
                    break_flag = True
                    break
                else:
                    print('Некорректно введен оператор! Попробуй ещё раз:')
                    operation = input(f"""

Введите оператор один из 6-ти доступных: 
"+", 
"-", 
"/", 
"*", 
"pow", (возведение в степень N, N - второе число) 
"root", (корень N-ой степени, N - второе число)
(либо "exit" - для выхода).

""")
        if break_flag:
            break
        float_2 = input(f"""  
Введите второе число (или "exit" для выхода):
""")
        if float_2 == input_for_exit:
            break
        else:
            while re.fullmatch(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', float_2) == None:
            # while int_2.isdigit() != True:
            # Метод, проверяющий строку на наличие только цифр.
                if float_2 == input_for_exit:
                    break_flag = True
                    break
                print ('Неверный формат 2ого числа! Попробуй ещё раз:')
                float_2 = input(f"""

Введите второе число (или "exit" для выхода):
""")
            if break_flag:
                break

            float_2 = float(float_2)

            print(test_calculator.aritmetic(float_1, operation, float_2))
