contacts = ['Pavel', 'Kirill', 'Pasha', 'Lera', 'Aziz', 'Maftuna']
function = input('введите что хотите сделать:')

if function == 'добавить':
    new_name = input("введите новое имя")
    contacts.append(new_name)
    print(contacts)

contacts.insert(3,'Eva')
print(contacts)

contacts.extend(['Anora' , 'Imona'])
print(contacts)

contacts[0] = 'Iroda'
print(contacts)

contacts.sort()
print(contacts)

contacts.reverse()
print(contacts)

contacts.pop(3)
print(contacts)

contacts.remove('Aziz')
print(contacts)

contacts.clear()
print(contacts)







