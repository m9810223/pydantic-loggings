import pytest


@pytest.fixture
def pydantic_classvars_attribute():
    return '__class_vars__'


@pytest.fixture
def get_mocker_name():
    def _get_mocker_name(obj):
        return f'{obj.__module__}.{obj.__name__}'

    return _get_mocker_name
