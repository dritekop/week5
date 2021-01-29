import pytest

from src.pen_and_paper.pen import Pen
from src.pen_and_paper.paper import Paper


def test_pen_and_paper_construction():
    paper = Paper(5)
    assert paper.max_symbols == 5
    assert paper.symbols == 0
    assert paper.material == ''
    pen = Pen(5)
    assert pen.amount == 5
    assert pen.ink_capacity == 5


@pytest.mark.parametrize('ink_value, paper_space, message', [
    (10, 5, 'Hello'),
    (10, 10, 'Hello!'),
    (1, 10, 'H')
])
def test_write_and_add_content(ink_value, paper_space, message):
    pen = Pen(ink_value)
    paper = Paper(paper_space)
    pen.write(message, paper)
    assert paper.material == message
    assert pen.amount == pen.ink_capacity - len(message)


def test_write_and_add_content_limits():
    pen = Pen(5)
    paper = Paper(10)
    pen.write('Hello, world!', paper)
    assert paper.material == 'Hello'
    other_pen = Pen(10)
    other_paper = Paper(5)
    other_pen.write('Hello, world!', other_paper)
    assert other_paper.material == 'Hello'


def test_refill_pen():
    pen = Pen(1)
    paper = Paper(1)
    pen.write('H', paper)
    assert pen.amount == 0
    pen.refill()
    assert pen.amount == 1


def test_construction_failed():
    with pytest.raises(ValueError):
        pen = Pen(0)


def test_to_string():
    pen = Pen(1)
    assert str(pen) == '1/1'
    paper = Paper(1)
    assert str(paper) == '\nfree space: 1 of 1'
