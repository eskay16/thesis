import pytest
from heal.paths import get_path, set_path, flatten


def test_get_path_top_level():
    assert get_path({"totalAmount": 99.9}, "totalAmount") == 99.9


def test_get_path_deeply_nested():
    assert get_path({"a": {"b": {"c": 1}}}, "a.b.c") == 1


def test_get_path_falsy_value():

    assert get_path({"order": {"amount": 0}}, "order.amount") == 0


def test_get_path_non_existent():
    assert get_path({"a": 1}, "b") is None
    assert get_path({"a": {"b": 1}}, "a.c") is None


def test_get_path_through_non_dict():

    assert get_path({"customer": "Anna"}, "customer.fullName") is None


 
def test_set_path_nested_preserves_existing():

    data = {"customer": {"id": 1}}
    result = set_path(data, "customer.name", "Anna")
    assert result == {"customer": {"id": 1, "name": "Anna"}}


def test_set_path_deep_creation():
    assert set_path({}, "a.b.c", 1) == {"a": {"b": {"c": 1}}}


def test_set_path_single_part():
    assert set_path({}, "totalAmount", 99.9) == {"totalAmount": 99.9}



def test_flatten():
    assert flatten({
        "customer": {"fullName": "Anna"},
        "totalAmount": 99.9
    }) == {
        "customer.fullName": "Anna",
        "totalAmount": 99.9
    }