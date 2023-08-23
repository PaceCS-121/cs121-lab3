import re
import poem_analysis

def test_analysis_counts(capsys):
    outputs = [
        r"(?=.*number)(?=.*characters)(?=.*474)",
        r"(?=.*number)(?=.*words)(?=.*91)",
        r"(?=.*number)(?=.*lines)(?=.*12)",
    ]
    poem_analysis.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out, re.IGNORECASE)

def test_analysis_averages(capsys):
    outputs = [
        r"(?=.*[average|mean])(?=.*word)(?=.*4.2)",
        r"(?=.*[average|mean])(?=.*line)(?=.*[38.5|38.6])",
        r"(?=.*[average|mean])(?=.*number)(?=.*7.5)",
    ]
    poem_analysis.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out, re.IGNORECASE)