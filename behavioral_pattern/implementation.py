from abc import abstractmethod


class ArithmeticOperation:

    def __init__(self, handler):
        """
            Инициализация класса
        :param handler: следующий обработчик в цепочке
        """
        self._next_handler = handler

    @abstractmethod
    def calculate(self, operation: str) -> int:
        """
            Расчет результата вычислительной операции
            :param operation: операция записанная в виде строки
            :return: целочисленный результат
        """
        pass


class MinusOperation(ArithmeticOperation):
    """Операция вычитания"""


class PlusOperation(ArithmeticOperation):
    """Операция сложения"""


class DevideOperation(ArithmeticOperation):
    """Операция деления"""


class MultiplyOperation(ArithmeticOperation):
    """Опрация умножения"""

