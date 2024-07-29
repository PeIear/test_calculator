import test_vallue
import decimal

# Основная функция для реализации всех операций из main_file. Для перевода значений в тип данных Decimal используется
# метод Decimal из библиотеки decimal

def aritmetic(float_1, operation, float_2):
    if operation == '+':
        value_1 = test_vallue.value_chek(float_1)
        value_2 = test_vallue.value_chek(float_2)
        value_result = test_vallue.value_chek(decimal.Decimal(str(float_1)) + decimal.Decimal(str(float_2)))
        result = f"""

Выражение:
{value_1} {operation} {value_2}

Результат:
{value_result}"""

        return result

    elif operation == '-':
        value_1 = test_vallue.value_chek(float_1)
        value_2 = test_vallue.value_chek(float_2)
        value_result = test_vallue.value_chek(decimal.Decimal(str(float_1)) - decimal.Decimal(str(float_2)))
        result = f"""

Выражение:
{value_1} {operation} {value_2}

Результат:
{value_result}"""

        return result

    elif operation == '/':
        value_1 = test_vallue.value_chek(float_1)
        value_2 = test_vallue.value_chek(float_2)
        value_result = test_vallue.value_chek(decimal.Decimal(str(float_1)) / decimal.Decimal(str(float_2)))
        if float_2 == 0:
            result = f"""

Выражение:
{value_1} {operation} {value_2}

На ноль делить нельзя!"""
        else:
            result = f"""

Выражение:
{value_1} {operation} {value_2}

Результат:
{value_result}"""

        return result

    elif operation == '*':
        value_1 = test_vallue.value_chek(float_1)
        value_2 = test_vallue.value_chek(float_2)
        value_result = test_vallue.value_chek(decimal.Decimal(str(float_1)) * decimal.Decimal(str(float_2)))
        result = f"""

Выражение:
{value_1} {operation} {value_2}

Результат:
{value_result}"""

        return result

    elif operation == 'pow':
        value_1 = test_vallue.value_chek(float_1)
        value_2 = test_vallue.value_chek(float_2)
        if float_1 >= 0:
            value_result = test_vallue.value_chek(decimal.Decimal(str(float_1)) ** decimal.Decimal(str(float_2)))
        else:
            value_result = test_vallue.value_chek((float_1 ** float_2))
        result = f"""
        
Выражение:
{value_1} {operation} {value_2}
Число {value_1} в {value_2}-й степени

Результат:
{value_result}"""

        return result

    elif operation == 'root':
        value_1 = test_vallue.value_chek(float_1)
        value_2 = test_vallue.value_chek(float_2)
        if float_1 >= 0:
            value_result = test_vallue.value_chek(decimal.Decimal(str(float_1)) ** decimal.Decimal(decimal.Decimal(str(1))/decimal.Decimal(str(float_2))))
        else:
            value_result = test_vallue.value_chek((float_1 ** (1/float_2)))
        result = f"""
        
Выражение:
{value_1} {operation} {value_2}
{value_2}(th) {operation} of a number {value_1}
Корень {value_2}-й степени из числа {value_1}

Результат:
{value_result}"""

        return result
