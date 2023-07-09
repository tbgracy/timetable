from textual.app import App, ComposeResult

from textual import events, on
from textual.containers import Container
from textual.validation import Number
from textual.widgets import Button, Input, Label, DataTable, LoadingIndicator

from algo import Subject, generate_timetable

Jours = ("Horaire/Jours", "  Lundi  ", "  Mardi  ",
         "  Mercredi  ", "  Jeudi  ", "  Vendredi  ", "  Samedi  ")
horaires = [["8h30-9h30"], ["9h30-10h30"], ["10h30-11h30"], ["11h30-12h30"],
            ["12h30-13h30"], ["13h30-14h30"], ["14h30-15h30"], ["15h30-16h30"], ["16h30-17h30"]]

row_keys = []


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
        yield Button("Générer", id="submit")

    @staticmethod
    def transposed(data):
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
            global row_keys

            heur_sgb = int(self.query_one("#sgbd", Input).value)
            heur_sys = int(self.query_one("#sysAdmin", Input).value)
            heur_dev = int(self.query_one("#devWeb", Input).value)
            heur_algo = int(self.query_one("#algo", Input).value)
            heur_comm = int(self.query_one("#comm", Input).value)
            heur_ang = int(self.query_one("#ang", Input).value)

            hour = [heur_sgb, heur_sys, heur_dev,
                    heur_algo, heur_comm, heur_ang]

            for h in hour:
                if not 2 <= h <= 6:
                    raise Exception

            subjects = [
                Subject("SGBD", heur_sgb),
                Subject("SysAdmin", heur_sys),
                Subject("Dev WEB", heur_dev),
                Subject("Algo", heur_algo),
                Subject("Comm", heur_comm),
                Subject("Anglais", heur_ang)
            ]

            time_table = generate_timetable(subjects)

            table = self.query_one("#table", DataTable)

            time_table = [h + line for h,
                          line in zip(horaires, self.transposed(time_table))]

            for row_key in row_keys:
                table.remove_row(row_key)
            row_keys = table.add_rows(time_table)

        except Exception as e_:
            pass


if __name__ == "__main__":
    app = MyApp()
    app.run()
