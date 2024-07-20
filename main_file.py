

import test_calculator

symbols = "+","-","/","*","**","root"

int_1 = input(f"""
Введите первое число:
""")
while int_1.isdigit() != True:
    print ('Неверный формат числа! Попробуй ещё раз:')
    int_1 = input(f"""

Введите первое число:
""")

int_1 = int(int_1)
operation = input(f"""
Введите оператор (из 6-ти доступных: "+", "-", "/", "*", "**", "root".):
""")
while operation not in symbols:
    print('Некорректно введен оператор! Попробуй ещё раз:')
    operation = input(f"""

Введите оператор (один из 6-ти доступных: "+", "-", "/", "*", "**", "root".):
""")

int_2 = input(f"""
Введите второе число:
""")
while int_2.isdigit() != True:
    print ('Неверный формат 2ого числа! Попробуй ещё раз:')
    int_2 = input(f"""

Введите второе число:
""")

int_2 = int(int_2)

print(test_calculator.aritmetic(int_1, operation, int_2))









