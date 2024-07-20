

# import math

def aritmetic(int_1, operation, int_2):
    if operation == '+':
        result = f"""
Результат:
{int_1 + int_2}"""
    elif operation == '-':
        result = f"""
Результат:
{int_1 - int_2}"""
    elif operation == '/':
        if int_2 == 0:
            result = f"На ноль делить нельзя!"
        else:
            result = f"""
Результат:
{int_1 / int_2}"""
    elif operation == '*':
        result = f"""
Результат:
{int_1 * int_2}"""
    elif operation == '**':
        result = f"""
Результат:
{int_1 ** int_2}"""
    elif operation == 'root':
        result = (f"""
Результат:
{int_1 ** (1/int_2)}""")


    return result






