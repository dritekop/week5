from src.pen_and_paper.paper import Paper, check_value


class Pen:
    def __init__(self, ink_capacity: int) -> None:
        self._ink_capacity = check_value(ink_capacity)
        self._ink_amount = check_value(ink_capacity)

    @property
    def ink_capacity(self) -> int:
        return self._ink_capacity

    @property
    def amount(self) -> int:
        return self._ink_amount

    def write(self, message: str, paper: Paper) -> None:
        if len(message) > self.amount:
            message = message[:self.amount]
        self._ink_amount -= paper.add_content(message)

    def refill(self) -> None:
        self._ink_amount = self._ink_capacity

    def __str__(self) -> str:
        return f'{self.amount}/{self.ink_capacity}'


if __name__ == '__main__':  # pragma: no cover
    print('no cover')
