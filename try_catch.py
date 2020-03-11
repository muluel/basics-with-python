try:
    answer = 10/2
    number = int(input('Enter a number: '))
    print('The number is', number)
except ZeroDivisionError as err:
    print(err)
except ValueError as v_err:
    print(v_err)