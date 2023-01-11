import numbers


class operacaoError(Exception):
    pass


class Somador:
    def soma(self, op1, op2):
        self._check_int_(op1)
        self._check_int_(op2)
        return op1 + op2

    def _check_int_(self, op):
        if not isinstance(op, numbers.Integral) or op < 0:
            raise operacaoError(f"{op} não é um número natural")


class Subt:
    def subtracao(self, op1, op2):
        self._check_int_(op1)
        self._check_int_(op2)
        self._check_result_(op1, op2)
        return op1 - op2

    def _check_int_(self, op):
        if not isinstance(op, numbers.Integral) or op < 0:
            raise operacaoError(f"{op} não é um número natural")

    def _check_result_(self, op1, op2):
        if (op1 - op2) < 0:
            raise operacaoError(f"O resultado dessa operação não é natual")


class Multiplicacao:
    def multiplicador(self, op1, op2):
        self._check_int_(op1)
        self._check_int_(op2)
        return op1 * op2

    def _check_int_(self, op):
        if not isinstance(op, numbers.Integral) or op < 0:
            raise operacaoError(f"{op} não é um número natural")


class Divisor:
    def divisao(self, op1, op2):
        self._check_int_(op1)
        self._check_int_(op2)
        self._check_zero_(op2)
        self._check_result(op1, op2)
        return op1 / op2

    def _check_int_(self, op):
        if not isinstance(op, numbers.Integral) or op < 0:
            raise operacaoError(f"{op} não é um número natural.")

    def _check_zero_(self, op):
        if op == 0:
            raise operacaoError(f"Não é possível realizar divisão por zero")

    def _check_result(self, op1, op2):
        if op1 % op2 != 0:
            raise operacaoError(f"O resultado dessa operação não é natual")
