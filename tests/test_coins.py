import io

from src.homework_day_1.coins import main


def test_main(monkeypatch):

    # В стандартный ввод передадим кол-во монеток
    monkeypatch.setattr('sys.stdin', io.StringIO('1000'))

    main()

    assert 1
