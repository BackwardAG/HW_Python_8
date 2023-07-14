file_path = r'\HW_Phy_8.txt'


def add_number():
    with open(file_path,'a') as p:
        p.write('\n')
        p.write(input('Введите ФИО и номер: '))

def search():
    with open(file_path,'r') as p:
        a = input('Введите искомый номер или ФИО: ')
        for line in p:
            if a in line.casefold(): print(line)

def create_phonebook():
    with open(file_path,'w') as p:
        p.write('Справочник')

def print_phonebook():
    with open(file_path,'r') as p:
        print(p.read())

def phonebook_change():
    with open(file_path,'r') as p:
        phoneb = p.readlines()
        number = input('Введите номер или ФИО изменяемой строки: ')
        modified_line = input('Введите новое ФИО и номер или ничего не вводите для удаления строки: ') + '\n'
        for i in range(len(phoneb)):
            if phoneb[i].casefold().find(number) != -1: phoneb[i] = modified_line
        phoneb = ''.join(phoneb)   
    with open(file_path,'w') as p:
        p.write(phoneb)



while True:
    p = input('Введите : 1 - для создания пустого справочника,' + '\n' 
              '2 - для добавления строки,' + '\n' 
              '3 для изменения/удаления строки,' + '\n' 
              '4 - для поиска по номеру или имени,' + '\n' 
              '5 - для вывода всего справочника. ')
    if p == '1': create_phonebook()
    elif p == '2': add_number()
    elif p == '3': phonebook_change()
    elif p == '4': search()
    elif p == '5': print_phonebook()
    else:
        print('Некорректный ввод')
    print()
    print()



