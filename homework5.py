immutable_var = (123,33,0,[666,13])
print(immutable_var)
print('Кортеж менять нельзя, но изменяемые типы данных записанные в кортеж менять можно.')
immutable_var[3][1] = 9
print(immutable_var)
mutable_list = [1,3,9,2,5]
print(mutable_list)
mutable_list[3] = 987654321
mutable_list[2] = False
print(mutable_list)