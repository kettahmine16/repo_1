import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# TRIM
# Пробелы в начале
# Отсутствие пробела
# Одни пробелы


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("  Skypro", "Skypro"),
    ("Hello world", "Hello world"),
    ("   ", ""),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

# Пробел в конце


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("Skypro ", "Skypro "),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

# CONTAINS
# Символ в начале
# Символ в середине
# Символ в конце
# Повторяющийся символ
# Строка из одного символа


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "S", True),
    ("Skypro", "y", True),
    ("Skypro", "o", True),
    ("Hello", "l", True),
    ("P", "P", True),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

# Отсутствие символа
# Регистр
# Пустая строка


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "U", False),
    ("Skypro", "s", False),
    ("", "o", False),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

# DELETE
# Удаление одного символа
# Удаление части строки
# Удаление повторяющихся символов
# Удаление всех комбинаций символов
# Удаление строки


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "k", "Sypro"),
    ("Skypro", "Sky", "pro"),
    ("Hello", "l", "Heo"),
    ("bbbb", "bb", ""),
    ("Skypro", "Skypro", ""),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected

# Символ отсутствует
# Регистр
# Пустая строка


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "a", "Skypro"),
    ("Skypro", "s", "Skypro"),
    ("", "a", ""),
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
