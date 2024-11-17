# install pytest first: pip install pytest
# run with the following command: pytest hw_test.py

import numpy as np
from hw07 import *

def test_p1():
    y = p1(func1, 1, [0, 3], 10000, 'euler')
    assert np.isclose(y[-1], exact1(3), atol=1e-2 )
    y = p1(func1, 1, [0, 3], 100, 'midpoint')
    assert np.isclose(y[-1], exact1(3), atol=1e-2 )
    y = p1(func1, 1, [0, 3], 10, 'rk4')
    assert np.isclose(y[-1], exact1(3), atol=1e-2 )
    
def test_p2():
    y = p1(func2, 1, [0, 3], 10000, 'euler')
    assert np.isclose(y[-1], exact2(3), atol=1e-4 )
    y = p1(func2, 1, [0, 3], 100, 'midpoint')
    assert np.isclose(y[-1], exact2(3), atol=1e-4 )
    y = p1(func2, 1, [0, 3], 10, 'rk4')
    assert np.isclose(y[-1], exact2(3), atol=1e-4 )


def test_p3():
    y = p1(func3, 1, [0, 3], 10000, 'euler')
    assert np.isclose(y[-1], exact3(3), atol=1e-4 )
    y = p1(func3, 1, [0, 3], 100, 'midpoint')
    assert np.isclose(y[-1], exact3(3), atol=1e-4 )
    y = p1(func3, 1, [0, 3], 10, 'rk4')
    assert np.isclose(y[-1], exact3(3), atol=1e-4 )
    

def func1(t, y):
    return y

def func2(t, y):
    return -y

def func3(t, y):
    return -y + t


def exact1(t):
    return np.exp(t)

def exact2(t):
    return np.exp(-t)

def exact3(t):
    return 2 * np.exp(-t) + t - 1
