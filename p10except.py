def primer(n_one, n_two, zn, result):
    print(str(n_one) + zn + str(n_two) + '=')
    slova(result)


def slova(result):
    print(result)
    print('Желаете закончить использование программы')
    print('Введите - "выход"')


def step(stepen):
    stp_c = True
    while stp_c:
        try:
            int(stepen) == int(stepen)
            stepen = int(stepen)
            result = number_one ** stepen
            print(str(number_one) + " в степени " + str(stepen) + " =")
            slova(result)
            stp_c = False
        except ValueError:
            stepen = input('Введите степень! ')
            continue


def krn(kor):
    krn_c = True
    while krn_c:
        try:
            int(kor) == int(kor)
            kor = int(kor)
            result = number_one ** (1 / kor)
            print("Корень " + str(kor) + " степени из " + str(number_one) + " =")
            slova(result)
            krn_c = False
        except ValueError:
            kor = input('Введите степень корня! ')
            continue


calc = True
while calc:
    number_one = input('Введите первое число: ')
    if number_one == 'выход':
        print('Списибо за использование программы.')
        break
    try:
        int(number_one) == int(number_one)
        number_one = int(number_one)
        two = True
    except ValueError:
        print('Введите число!')
        continue
    while two:
        number_two = input('Введите второе число (можно ввести "степень"/"корень"): ')
        if number_two == 'выход':
            print('Списибо за использование программы.')
            calc = False
            break
        elif number_two == 'назад':
            two = False
            continue
        elif number_two == 'степень':
            stepen = input('Какая степень? ')
            step(stepen)
            break
        elif number_two == 'корень':
            kor = input('Корень какой степени? ')
            krn(kor)
            break
        try:
            int(number_two) == int(number_two) or number_two == "корень" or number_two == "степень"
        except ValueError:
            print('Введите число!')
            print('Первое число введено - ' + str(number_one))
            print('Желаете заменить первое число, введите "назад"')
            continue
        znak = True
        while znak:
            number_two = int(number_two)
            znaki = input('Введите знак - "+", "-", "*", "/": ')
            if znaki == "/":
                try:
                    result = number_one / number_two
                except ZeroDivisionError:
                    print('Нельзя делить на 0.')
                else:
                    primer(number_one, number_two, znaki, result)
                    znak = False
                    two = False
            elif znaki == "+":
                result = number_one + number_two
                primer(number_one, number_two, znaki, result)
                znak = False
                two = False
            elif znaki == "-":
                result = number_one - number_two
                primer(number_one, number_two, znaki, result)
                znak = False
                two = False
            elif znaki == "*":
                result = number_one * number_two
                primer(number_one, number_two, znaki, result)
                znak = False
                two = False
            elif znaki == "выход":
                print('Списибо за использование программы.')
                znak = False
                two = False
                calc = False
                break
            elif znaki == "назад":
                break
            elif znaki == "стоп":
                two = False
                break
            else:
                print("Введите знак!")
                print("Первое число: " + str(number_one))
                print("Второе число: " + str(number_two))
                povtor = input("Работать с этими числами? ('да'/'нет'): ")
                pov = True
                while pov:
                    if povtor == 'да':
                        break
                    elif povtor == 'нет':
                        pov = False
                        two = False
                        znak = False
                    elif povtor == "выход":
                        print('Списибо за использование программы.')
                        znak = False
                        two = False
                        calc = False
                        break
                    else:
                        povtor = input("Введите 'да'/'нет': ")
