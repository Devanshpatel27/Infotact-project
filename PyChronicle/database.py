import json
import sqlite3
from datetime import datetime
from pathlib import Path
from models import ExecutionFrame, ExecutionHistory, VariableState


class DatabaseManager:
    """Store and retrieve traced execution frames in SQLite."""

    TABLE_NAME = "execution_history"
    COLUMNS = ("id", "timestamp", "filename", "function_name", "line_number", "variables")

    def __init__(self, database_path: str | Path) -> None:
        self.connection = sqlite3.connect(database_path)
        self.connection.execute("PRAGMA journal_mode = WAL")
        self.create_table()

    def create_table(self) -> None:
        """Create the Week 2 schema, replacing the incompatible Week 1 schema once."""
        columns = tuple(row[1] for row in self.connection.execute(f"PRAGMA table_info({self.TABLE_NAME})"))
        if columns and columns != self.COLUMNS:
            self.connection.execute(f"DROP TABLE {self.TABLE_NAME}")
        self.connection.execute(

            f"""
            CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                filename TEXT NOT NULL,
                function_name TEXT NOT NULL,
                line_number INTEGER NOT NULL,
                variables TEXT NOT NULL
            )
            """
        )
        self.connection.commit()

    def insert_frames(self, frames: list[ExecutionFrame]) -> None:
        """Insert a batch of captured frames in one transaction."""
        if not frames:
            return
        self.connection.executemany(
            """
            INSERT INTO execution_history
                (timestamp, filename, function_name, line_number, variables)
            VALUES (?, ?, ?, ?, ?)
            """,
            [
                (frame.timestamp.isoformat(timespec="milliseconds"), frame.filename,
                 frame.function_name, frame.line_number,
                 json.dumps(frame.variable_map(), ensure_ascii=False))
                for frame in frames
            ],
        )
        self.connection.commit()

    def read_frames(self) -> ExecutionHistory:
        """Return all saved frames in execution order."""
        frames = []
        query = "SELECT id, timestamp, filename, function_name, line_number, variables FROM execution_history ORDER BY id"
        for row in self.connection.execute(query):
            variables = [VariableState(name, value) for name, value in json.loads(row[5]).items()]
            frames.append(ExecutionFrame(datetime.fromisoformat(row[1]), row[2], row[3], row[4], variables, row[0]))
        return ExecutionHistory(frames)

    def record_count(self) -> int:
        return self.connection.execute("SELECT COUNT(*) FROM execution_history").fetchone()[0]

    def clear_history(self) -> None:
        self.connection.execute("DELETE FROM execution_history")
        self.connection.commit()

    def close(self) -> None:
        self.connection.close()
