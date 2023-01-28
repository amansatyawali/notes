a = [1, 2, 3, 4, 5]

for i in a:
    print(f'Item :{i - 4}')

    try:
        print(f'{i / (i - 4)}')
    except ZeroDivisionError:
        print('Zero division occurred')
        break
    else:
        print('Everything ran fine')
    finally:
        print('went to finally block')

print('came out of loop')

