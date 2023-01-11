from src.calc import Somador, operacaoError, Subt, Multiplicacao, Divisor
import pytest


@pytest.mark.parametrize("op1, op2, res_esp", [(1, 1, 2), (1, 7, 8), (6, 9, 15)])
def test_soma(op1, op2, res_esp):
    somador = Somador()
    resultado = somador.soma(op1, op2)
    assert resultado == res_esp


def test_somaDecimal():
    somador = Somador()
    with pytest.raises(operacaoError):
        somador.soma(4.3, 1)

def test_somaInteiro():
    somador = Somador()
    with pytest.raises(operacaoError):
        somador.soma(-4, -2)

def test_somaString():
    somador = Somador()
    with pytest.raises(operacaoError):
        somador.soma("3", "3")


@pytest.mark.parametrize("op1, op2, res_esp", [(1, 1, 0), (12, 7, 5), (30, 8, 22)])
def test_sub(op1, op2, res_esp):
    subt = Subt()
    resultado =subt.subtracao(op1, op2)
    assert resultado == res_esp


def test_subDecimal():
    subt = Subt()
    with pytest.raises(operacaoError):
        subt.subtracao(4.3, 1)


def test_subInteiro():
    subt = Subt()
    with pytest.raises(operacaoError):
        subt.subtracao(-4, -2)


def test_subResult():
    subt = Subt()
    with pytest.raises(operacaoError):
        subt.subtracao(1, 4)


def test_subString():
    subt = Subt()
    with pytest.raises(operacaoError):
        subt.subtracao("3", "3")


@pytest.mark.parametrize("op1, op2, res_esp", [(1, 1, 1), (4, 7, 28), (30, 8, 240)])
def test_mult(op1, op2, res_esp):
    multiplicacao = Multiplicacao()
    resultado = multiplicacao.multiplicador(op1, op2)
    assert resultado == res_esp


def test_multDecimal():
    multiplicacao = Multiplicacao()
    with pytest.raises(operacaoError):
        multiplicacao.multiplicador(4.3, 1)


def test_multInteiro():
    multiplicacao = Multiplicacao()
    with pytest.raises(operacaoError):
        multiplicacao.multiplicador(-4, -2)


def test_multString():
    multiplicacao = Multiplicacao()
    with pytest.raises(operacaoError):
        multiplicacao.multiplicador("3", "3")


@pytest.mark.parametrize("op1, op2, res_esp", [(1, 1, 1), (20, 4, 5), (30, 15, 2)])
def test_div(op1, op2, res_esp):
    divisor = Divisor()
    resultado = divisor.divisao(op1, op2)
    assert resultado == res_esp


def test_divDecimal():
    divisor = Divisor()
    with pytest.raises(operacaoError):
        divisor.divisao(4.3, 1)


def test_divInteiro():
    divisor = Divisor()
    with pytest.raises(operacaoError):
        divisor.divisao(-4, -2)


def test_divString():
    divisor = Divisor()
    with pytest.raises(operacaoError):
        divisor.divisao("3", "3")


def test_divZero():
    divisor = Divisor()
    with pytest.raises(operacaoError):
        divisor.divisao(2, 0)


def test_divResult():
    divisor = Divisor()
    with pytest.raises(operacaoError):
        divisor.divisao(1, 2)
