def cache3(max_count: int):
    """Декоратор для кэширования

    Сохраняет результаты функций при тех же параметрах на max_count запусков.

    Args:
        max_count (int): максимальное кол-во запусков
    """
    def decorator(func):
        cache = {}
        count = 0

        def wrapper(*args, **kwargs):
            nonlocal count
            key = (args, tuple(kwargs.items()))
            count += 1
            if (key in cache and count < max_count):
                pass
            else:
                count = 0
                cache[key] = func(*args, **kwargs)
            return cache[key]
        return wrapper
    return decorator


if __name__ == '__main__':
    @cache3(max_count=3)
    def heavy():
        print('Сложные вычисления')
        return 1
    print(heavy())
    # Сложные вычисления
    # 1
    print(heavy())
    # 1
    print(heavy())
    # 1

    # Опять кеш устарел, надо вычислять заново
    print(heavy())
    # Сложные вычисления
    # 1
