import sys
 
name = str(input('Укажите свое имя: '))
if name == 'Иван':
    print('Ваше имя не подходит!')
    sys.exit(0)
age = int(input('Укажите свой возраст: '))
if 16 <= age < 75:
    print("Поздравляем вы поступили в ВГУИТ!")
else:
    print("Введите возраст корректно")
