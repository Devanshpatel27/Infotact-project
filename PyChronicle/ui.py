from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Footer, Header, Label, Static, TextArea

from config import WINDOW_TITLE
from models import ExecutionHistory


class TimelineSlider(Static):
    """A visual timeline slider placeholder; playback is not a Week 2 feature."""

    def __init__(self, frame_count: int) -> None:
        super().__init__(f"0  [--------------------]  {frame_count}", id="timeline")


class PyChronicleApp(App[None]):
    """Week 2 layout only; it intentionally has no playback behavior."""

    TITLE = WINDOW_TITLE
    CSS = """
    Screen { layout: vertical; }
    #code { height: 1fr; border: round $accent; }
    #timeline, #variables, #status { border: round $primary; padding: 1; }
    #variables { height: 7; }
    """

    def __init__(self, source_code: str, history: ExecutionHistory) -> None:
        super().__init__()
        self.source_code = source_code
        self.history = history

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Code View")
        yield TextArea(self.source_code, id="code", read_only=True)
        yield Label("Timeline Slider")
        yield TimelineSlider(len(self.history))
        with VerticalScroll(id="variables"):
            yield Static("Variables\nFrame data will be displayed here.")
        yield Static(f"Status Bar | {len(self.history)} frames recorded", id="status")
        yield Footer()


def main() -> None:
    """Launch the static Week 2 layout using the saved execution history."""
    from config import DATABASE_PATH, TARGET_FILE
    from database import DatabaseManager

    database = DatabaseManager(DATABASE_PATH)
    try:
        PyChronicleApp(TARGET_FILE.read_text(encoding="utf-8"), database.read_frames()).run()
    finally:
        database.close()


if __name__ == "__main__":
    main()
