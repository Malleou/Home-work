immutable_var = (12, 'str', True, ['Яблоко', 'мышь', 'кот'])
print(immutable_var)

# immutable_var[0] = 55
# print(immutable_var)
# Ничего не выйдет, так как для кортежа приемлема только конкатенация и умножение.
# Другие изменения вносить нельзя. Для изменений подойдёт список

mutable_list = ['space', 12, 'microphon']
mutable_list[0] = 'stars'
print(mutable_list)