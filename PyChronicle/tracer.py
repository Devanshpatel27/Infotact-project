import sys
from datetime import datetime
from pathlib import Path
from types import FrameType
from typing import Callable

from config import IGNORED_VARIABLES, TRACE_BATCH_SIZE
from database import DatabaseManager
from models import ExecutionFrame, ExecutionHistory, VariableState

FrameCallback = Callable[[ExecutionFrame, int], None]


class ExecutionTracer:
    """Capture every line event from one target Python file."""

    def __init__(self, database: DatabaseManager, target_file: str | Path, on_frame: FrameCallback | None = None) -> None:
        self.database = database
        self.target_file = Path(target_file).resolve()
        self.on_frame = on_frame
        self.history = ExecutionHistory()
        self._buffer: list[ExecutionFrame] = []
        self.enabled = False

    def start(self) -> None:
        self.history.clear()
        self._buffer.clear()
        self.enabled = True
        sys.settrace(self.trace)

    def stop(self) -> ExecutionHistory:
        sys.settrace(None)
        self.enabled = False
        self.flush()
        return self.history

    def trace(self, frame: FrameType, event: str, argument: object):
        if event == "line" and self.enabled and self._is_target(frame):
            self._record(frame)
        return self.trace

    def flush(self) -> None:
        self.database.insert_frames(self._buffer)
        self._buffer.clear()

    def _is_target(self, frame: FrameType) -> bool:
        return Path(frame.f_code.co_filename).resolve() == self.target_file

    def _record(self, frame: FrameType) -> None:
        variables = [VariableState(name, repr(value)) for name, value in frame.f_locals.items() if name not in IGNORED_VARIABLES]
        record = ExecutionFrame(datetime.now(), frame.f_code.co_filename, frame.f_code.co_name, frame.f_lineno, variables)
        self.history.add(record)
        self._buffer.append(record)
        if self.on_frame:
            self.on_frame(record, len(self.history))
        if len(self._buffer) >= TRACE_BATCH_SIZE:
            self.flush()
