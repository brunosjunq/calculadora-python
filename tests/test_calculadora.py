# tests/test_calculadora.py

import pytest
from src.calculadora import somar, subtrair, multiplicar, dividir

def test_somar():
    assert somar(1, 2) == 3
    assert somar(-1, 1) == 0

def test_subtrair():
    assert subtrair(2, 1) == 1
    assert subtrair(-1, -1) == 0

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-1, 1) == -1

def test_dividir():
    assert dividir(6, 3) == 2
    with pytest.raises(ValueError):
        dividir(1, 0)
