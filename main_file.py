import re
import test_calculator

operations_symbols = "+","-","/","*","pow","root"
input_for_exit = "exit"
break_flag = False
input_1 = 'Введите первое число (или "exit" для выхода):'
input_2 = 'Введите второе число (или "exit" для выхода):'
error_1 = 'Неверный формат числа! Попробуй ещё раз:'
error_2 = 'Некорректно введен оператор! Попробуй ещё раз:'
error_3 = 'Неверный формат 2ого числа! Попробуй ещё раз:'
operation_input = f'''Введите один оператор из 6-ти доступных: 
"+", 
"-", 
"/", 
"*", 
"pow", (возведение в степень N, N - второе число) 
"root", (корень N-ой степени, N - второе число)
(либо "exit" - для выхода).'''

# Исполняемый файл представляет собой цикл
# из запросов на входные данные с защитой от ошибок при некорректном введении этих данны и с возможность прерывания этого цикла в любой момент.
# (Вводимые данные - (1)Первое число, (2)конкретная операция, (3)второе число).
# ВНИМАНИЕ:
# Результат выполнения определнных операций (конкретно "возведение в степень" и "извлечение корня")
# над ОТРИЦАТЕЛЬНЫМ значением может быть неточным из-за особенности выполнения операций
# над числами типа данных float из-за ошибки представления чисел с плавающей точкой в Python.
# (Во всех остальных случаях для получения корректных результатов используется тип данных Decimal)

i = 0
while i == 0:
    float_1 = input(f"""
{input_1}
""")
    if float_1 == input_for_exit:
        break
    else:
        while re.fullmatch(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?',float_1) == None:
                 # Функция, которая проверяет, подходит ли строка str под шаблон (под регулярку).
                 # Регулярное выражение для всех целых (отрицательных и положительных) чисел и чисел с плавающей точкой
                 # (Возможно в экспоненциальной записи - "-3.17е-14")
            if float_1 == input_for_exit:
                break_flag = True
                break
            else:
                print (error_1)
                float_1 = input(f"""

{input_1}
""")

    if break_flag:
        break
    else:
        float_1 = float(float_1)
        operation = input(f"""
{operation_input}

""")
        if operation == input_for_exit:
            break
        else:
            while operation not in operations_symbols:
                if operation == input_for_exit:
                    break_flag = True
                    break
                else:
                    print(error_2)
                    operation = input(f"""

{operation_input}

""")
        if break_flag:
            break
        float_2 = input(f"""  
{input_2}
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
                print (error_3)
                float_2 = input(f"""

{input_2}
""")
            if break_flag:
                break

            float_2 = float(float_2)

            print(test_calculator.aritmetic(float_1, operation, float_2))
