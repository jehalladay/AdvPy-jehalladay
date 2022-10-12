import pytest
import import_path
from main import (
    can_finish_adventure
)

test_cases: list = [
    (
        ".$.b.|.t.*.j.................$$$$$bbbbb||....tt.....",
        "YES"
    ),
    (
        ".$.b.|.t.*.j..",
        "YES"
    ),
    (
        "................................",
        "YES"
    ),
    (
        ".......$....$......*....*.....|......t........j...j.....b..b........",
        "YES"
    ),
    (
        "...$.$.$..*..*..*...*..|..*..b.....*******...",
        "NO"
    ),
    (
        "........$b...$$..t...*..*...j.........j...",
        "NO"
    ),
    (
        ".........*****jjjj...............|tj....",
        "YES"
    ),
    (
        ".$.|.*.$.|.*.$.|.*.j.t.b.j.t.b.j.t.b.",
        "YES"
    ),
    (
        "...$$..$$..$$..|..$$..b......b....t..bbbbbb.....j...",
        "NO"
    ),
    (
        "$",
        "NO"
    )
]

@pytest.mark.parametrize('n', list(range(len(test_cases))))
def test_can_finish_adventure(n: int):
    case = test_cases[n]
    assert can_finish_adventure(case[0]) == case[1]
    # for case in test_cases: