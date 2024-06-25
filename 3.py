def func_table(f, x_max, y_max):
    f = lambda x: eval(f)
    print("x\ty")
    for x in range(0, x_max + 1):
        y = f(x)
        if y <= y_max:
            print(f"{x}\t{y}")
        else:
            break
