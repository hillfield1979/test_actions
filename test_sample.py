from contextlib import contextmanager

import calculation


def test_sample(mocker):
    mocker.patch.object(calculation, '_tasks_db', new=stub_tasks_db)
    mocker.patch.object(calculation, 'mymult', return_value=15)
    mocker.patch.object(calculation, 'myadd', new=stub_myadd)
    assert calculation.calc_sample() == 5


def stub_myadd(t1, t2):
    print('stub_stub_myadd')
    return t1 / t2


@contextmanager
def stub_tasks_db():
    print('stub_context_start')
    yield
    print('stub_context_end')
