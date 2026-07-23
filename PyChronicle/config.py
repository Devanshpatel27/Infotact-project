from pathlib import Path

PROJECT_NAME = "PyChronicle"
VERSION = "0.2.0"
WINDOW_TITLE = f"{PROJECT_NAME} - Time Travel Debugger"
BANNER = "PyChronicle - Python Execution History"
LINE = "=" * 60
BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "history.db"
DATABASE_NAME = "history.db"
TARGET_FILE = BASE_DIR / "sample.py"
TRACE_BATCH_SIZE = 250
IGNORED_VARIABLES = {"__builtins__", "__file__", "__name__"}
