def raise_exception(flag=1):
    if flag:
        raise ZeroDivisionError('Custom division error')
    raise FileNotFoundError('Custom FileNotfound error')

try:
    raise_exception(flag=0)
except (ZeroDivisionError, FileNotFoundError) as error:
    print(error)
finally:
    print('try, except completed')