from paint import Paint
import textwrap
from pathlib import Path


def test_rendering_a_report():
    json_path = Path("test.json")
    if json_path.exists():
        json_path.unlink()
    paint = Paint(json_path)
    paint.get_paint_left("blue", 1)
    paint.get_paint_left("red", 2)
    paint.get_paint_left("green", 3)
    expected = "<color>: <remaining>\nblue: 7\nred: 6\ngreen: 5\n\n"
    actual = paint.generate_report()
    assert actual == expected
