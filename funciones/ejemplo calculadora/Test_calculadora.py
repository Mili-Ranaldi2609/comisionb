import pytest
from funciones_calculadora import *

@pytest.mark.parametrize("a, b, res",[
    (2,4,6),
    (-4,6,2),
    (-5,-1,-6),
])
def test_suma(a, b, res):
    assert suma(a, b) == res

@pytest.mark.parametrize("a, b, res",[
    (2,4,-2),
    (-4,6,-10),
    (-5,-1,-4),
])
def test_resta(a, b, res):
    assert resta(a, b) == res

@pytest.mark.parametrize("a, b, res",[
    (2,4,8),
    (-4,6,-24),
    (-5,-1,5),
])
def test_multiplicacion(a, b, res):
    assert multiplicacion(a, b) == res

@pytest.mark.parametrize("a, b, res",[
    (4,2,2),
    (-6,2,-3),
    (-5,-1,5),
    (3,0,"No se puede dividir por cero!")
])
def test_division(a, b, res):
    assert division(a, b) == res