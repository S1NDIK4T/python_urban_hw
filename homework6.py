my_dict = {'Wasya': 1021231, 'Petya': 11333, 'uglich': 312312231231}
print(f"{my_dict}\n"
      f"{my_dict['uglich']}\n"
      f"{my_dict.get('Epron')}")
my_dict.update({"Epron-711": 123231232,
               "Denis": 42223342565})
my_dict.pop('Wasya')
print(my_dict)

my_set = {1, True, False, False, 4, 17, 'Olexiy', 'Gadya', 'Petrovich', 12, 3.231112233123}
print(my_set)
my_set.add(666)
my_set.add(13)
print(my_set)





# 2. Работа со словарями:
#   - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
# Например: Имя(str)-Год рождения(int).
#   - Выведите на экран словарь my_dict.
#   - Выведите на экран одно значение по существующему ключу, одно по отсутствуещему из словаря my_dict без ошибки.
#   - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
#  - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
#   - Выведите на экран словарь my_dict.
#
# 3. Работа с множествами:
#   - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
#   - Выведите на экран множество my_set (должны отобразиться только уникальныые значения).
#   - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
#   - Удалите один любой элемент из множества my_set.
#   - Выведите на экран измененное множество my_set.