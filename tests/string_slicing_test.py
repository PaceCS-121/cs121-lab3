import string_slicing
import re

def test_string_slicing_fml_hw(capsys, monkeypatch):
    inputs = "Hello Worlds"
    outputs = [
        r"(?=.*first)(?=.*H)",
        r"(?=.*middle)(?=.*W)",
        r"(?=.*last)(?=.*s)",
    ]
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    string_slicing.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out, re.IGNORECASE)

def test_string_slicing_fml_ts(capsys, monkeypatch):
    inputs = "test string"
    outputs = [
        r"(?=.*first)(?=.*t)",
        r"(?=.*middle)(?=.*s)",
        r"(?=.*last)(?=.*g)",
    ]
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    string_slicing.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out, re.IGNORECASE)

def test_string_slicing_reverse_hw(capsys, monkeypatch):
    inputs = "Hello Worlds"
    outputs = [
        "Worlds Hello",
        "sdlroW olleH",
    ]
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    string_slicing.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out, re.IGNORECASE)

def test_string_slicing_reverse_ts(capsys, monkeypatch):
    inputs = "test string"
    outputs = [
        "string test",
        "gnirts tset",
    ]
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    string_slicing.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out, re.IGNORECASE)

def test_string_slicing_skip_hw(capsys, monkeypatch):
    inputs = "Hello Worlds"
    outputs = [
        "el ols",
        "H W",
    ]
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    string_slicing.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out, re.IGNORECASE)

def test_string_slicing_skip_ts(capsys, monkeypatch):
    inputs = "test string"
    outputs = [
        "etsrn",
        "t s",
    ]
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    string_slicing.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out, re.IGNORECASE)