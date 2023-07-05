import string
import typing as t

import pytest
from hypothesis import HealthCheck
from hypothesis import given
from hypothesis import settings
from hypothesis import strategies as st
from pydantic_loggings import mixins
from pydantic_settings import BaseSettings
from pytest_mock.plugin import MockerFixture


class TestNameMixin:
    @pytest.fixture
    def cls_factory(self):
        def _cls(name: str):
            class C(mixins.NameMixin, BaseSettings):
                NAME: t.ClassVar[str] = name

            return C

        return _cls

    @given(name=st.text())
    @settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
    def test_namemixin(
        self,
        name: str,
        cls_factory: t.Callable[[str], t.Type[mixins.NameMixin]],
    ):
        cls = cls_factory(name)
        assert cls().NAME == name

    @given(name=st.text())
    @settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
    def test_default(
        self,
        name: str,
        cls_factory: t.Callable[[str], t.Type[mixins.NameMixin]],
    ):
        cls = cls_factory(name)
        obj = cls.default()
        assert obj
        assert isinstance(obj[name], cls)


class TestModelDumpMixin:
    @pytest.fixture
    def cls(self):
        class C(mixins.ModelDumpMixin, BaseSettings):
            ...

        return C

    @pytest.fixture
    def obj(self, cls):
        return cls()

    @given(
        cls_attrs=st.lists(
            st.text(alphabet=string.ascii_lowercase, min_size=1),
            max_size=2,
            unique=True,
        ),
    )
    @settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
    def test_class_dump_kwargs(
        self,
        cls: t.Type[mixins.ModelDumpMixin],
        obj: mixins.ModelDumpMixin,
        mocker: MockerFixture,
        cls_attrs: list[str],
        pydantic_classvars_attribute: str,
    ):
        mocker.patch.object(
            target=cls,
            attribute=pydantic_classvars_attribute,
            new={f'{mixins.ModelDumpMixin.ns_model_dump}{x}' for x in cls_attrs},
        )
        for x in cls_attrs:
            mocker.patch.object(
                target=cls,
                attribute=f'{mixins.ModelDumpMixin.ns_model_dump}{x}',
                create=True,
            )
        assert set(cls_attrs) == set(obj.class_dump_kwargs.keys())

    def test_model_dump(
        self,
        cls: t.Type[mixins.ModelDumpMixin],
        obj: mixins.ModelDumpMixin,
        mocker: MockerFixture,
    ):
        # TODO
        model_dump = mocker.patch.object(target=cls, attribute='model_dump')
        obj.model_dump()
        model_dump.assert_called_once()


class TestByAliasModelDumpMixin:
    @pytest.fixture
    def cls(self):
        class M(mixins.ByAliasModelDumpMixin, BaseSettings):
            ...

        return M

    @pytest.fixture
    def obj(self, cls):
        return cls()

    def test_class_dump_kwargs(
        self,
        cls: t.Type[mixins.ByAliasModelDumpMixin],
        obj: mixins.ByAliasModelDumpMixin,
    ):
        assert obj.class_dump_kwargs['by_alias'] is True


class TestExcludeNoneModelDumpMixin:
    @pytest.fixture
    def cls(self):
        class M(mixins.ExcludeNoneModelDumpMixin, BaseSettings):
            ...

        return M

    @pytest.fixture
    def obj(self, cls):
        return cls()

    def test_class_dump_kwargs(
        self,
        cls: t.Type[mixins.ExcludeNoneModelDumpMixin],
        obj: mixins.ExcludeNoneModelDumpMixin,
    ):
        assert obj.class_dump_kwargs['exclude_none'] is True


class TestModelDumpJsonMixin:
    @pytest.fixture
    def cls(self):
        class C(mixins.ModelDumpJsonMixin, BaseSettings):
            ...

        return C

    @pytest.fixture
    def obj(self, cls):
        return cls()

    @given(
        cls_attrs=st.lists(
            st.text(alphabet=string.ascii_lowercase, min_size=1),
            max_size=2,
            unique=True,
        ),
    )
    @settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
    def test_class_dump_json_kwargs(
        self,
        cls: t.Type[mixins.ModelDumpJsonMixin],
        obj: mixins.ModelDumpJsonMixin,
        mocker: MockerFixture,
        cls_attrs: list[str],
        pydantic_classvars_attribute: str,
    ):
        mocker.patch.object(
            target=cls,
            attribute=pydantic_classvars_attribute,
            new={
                f'{mixins.ModelDumpJsonMixin.ns_model_dump_json}{x}' for x in cls_attrs
            },
        )
        for x in cls_attrs:
            mocker.patch.object(
                target=cls,
                attribute=f'{mixins.ModelDumpJsonMixin.ns_model_dump_json}{x}',
                create=True,
            )
        assert set(cls_attrs) == set(obj.class_dump_json_kwargs.keys())

    def test_model_dump_json(
        self,
        cls: t.Type[mixins.ModelDumpJsonMixin],
        obj: mixins.ModelDumpJsonMixin,
        mocker: MockerFixture,
    ):
        # TODO
        model_dump_json = mocker.patch.object(target=cls, attribute='model_dump_json')
        obj.model_dump_json()
        model_dump_json.assert_called_once()


class TestDoNotEnsureAsciiModelDumpJsonModel:
    @pytest.fixture
    def cls(self):
        class M(mixins.DoNotEnsureAsciiModelDumpJsonModel, BaseSettings):
            ...

        return M

    @pytest.fixture
    def obj(self, cls):
        return cls()

    def test_class_dump_kwargs(
        self,
        cls: t.Type[mixins.DoNotEnsureAsciiModelDumpJsonModel],
        obj: mixins.DoNotEnsureAsciiModelDumpJsonModel,
    ):
        assert obj.class_dump_json_kwargs['ensure_ascii'] is False


class TestIndent2ModelDumpJsonModel:
    @pytest.fixture
    def cls(self):
        class M(mixins.Indent2ModelDumpJsonModel, BaseSettings):
            ...

        return M

    @pytest.fixture
    def obj(self, cls):
        return cls()

    def test_class_dump_kwargs(
        self,
        cls: t.Type[mixins.Indent2ModelDumpJsonModel],
        obj: mixins.Indent2ModelDumpJsonModel,
    ):
        assert obj.class_dump_json_kwargs['indent'] == 2
