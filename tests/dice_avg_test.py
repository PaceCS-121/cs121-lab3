import importlib
import re
import dice_avg

def test_random_input():
    assert 'random' in importlib.sys.modules

def test_dice_avg(capsys):
    dice_avg.main()
    captured = capsys.readouterr()
    results = re.findall("[\\d.]+", captured.out)
    assert len(results) == 1
    result = float(results[0])
    assert 1 <= result <= 6