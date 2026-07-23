from config import DATABASE_PATH, PROJECT_NAME, TARGET_FILE
from database import DatabaseManager
from executor import ExecutionExecutor
from models import ExecutionFrame
from ui import PyChronicleApp


def print_frame(frame: ExecutionFrame, number: int) -> None:
    """Display one captured execution frame in the terminal."""
    print(f"Frame {number}")
    print(f"Line {frame.line_number}")
    print("Variables")
    if not frame.variables:
        print("None")
    for variable in frame.variables:
        print(f"{variable.name} = {variable.value}")


def main() -> None:
    """Parse, execute, trace, persist, validate, and initialize the Week 2 UI."""
    print(f"{PROJECT_NAME} Started")
    database = DatabaseManager(DATABASE_PATH)
    executor = ExecutionExecutor(TARGET_FILE, database, print_frame)
    try:
        executor.parse()
        print("AST Parsing Completed")
        print("Execution Started")
        history = executor.execute()
        PyChronicleApp(TARGET_FILE.read_text(encoding="utf-8"), history)
        print("Execution Finished")
        print("History Saved")
        print("Database Updated")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    except Exception as error:
        print(f"Execution Error: {error}")
    finally:
        database.close()


if __name__ == "__main__":
    main()
