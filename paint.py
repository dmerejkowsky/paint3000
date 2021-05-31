import json
from pathlib import Path

MAX_USES = 8


class Paint:
    def __init__(self, json_path):
        self.json_path = json_path
        if not self.json_path.exists():
            self.json_path.write_text("{}")
        with self.json_path.open("r") as f:
            self.data = json.load(f)

    def get_paint_left(self, color, uses):
        if color not in self.data:
            # Make sure it's MAX_USES by default
            self.data[color] = MAX_USES
            with self.json_path.open("w") as f:
                json.dump(self.data, f)
        if uses:
            # Take paint away if uses is set
            self.data[color] = max((self.data[color] - uses, 0))
            with self.json_path.open("w") as f:
                json.dump(self.data, f)
        return self.data[color]

    def generate_report(self):
        self.report_done = False
        self.in_header = True
        self.row_num = 0
        self.report = ""
        while not self.report_done:
            self.get_report_row()
            self.report += "\n"
        return self.report

    def get_report_row(self):
        output = ""
        if self.in_header:
            self.in_header = False
            output = "<color>: <remaining>"
        else:
            colors = list(self.data.keys())
            if self.row_num >= len(colors):
                self.report_done = True
            else:
                color = colors[self.row_num]
                self.row_num += 1
                remaining = self.data[color]
                output = f"{color}: {remaining}"
        self.report += output
        return output
