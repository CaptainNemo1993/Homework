my_dict={'Денис':1993, 'Сергей':2002, 'Максим':1978, 'Анатолий':1945}
print(my_dict)
print(my_dict['Денис'])
print(my_dict.get('Михаил'))
my_dict.update({'Алексей':1988,
                     'Петр': 2016})
z=my_dict.pop('Сергей')
print(z)
print(my_dict)

my_set= {1, 2, 4, "Footbol", "Hockey", True,"Footbol",1 }
print(my_set)
my_set.update([False, 12])
my_set.remove(1)
print(my_set)