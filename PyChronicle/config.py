import os

# ==========================================================

PROJECT_NAME = "PyChronicle"

VERSION = "1.0.0"

AUTHOR = "Devansh Patel"

DESCRIPTION = "AST Powered Time Travel Debugger"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_DIR = os.path.join(BASE_DIR, "logs")

DATABASE_DIR = os.path.join(BASE_DIR, "database")

UI_DIR = os.path.join(BASE_DIR, "ui")

TEMP_DIR = os.path.join(BASE_DIR, "temp")



os.makedirs(LOG_DIR, exist_ok=True)

os.makedirs(DATABASE_DIR, exist_ok=True)

os.makedirs(UI_DIR, exist_ok=True)

os.makedirs(TEMP_DIR, exist_ok=True)



DATABASE_NAME = "history.db"

DATABASE_PATH = os.path.join(DATABASE_DIR, DATABASE_NAME)

TARGET_FILE = "sample.py"
TRACE_LINE = True

TRACE_CALL = True

TRACE_RETURN = True

TRACE_EXCEPTION = True

LOG_FILE = os.path.join(LOG_DIR, "pychronicle.log")


WINDOW_TITLE = "PyChronicle Time Travel Debugger"

WINDOW_WIDTH = 120

WINDOW_HEIGHT = 40


SUCCESS_COLOR = "green"

ERROR_COLOR = "red"

WARNING_COLOR = "yellow"

INFO_COLOR = "cyan"
LINE = "=" * 70

SMALL_LINE = "-" * 70

TABLE_NAME = "execution_history"

EXPORT_JSON = os.path.join(BASE_DIR, "execution_history.json")

EXPORT_CSV = os.path.join(BASE_DIR, "execution_history.csv")

ENCODING = "utf-8"

MINIMUM_PYTHON = (3, 10)

BANNER = f"""
                {PROJECT_NAME}

        AST Powered Time Travel Debugger

Version : {VERSION}

Author  : {AUTHOR}

"""

DEBUG = True

AUTO_COMMIT = True

MAX_HISTORY = 100000

WATCH_VARIABLES = []


IGNORE_VARIABLES = [

    "__builtins__",

    "__loader__",

    "__spec__",

    "__package__",

    "__cached__",

    "__doc__",

    "__name__"

]