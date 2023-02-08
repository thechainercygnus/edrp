import pytest
from edrp import Reader


@pytest.fixture
def riches_reader():
    return Reader('/Users/brycej/PycharmProjects/edrp/riches-Sol-Eravate-8AD6399E-A753-11ED-8EB0-7A5D4A549FEC.csv')


@pytest.fixture
def exobiology_reader():
    return Reader('/Users/brycej/PycharmProjects/edrp/exobiology-Sol-Eravate-33EE3D5C-A753-11ED-8534-4C594A549FEC.csv')


def test_riches_reader_init(riches_reader):
    assert type(riches_reader) is Reader


def test_exobiology_reader_init(exobiology_reader):
    assert type(exobiology_reader) is Reader


def test_riches_type(riches_reader):
    assert riches_reader.type == 'riches'


def test_exobiology_type(exobiology_reader):
    assert exobiology_reader.type == 'exobiology'
