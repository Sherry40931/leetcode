from time import time


def timing(fn):
    def wrap(self, *args):
        t1 = time()
        fn(self, *args)
        t2 = time()
        print(f'{fn.__name__}: {t2 - t1}')
    return wrap