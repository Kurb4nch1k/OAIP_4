def template(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print(f'Периметр: {a + b + c}')
        p = (a + b + c) / 2
        print(f'Площадь: {(p * (p - a) * (p - b) * (p - c)) ** 0.5}'
              f'\nРавнобедренный: {"да" if a == b or a == c or b == c else "нет"}'
              f'\nРавносторонний: {"да" if a == b == c else "нет"}')
    else:
        print('None')


template(6, 4, 7)