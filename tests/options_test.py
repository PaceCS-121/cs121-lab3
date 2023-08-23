import re
import options

def test_added_options(capsys):
    outputs = [
        r"(?=.*y)(?=.*yes)",
        r"(?=.*n)(?=.*no)",
        r"(?=.*m)(?=.*maybe)",
        r"(?=.*p)(?=.*prefer not to answer)",
    ]
    options.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out, re.IGNORECASE)

def tests_print_options(capsys):
    output = "y: yes\\nn: no\\nm: maybe\\np: prefer not to answer"
    options.main()
    captured = capsys.readouterr()
    assert re.search(output, captured.out, re.IGNORECASE)

def tests_options_newoptions():
    varnames = options.main.__code__.co_varnames
    assert 'new_options' in varnames