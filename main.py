contacts = ['Pavel', 'Kirill', 'Pasha', 'Lera', 'Aziz', 'Maftuna']
function = input('введите что хотите сделать:')

if function == 'добавить':
    new_name = input("введите новое имя")
    contacts.append(new_name)
    print(contacts)
elif function == 'очистка':
    contacts.clear()
    print(contacts)
elif function == 'заменить':
    zamena = input('кого хотите заменить')
    zamena2 = contacts.index(zamena)
    new_name = input('введите новое имя')
    contacts[zamena2] = new_name
    print(contacts)

elif function == 'удалить':
    delete_name = input('введите имя которое хотите удалить:')

    contacts.remove(delete_name)
    print(contacts)

