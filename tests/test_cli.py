import cyclopts

from path_extract.cli import app, main


def test_cli_app_is_named_pathex() -> None:
    assert isinstance(app, cyclopts.App)
    assert tuple(app.name) == ("pathex",)


def test_cli_main_prints_greeting(capsys) -> None:
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello from pathex!"
