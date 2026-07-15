"""
============================================================
PyChronicle
Console UI

Author : Devansh Patel

Responsibilities
----------------
1. Display execution history
2. Display execution summary
3. Display variable timeline
4. Future upgrade -> Textual TUI
============================================================
"""

from config import LINE


class ConsoleUI:

    def __init__(self):

        pass

    # -----------------------------------------------------

    def banner(self):

        print(LINE)
        print("           PyChronicle Time Travel Debugger")
        print(LINE)

    # -----------------------------------------------------

    def show_execution(self, history):

        print()
        print(LINE)
        print("EXECUTION HISTORY")
        print(LINE)

        if len(history) == 0:

            print("\nNo execution history found.\n")
            return

        for index, record in enumerate(history, start=1):

            print(f"\nFrame : {index}")

            print("-" * 50)

            print(f"Event      : {record['event']}")

            print(f"Function   : {record['function']}")

            print(f"Line       : {record['line']}")

            print("\nVariables")

            if len(record["variables"]) == 0:

                print("None")

            else:

                for key, value in record["variables"].items():

                    print(f"{key} = {value}")

    # -----------------------------------------------------

    def summary(self, history):

        print()

        print(LINE)

        print("SUMMARY")

        print(LINE)

        print(f"Frames Recorded : {len(history)}")

        print()

    # -----------------------------------------------------

    def variable_timeline(self, history):

        print()

        print(LINE)

        print("VARIABLE TIMELINE")

        print(LINE)

        for record in history:

            print()

            print(f"Line {record['line']}")

            if len(record["variables"]) == 0:

                print("No Variables")

            else:

                for key, value in record["variables"].items():

                    print(f"{key} -> {value}")

    # -----------------------------------------------------

    def line_view(self, history):

        print()

        print(LINE)

        print("LINE EXECUTION")

        print(LINE)

        for record in history:

            print(

                f"Line {record['line']}"

                f" ({record['event']})"

            )

    # -----------------------------------------------------

    def wait(self):

        input("\nPress ENTER to continue...")