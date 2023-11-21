if __name__ == '__main__':
    prev_err = None
    for i in range(4):
        try:
            if i != 2:
                raise KeyError('PUTIN')
            else:
                raise TypeError('BIDEN')
        except Exception as err:
            if str(prev_err) == str(err):
                message = f'Сбой в работе программы: {err}'
                print('VLADIMIR')
            print(err)
            prev_err = err
