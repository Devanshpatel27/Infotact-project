"""
============================================================
PyChronicle
Main Entry Point

Author : Devansh Patel

Workflow

1. Show Banner
2. Parse AST
3. Execute Program
4. Trace Execution
5. Display Execution History
============================================================
"""

import traceback

from config import (
    BANNER,
    TARGET_FILE,
    LINE
)

from ast_parser import ASTParser
from executor import ProgramExecutor
from ui import ConsoleUI


class PyChronicle:

    def __init__(self):

        self.ui = ConsoleUI()

        self.parser = ASTParser(TARGET_FILE)

        self.executor = ProgramExecutor(TARGET_FILE)

    # ------------------------------------------------------

    def ast_phase(self):

        print(LINE)
        print("STEP 1 : AST ANALYSIS")
        print(LINE)

        self.parser.load_file()

        self.parser.parse_ast()

        self.parser.find_assignments()

    # ------------------------------------------------------

    def execution_phase(self):

        print()

        print(LINE)
        print("STEP 2 : PROGRAM EXECUTION")
        print(LINE)

        self.executor.execute()

    # ------------------------------------------------------

    def ui_phase(self):

        history = self.executor.get_history()

        self.ui.show_execution(history)

        self.ui.summary(history)

        self.ui.variable_timeline(history)

    # ------------------------------------------------------

    def run(self):

        print(BANNER)

        self.ast_phase()

        self.execution_phase()

        self.ui_phase()


# ============================================================

def main():

    try:

        app = PyChronicle()

        app.run()

    except KeyboardInterrupt:

        print("\nProgram Interrupted.")

    except Exception:

        print("\nApplication Error\n")

        traceback.print_exc()


# ============================================================

if __name__ == "__main__":

    main()