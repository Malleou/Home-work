number = int(input('Число из первой части: '))
sum_counter = 0

for sum in range(2, number + 1):
    sum_counter = 0
    if number % sum == 0:
        for numbers in range(1, (sum + 1) //2):
            a = sum - numbers
            print(numbers, a, end = '; ')