import pytest

from src.keyboard import Keyboard


@pytest.fixture
def kb():
    return Keyboard("Dark Project KD87A", 9600, 5)


def test_kb(kb):
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"


def test_change_lang(kb):
    assert str(kb.language) == "EN"

    assert kb.language == "EN"

    with pytest.raises(AttributeError):
        kb.language = "CH"

        kb.change_lang()
