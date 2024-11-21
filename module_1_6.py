my_dict = {'Nikita': 1995, 'Kristina': 1995, 'Alena': 2013, 'Anna': 2011}
print(my_dict)
print(my_dict['Anna'])
print(my_dict.get('Alex'))
my_dict.update({'Max': 2000, 'Nina': 1998})
print(my_dict)
del my_dict['Max']
print(my_dict)
j = my_dict.pop('Alena')
print(j)
print(my_dict)
print()

my_sat = {1, 1, 2, 2, 3, 3, 'apple', 'apple', True, True}
print(my_sat)
my_sat.add('Tanos')
my_sat.discard(1)
print(my_sat)