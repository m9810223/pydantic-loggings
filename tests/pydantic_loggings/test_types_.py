import json
from typing import get_args

import pytest
from hypothesis import HealthCheck
from hypothesis import given
from hypothesis import settings
from hypothesis import strategies as st
from pydantic_loggings import types_


class TestFormatterStylesType:
    @pytest.fixture
    def formatterstylestype(self) -> tuple[str, ...]:
        t = get_args(types_.FormatterStylesType)
        assert all(type(x) == str for x in t)
        return t

    @pytest.mark.parametrize(
        'formatter_styles',
        [
            '%',
            '{',
            '$',
        ],
    )
    def test_formatterstylestype(self, formatter_styles: str, formatterstylestype):
        assert 1 == len(formatter_styles)
        assert formatter_styles in formatterstylestype


class TestStrList:
    @pytest.fixture
    def model_validate_json(self):
        m = types_.StrList.model_validate_json
        return m

    @given(str_list=st.lists(st.text()))
    def test_root(self, str_list: list[str]):
        assert types_.StrList(root=str_list).model_dump() == str_list

    @given(str_list=st.lists(st.text()))
    @settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
    def test_model_validate_jsona(self, str_list: list[str], model_validate_json):
        assert str_list == model_validate_json(json.dumps(str_list)).model_dump()
