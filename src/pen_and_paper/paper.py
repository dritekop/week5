def check_value(value: int) -> int:
    if value <= 0:
        raise ValueError(f'Value should be positive')
    return value


class Paper:
    def __init__(self, max_symbols: int) -> None:
        self._max_symbols = check_value(max_symbols)
        self._symbols = 0
        self._material = ''

    @property
    def max_symbols(self) -> int:
        return self._max_symbols

    @property
    def symbols(self) -> int:
        return self._symbols

    @property
    def material(self) -> str:
        return str(self._material)

    def add_content(self, text: str) -> int:
        available = self.max_symbols - self.symbols
        if len(text) > available:
            text = text[:available]
            self._material = text
        else:
            self._material += text
        self._symbols += len(text)
        return len(text)

    def __str__(self) -> str:
        return f'{self._material}\nfree space: {self.max_symbols - len(str(self.material))} of {self.max_symbols}'


if __name__ == '__main__':  # pragma: no cover
    paper = Paper(5)
    # paper.add_content('Hello!')
    print(paper)
