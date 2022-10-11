def raise_exception(flag=1):
    if flag:
        raise ZeroDivisionError('Custom division error')
    raise FileNotFoundError('Custom FileNotFound error')

# raise_exception()


try:
    raise_exception(flag=0)
except ZeroDivisionError as error:
    print(error)
except FileNotFoundError as error:
    print(str(error) + '!!!')
finally:
    print('try, except completed')
