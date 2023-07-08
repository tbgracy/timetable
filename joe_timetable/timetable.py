from textual.app import App, ComposeResult

from textual.containers import Container
from textual.widgets import Button, Input, Label, Static


class MyApp(App):
    CSS_PATH = "timetable.css"

    def compose(self) -> ComposeResult:
        yield Label("Time Table", id="title")
        with Container(id="container"):
            with Container(classes="form"):
                yield Label("SGBD")
                yield Input(id="sgbd", placeholder="Heure")

            with Container(classes="form"):
                yield Label("SysAdmin")
                yield Input(id="sysadmin", placeholder="Heure")
 
            with Container(classes="form"):
                yield Label("Dev Web")
                yield Input(id="dHeurevWeb",placeholder="Heure")

            with Container(classes="form"):
                yield Label("Algo")
                yield Input(id="algo", placeholder="Heure")
            
            with Container(classes="form"):
                yield Label("Communitcation")
                yield Input(id="comm", placeholder="Heure")

            with Container(classes="form"):
                yield Label("Anglais")
                yield Input(id="ang", placeholder="Heure")          
        
    
if __name__ == "__main__":
    app = MyApp()
    app.run()
