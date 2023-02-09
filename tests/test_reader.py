import collections.abc
from pathlib import Path
import pytest
from edrp import Reader


DATA_PATH = Path.cwd().joinpath('data')
RICHES_FILENAME = 'riches-Sol-Eravate-8AD6399E-A753-11ED-8EB0-7A5D4A549FEC.csv'
EXOBIOLOGY_FILENAME = 'exobiology-Sol-Eravate-33EE3D5C-A753-11ED-8534-4C594A549FEC.csv'


@pytest.fixture
def riches_reader_str():
    riches_path = str(DATA_PATH.joinpath(RICHES_FILENAME))
    return Reader(riches_path)


@pytest.fixture
def riches_reader_path():
    riches_path = DATA_PATH.joinpath(RICHES_FILENAME)
    return Reader(riches_path)


@pytest.fixture
def exobiology_reader_str():
    exobiology_path = str(DATA_PATH.joinpath(EXOBIOLOGY_FILENAME))
    return Reader(exobiology_path)


@pytest.fixture
def exobiology_reader_path():
    exobiology_path = DATA_PATH.joinpath(EXOBIOLOGY_FILENAME)
    return Reader(exobiology_path)


def test_riches_reader_str_init(riches_reader_str):
    assert type(riches_reader_str) is Reader


def test_riches_reader_path_init(riches_reader_path):
    assert type(riches_reader_path) is Reader


def test_exobiology_reader_str_init(exobiology_reader_str):
    assert type(exobiology_reader_str) is Reader


def test_exobiology_reader_path_init(exobiology_reader_path):
    assert type(exobiology_reader_path) is Reader


@pytest.mark.parametrize("riches_reader", ['riches_reader_str', 'riches_reader_path'])
def test_riches_type(riches_reader, request):
    rr = request.getfixturevalue(riches_reader)
    assert rr.type == 'riches'


@pytest.mark.parametrize("exobiology_reader", ['exobiology_reader_str', 'exobiology_reader_path'])
def test_exobiology_type(exobiology_reader, request):
    er = request.getfixturevalue(exobiology_reader)
    assert er.type == 'exobiology'


@pytest.mark.parametrize("reader", [
    'riches_reader_str',
    'riches_reader_path',
    'exobiology_reader_str',
    'exobiology_reader_path'
])
def test_reader_is_iterable(reader, request):
    reader = request.getfixturevalue(reader)
    assert isinstance(reader, collections.abc.Iterable)
