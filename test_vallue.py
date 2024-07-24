import re
import test_calculator


positive_float = 'Число с плавающей точкой'
negative_float = 'Отрицательное число с плавающей точкой'
positive_integer = 'Целое положительное число'
negative_integer = 'Целое Отрицательное число'


# Функция для определения типа входных значений (чисел)

def check_int(int):
    if re.fullmatch(r'[+]?\d+\.[1-9]\d*', str(int)) != None:
        result = positive_float
        # return False
        return result
    elif re.fullmatch(r'[-]\d+\.[1-9]\d*', str(int)) != None:
        return negative_float
    elif re.fullmatch(r'[-]\d+\.?[0]*', str(int)) != None:
        return negative_integer
    elif re.fullmatch(r'[+]?\d+\.?[0]*', str(int)) != None:
        return positive_integer



# Функция для грамотного и удобного отображения на экран пользователя результата - значений (чисел)
# с определённым типом данных (в функции выше)

def value_chek(int_test):
    if check_int(int_test) == positive_integer:
        value = int(int_test)
        return value
    elif check_int(int_test) == negative_float:
        if type(int_test) == complex:
            value = f"{int_test}"
        else:
            value = f"({float(int_test)})"
        return value
    elif check_int(int_test) == negative_integer:
        value = f"({int(int_test)})"
        return value
    else:
        if type(int_test) == complex:
            value = f"{int_test}"
        else:
            value = f"{float(int_test)}"
        return value
