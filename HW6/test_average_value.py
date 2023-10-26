from typing import Literal
import pytest
from average_value import AverageValue

@pytest.fixture(name='list1')
def list_1():
    """Возвращает 1-ый тестовый массив"""
    return [1, 2, 3, 4, 5]

@pytest.fixture(name='list2')
def list_2():
    """Возвращает 2-ой тестовый массив"""
    return [3, 4, 5, 6, 7]


def test_init(list1: list[int], list2: list[int]):
    """Проверка корректной инициализации класса"""
    lists = AverageValue(list1, list2)
    assert lists.list_a == list1
    assert lists.list_b == list2


def test_get_lists_averages(list1: list[int], list2: list[int]):
    """Проверка средних значений списков размером больше 1"""
    lists = AverageValue(list1, list2)
    assert lists.average_val() == (3, 5)

@pytest.mark.parametrize('list1, list2, result',
                         [([1, 2, 3], [], (2, 0)), ([], [1, 2, 3], (0, 2)), ([], [], (0, 0))])
def test_get_empty_lists_averages(list1: list[int], list2: list[int], result: tuple[Literal[2], Literal[0]] | tuple[Literal[0], Literal[2]] | tuple[Literal[0], Literal[0]]):
    """Проверка средних значений, если один или оба списка пустые"""
    lists = AverageValue(list1, list2)
    assert lists.average_val() == result


@pytest.mark.parametrize('list1, list2, result',
                         [([1, 2, 3], [5], (2, 5)), ([5], [1, 2, 3], (5, 2)), ([5], [5], (5, 5))])
def test_get_one_elemented_lists_averages(list1: list[int], list2: list[int], result: tuple[Literal[2], Literal[5]] | tuple[Literal[5], Literal[2]] | tuple[Literal[5], Literal[5]]):
    """Проверка средних значений, если один или оба списка имеют только один элемент"""
    lists = AverageValue(list1, list2)
    assert lists.average_val() == result


def test_first_average_more(list1: list[int], list2: list[int], capfd: pytest.CaptureFixture[str]):
    """Проверка сообщения, когда среднее значение первого списка больше второго"""
    lists = AverageValue(list1, list2)
    lists.comparison_average_val()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'Первый список имеет большее среднее значение'


def test_second_average_more(list1: list[int], list2: list[int], capfd: pytest.CaptureFixture[str]):
    """Проверка сообщения, когда среднее значение второго списка больше первого"""
    lists = AverageValue(list1, list2)
    lists.comparison_average_val()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'Второй список имеет большее среднее значение'


def test_equal_averages(list1: list[int], list2: list[int], capfd: pytest.CaptureFixture[str]):
    """Проверка сообщения, когда средние значения списков равны"""
    lists = AverageValue(list1, list2)
    lists.comparison_average_val()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'Средние значения равны'