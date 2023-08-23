import re
import sum_digits

def test_sum_digits_2d(capsys, monkeypatch):
    inputs, output = ("22", "4")
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    sum_digits.main()
    captured = capsys.readouterr()
    assert output in captured.out

def test_sum_digits_3d(capsys, monkeypatch):
    inputs, output = ("456", "15")
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    sum_digits.main()
    captured = capsys.readouterr()
    assert output in captured.out

def test_sum_digits_zero(capsys, monkeypatch):
    inputs, output = ("0", "0")
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    sum_digits.main()
    captured = capsys.readouterr()
    assert output in captured.out

def test_sum_digits_one(capsys, monkeypatch):
    inputs, output = ("10", "1")
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    sum_digits.main()
    captured = capsys.readouterr()
    assert output in captured.out