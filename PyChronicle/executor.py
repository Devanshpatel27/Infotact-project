import ast
from pathlib import Path
from types import CodeType
from typing import Callable

from database import DatabaseManager
from models import ExecutionFrame, ExecutionHistory
from tracer import ExecutionTracer


class ExecutionExecutor:
    """Own target loading, execution, tracing, and validation."""

    def __init__(self, target_file: str | Path, database: DatabaseManager, on_frame: Callable[[ExecutionFrame, int], None] | None = None) -> None:
        self.target_file = Path(target_file).resolve()
        self.database = database
        self.on_frame = on_frame

    def parse(self) -> None:
        """Validate that the target contains valid Python syntax."""
        ast.parse(self.target_file.read_text(encoding="utf-8"), filename=str(self.target_file))

    def compile(self) -> CodeType:
        """Compile the target source without modifying it."""
        return compile(self.target_file.read_text(encoding="utf-8"), str(self.target_file), "exec")

    def execute(self) -> ExecutionHistory:
        """Run the target code and return its complete execution history."""
        tracer = ExecutionTracer(self.database, self.target_file, self.on_frame)
        namespace = {"__name__": "__main__", "__file__": str(self.target_file)}
        self.database.clear_history()
        tracer.start()
        try:
            exec(self.compile(), namespace, namespace)
        except Exception as error:
            raise RuntimeError(f"Target execution failed: {error}") from error
        finally:
            history = tracer.stop()
        self._validate(history)
        return history

    def _validate(self, history: ExecutionHistory) -> None:
        """Ensure all traced frames were persisted without drops."""
        if not history.frames:
            raise RuntimeError("Tracing completed without recording any execution frames.")
        if len(history) != self.database.record_count():
            raise RuntimeError("Trace validation failed: one or more frames were not saved.")
