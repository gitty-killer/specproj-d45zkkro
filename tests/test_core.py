from app import parse, transform


def test_parse_and_transform():
    assert parse.parse_func_1('x')
    assert transform.transform_func_1('y')

