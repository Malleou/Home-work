alphabet = 'abcdefg'

# здесь код
new_alphabet = alphabet[:]
print('1:', new_alphabet)
print('2:', alphabet[::-1])
print('3:', alphabet[::2])
print('4:', alphabet[1::2])
print('5:', alphabet[1])
print('6:', alphabet[-1:-2:-1])  # Но если нужен только 1 эл-т, можно было и просто -1 написать
print('7:', alphabet[3:4])
print('8:', alphabet[-3::1])
print('9:', alphabet[3:5])
print('10:', alphabet[4:2:-1])