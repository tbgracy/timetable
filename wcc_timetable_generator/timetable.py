from textual.app import App, ComposeResult

from textual import events, on
from textual.containers import Container
from textual.validation import Number
from textual.widgets import Button, Input, Label, DataTable, LoadingIndicator

from algo import Subject, generate_timetable

Jours = ("", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi")
horaires = [["8h30 - 10h30"], ["10h45 - 12h45"],
            ["13h30 - 15h30"], ["15h45 - 17h45"]]


class MyApp(App):
    CSS_PATH = "timetable.css"

    def compose(self) -> ComposeResult:
        yield Label("Time Table", id="title")
        with Container(id="container"):
            with Container(classes="form"):
                yield Label("SGBD")
                yield Input(id="sgbd", placeholder="Heure", validators=[Number(minimum=2, maximum=6)])

            with Container(classes="form"):
                yield Label("SysAdmin")
                yield Input(id="sysAdmin", placeholder="Heure", validators=[Number(minimum=2, maximum=6)])

            with Container(classes="form"):
                yield Label("Dev Web")
                yield Input(id="devWeb", placeholder="Heure", validators=[Number(minimum=2, maximum=6)])

            with Container(classes="form"):
                yield Label("Algo")
                yield Input(id="algo", placeholder="Heure", validators=[Number(minimum=2, maximum=6)])

            with Container(classes="form"):
                yield Label("Communitcation")
                yield Input(id="comm", placeholder="Heure", validators=[Number(minimum=2, maximum=6)])

            with Container(classes="form"):
                yield Label("Anglais")
                yield Input(id="ang", placeholder="Heure", validators=[Number(minimum=2, maximum=6)])

        yield DataTable(id="table")
        yield Button("Submit", id="submit")

    def transposed(self, data):
        max_row_length = max(len(row) for row in data)

        transposed_data = []
        for column_index in range(max_row_length):
            transposed_row = []
            for row in data:
                if column_index < len(row):
                    transposed_row.append(row[column_index])
            transposed_data.append(transposed_row)

        return transposed_data

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*Jours)

    @on(Button.Pressed, "#submit")
    def submit_action(self, event: Button.Pressed) -> None:
        try:
            global horaires
            heurs_sgbd = int(self.query_one("#sgbd", Input).value)
            

            subjects = [
                Subject("SGBD", int(self.query_one("#sgbd", Input).value)),
                Subject("SysAdmin", int(
                    self.query_one("#sysAdmin", Input).value)),
                Subject("Dev WEB", int(self.query_one("#devWeb", Input).value)),
                Subject("Algo", int(self.query_one("#algo", Input).value)),
                Subject("Comm", int(self.query_one("#comm", Input).value)),
                Subject("Anglais", int(self.query_one("#ang", Input).value))
            ]

            time_table = generate_timetable(subjects)

            table = self.query_one(DataTable)

            time_table = [h + subjects_in_one_day for h,
                          subjects_in_one_day in zip(horaires, self.transposed(time_table))]

            table.add_rows(time_table)
        except Exception as _e:
            pass


if __name__ == "__main__":
    app = MyApp()
    app.run()
