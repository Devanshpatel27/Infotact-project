"""
============================================================
PyChronicle
Configuration Module

Author : Devansh Patel

This module stores all application configuration.

============================================================
"""

import os

# ==========================================================
# PROJECT INFORMATION
# ==========================================================

PROJECT_NAME = "PyChronicle"

VERSION = "1.0.0"

AUTHOR = "Devansh Patel"

DESCRIPTION = "AST Powered Time Travel Debugger"


# ==========================================================
# PROJECT PATHS
# ==========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_DIR = os.path.join(BASE_DIR, "logs")

DATABASE_DIR = os.path.join(BASE_DIR, "database")

UI_DIR = os.path.join(BASE_DIR, "ui")

TEMP_DIR = os.path.join(BASE_DIR, "temp")


# ==========================================================
# CREATE DIRECTORIES
# ==========================================================

os.makedirs(LOG_DIR, exist_ok=True)

os.makedirs(DATABASE_DIR, exist_ok=True)

os.makedirs(UI_DIR, exist_ok=True)

os.makedirs(TEMP_DIR, exist_ok=True)


# ==========================================================
# DATABASE
# ==========================================================

DATABASE_NAME = "history.db"

DATABASE_PATH = os.path.join(DATABASE_DIR, DATABASE_NAME)


# ==========================================================
# TARGET PROGRAM
# ==========================================================

TARGET_FILE = "sample.py"


# ==========================================================
# TRACE SETTINGS
# ==========================================================

TRACE_LINE = True

TRACE_CALL = True

TRACE_RETURN = True

TRACE_EXCEPTION = True


# ==========================================================
# LOG FILE
# ==========================================================

LOG_FILE = os.path.join(LOG_DIR, "pychronicle.log")


# ==========================================================
# UI SETTINGS
# ==========================================================

WINDOW_TITLE = "PyChronicle Time Travel Debugger"

WINDOW_WIDTH = 120

WINDOW_HEIGHT = 40


# ==========================================================
# COLORS
# ==========================================================

SUCCESS_COLOR = "green"

ERROR_COLOR = "red"

WARNING_COLOR = "yellow"

INFO_COLOR = "cyan"


# ==========================================================
# DISPLAY
# ==========================================================

LINE = "=" * 70

SMALL_LINE = "-" * 70


# ==========================================================
# SQLITE
# ==========================================================

TABLE_NAME = "execution_history"


# ==========================================================
# JSON EXPORT
# ==========================================================

EXPORT_JSON = os.path.join(BASE_DIR, "execution_history.json")


# ==========================================================
# CSV EXPORT
# ==========================================================

EXPORT_CSV = os.path.join(BASE_DIR, "execution_history.csv")


# ==========================================================
# DEFAULT ENCODING
# ==========================================================

ENCODING = "utf-8"


# ==========================================================
# PYTHON VERSION CHECK
# ==========================================================

MINIMUM_PYTHON = (3, 10)


# ==========================================================
# APPLICATION BANNER
# ==========================================================

BANNER = f"""
============================================================
                {PROJECT_NAME}

        AST Powered Time Travel Debugger

Version : {VERSION}

Author  : {AUTHOR}

============================================================
"""


# ==========================================================
# DEBUG MODE
# ==========================================================

DEBUG = True


# ==========================================================
# SQLITE COMMIT INTERVAL
# ==========================================================

AUTO_COMMIT = True


# ==========================================================
# MAX TRACE RECORDS
# ==========================================================

MAX_HISTORY = 100000


# ==========================================================
# WATCH VARIABLES
# ==========================================================

WATCH_VARIABLES = []


# ==========================================================
# IGNORE VARIABLES
# ==========================================================

IGNORE_VARIABLES = [

    "__builtins__",

    "__loader__",

    "__spec__",

    "__package__",

    "__cached__",

    "__doc__",

    "__name__"

]