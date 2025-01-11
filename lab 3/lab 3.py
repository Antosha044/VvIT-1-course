'Задание 1' + 'Задание 3'
def reading(file,type_of_reading):
    if type_of_reading=='1':
        print(file.read())
    elif type_of_reading=='2':
        for line in file:
            print(line)
    else:
        print('Вы ввели несуществующий вариант. Перезапустите программу')
try:
    with open('example.txt','r') as file:
        chose=input('Выберите тип чтения: \n 1-чтение файла целиком \n 2-чтение файла построчно \n Укажите цифру выбранного варинта ')
        reading(file,chose)
except FileNotFoundError:
    print('Файл не найден')
'Задание 2'
# def writer():
#     file=open('user_input.txt', 'w')
#     file.write(input('Введите текст:'))
# def adder():
#     file= open('user_input.txt', 'a')
#     file.write('\n' + input('Введите текст:'))
# writer(); adder()
# print(open('user_input.txt').read())