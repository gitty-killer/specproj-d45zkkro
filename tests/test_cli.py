from app import cli


def test_cli_has_main():
    assert hasattr(cli, 'main')

