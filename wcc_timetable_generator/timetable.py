from textual.app import App, ComposeResult

from textual import events, on
from textual.containers import Container
from textual.validation import Number
from textual.widgets import Button, Input, Label, DataTable, LoadingIndicator, Pretty

from .algo import Subject, generate_timetable

Jours = ("", "  Monday  ", "  Tuesday  ",
         "  Wednesday  ", "  Thursday  ", "  Friday  ", "  Saturday  ")
hourly = [["8:30 AM-9:30 AM"], ["9:30 AM-10:30 AM"], ["10:30 AM-11:30 AM"], ["11:30 AM-12:30 PM"],
            ["13:30 PM-14:30 PM"], ["14:30 PM-15:30 PM"], ["15:30 PM-16:30 PM"], ["16:30 PM-17:30 PM"]]

row_keys = []


class MyApp(App):
    CSS_PATH = "timetable.css"

    def compose(self) -> ComposeResult:
        yield Label("Time Table", id="title")
        with Container(id="container"):
            with Container(classes="form"):
                yield Label("DBMS")
                yield Input(id="sgbd", placeholder="Hours", validators=[Number(minimum=2, maximum=6)])

            with Container(classes="form"):
                yield Label("System and Network Administration")
                yield Input(id="sysAdmin", placeholder="Hours", validators=[Number(minimum=2, maximum=6)])

            with Container(classes="form"):
                yield Label("Web Development")
                yield Input(id="devWeb", placeholder="Hours", validators=[Number(minimum=2, maximum=6)])

            with Container(classes="form"):
                yield Label("Algorithm")
                yield Input(id="algo", placeholder="Hours", validators=[Number(minimum=2, maximum=6)])

            with Container(classes="form"):
                yield Label("Communitcation")
                yield Input(id="comm", placeholder="Hours", validators=[Number(minimum=2, maximum=6)])

            with Container(classes="form"):
                yield Label("English")
                yield Input(id="ang", placeholder="Hours", validators=[Number(minimum=2, maximum=6)])

        yield Pretty([])
        yield DataTable(id="table")
        with Container(id="btn-container"):
            yield Button("Generate", id="submit")
            yield Button("Quit", id="quit")

    @on(Input.Changed)
    def show_invalid_reasons(self, event: Input.Changed) -> None:
        if not event.validation_result.is_valid:
            self.query_one(Pretty).update(event.validation_result.failure_descriptions)
        else:
            self.query_one(Pretty).update("Everything is fine")

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
        table.zebra_stripes = True
        table.add_columns(*Jours)

    @on(Button.Pressed, "#submit")
    def submit_action(self, event: Button.Pressed) -> None:
        try:
            global hourly
            global row_keys

            heur_sgb = int(self.query_one("#sgbd", Input).value)
            heur_sys = int(self.query_one("#sysAdmin", Input).value)
            heur_dev = int(self.query_one("#devWeb", Input).value)
            heur_algo = int(self.query_one("#algo", Input).value)
            heur_comm = int(self.query_one("#comm", Input).value)
            heur_ang = int(self.query_one("#ang", Input).value)

            hours = [heur_sgb, heur_sys, heur_dev,
                    heur_algo, heur_comm, heur_ang]

            for h in hours:
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

            transposed_timetable = self.transposed(time_table)

            timetable_plus_hourly = [hour + line for hour,
                          line in zip(hourly, transposed_timetable)]

            timetable_plus_hourly.insert(4, []) # add seprator line

            for row_key in row_keys:
                table.remove_row(row_key)

            row_keys = table.add_rows(timetable_plus_hourly)

        except Exception as e_:
            pass
    
    @on(Button.Pressed, "#quit")
    def quit_action(self, event: Button.Pressed):
        exit()


if __name__ == "__main__":
    app = MyApp()
    app.run()
