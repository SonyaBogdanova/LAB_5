"LAB_5"

def p1():
    num = int(input('Введите число: '))
    x = [ 5, 8, 9, 2, 0 ]
    if num in x:
        print("Вы угадали число!")
    else:
        print('Такого числа нет!')

def p2():
    z = [5, 8, 9, 9, 1, 7, 7]
    duble = {str(x) for x in z if z.count(x) > 1}
    x = lambda: print('nothing')
    y = lambda: print(' '.join(duble))
    x() if len (duble) < 1 else y()

def p3():
    week = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
    weekends = int(input('Сколько выходных Вам надо?: '))
    print('Ваши выходные дни: ', *week[:-weekends -1:-1])
    print('Ваши рабочие дни: ', *week[:-weekends])
    print()

def p4():
    import random

    a = ['Акимов(A)', 'Королев(A)', 'Котов(A)', 'Голубёва(A)', 'Иванов(A)', 'Ларионов(A)', 'Виноградова(A)', 'Егорова(A)', 'Соболева(A)', 'Трофимова(A)']
    b = ['Болдырёва(B)', 'Андреев(B)', 'Винокурова(B)', 'Исаева(B)', 'Иванов(B)', 'Баранова(B)', 'Воробьёва(B)', 'Петров(B)', 'Наумова(B)', 'Кириллова(B)']
    a_fix = ", ".join(a)
    b_fix = ", ".join(b)

    print("  Список А:", "\n", a_fix, '\n ', "Список B:", "\n", b_fix)

    random.shuffle(a)
    test_a = random.sample(a, 5)

    random.shuffle(b)
    test_b = random.sample(b, 5)

    mix = []
    mix = test_a + test_b
    mix_fix = ", ".join(mix)
    print('\n', 'ПУНКТ а): {спортивная команда}', '\n', mix_fix)

    chislo = len(mix_fix)
    print('\n', 'ПУНКТ b):','\n', chislo, 'символов.')

    s = sorted(mix)
    s_fix = ', '.join(s)
    print('\n','ПУНКТ c):', '\n', s_fix)

    print('\n', 'ПУНКТ d):')
    k = 0
    for i in mix:
        if i[:-3] == 'Иванов':
            k+=1

    if k != 0:
        print('В команде есть фамилия Иванов. Таких Ивановых (кол-во): ', k)
    else:
        print('Такой фамилии нет в команде.')

p1(), p2(), p3(), p4()
