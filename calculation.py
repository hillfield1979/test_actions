from contextlib import contextmanager

def mymult(t1, t2):
    return t1 * t2


def myadd(t1, t2):
    return t1 + t2


def calc_sample():
    with _tasks_db():
        t1 = 1
        t2 = 2
        t3 = 3
        tmp = mymult(t1, t2)
        tmp2 = myadd(tmp, t3)
    return tmp2


@contextmanager
def _tasks_db():
    print('context_start')
    yield
    print('context_end')
