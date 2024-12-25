def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) == 1:
        return int(str_number) if int(str_number) != 0 else 1
    return first * get_multiplied_digits(int(str_number[1:]))


def get_multiplied_digits_2(number):
    if number == 0:
        return 1
    n = number % 10
    if n == 0:
        n = 1
    return n * get_multiplied_digits_2(number // 10)


result = get_multiplied_digits_2(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)