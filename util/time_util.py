def runtime(func):
    import time

    def print_time(*args):
        start_time = time.time()
        result = func(*args)

        print(func.__name__ + " (1 ~ " + "{:,}".format(*args) + ")")
        print(time.time() - start_time)

        return result
    return print_time
