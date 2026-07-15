"""
============================================================
PyChronicle
Models Module

Author : Devansh Patel

This module contains all data models used by PyChronicle.
============================================================
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any, List


# ==========================================================
# Execution Frame
# ==========================================================

@dataclass
class ExecutionFrame:
    """
    Represents one execution step.
    """

    event: str
    filename: str
    function: str
    line_number: int
    variables: Dict[str, Any]
    timestamp: datetime = field(default_factory=datetime.now)

    def to_dict(self):

        return {
            "event": self.event,
            "filename": self.filename,
            "function": self.function,
            "line_number": self.line_number,
            "variables": self.variables,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }


# ==========================================================
# Variable State
# ==========================================================

@dataclass
class VariableState:
    """
    Represents a single variable.
    """

    name: str
    value: Any
    variable_type: str

    def to_dict(self):

        return {
            "name": self.name,
            "value": repr(self.value),
            "type": self.variable_type
        }


# ==========================================================
# Execution History
# ==========================================================

@dataclass
class ExecutionHistory:
    """
    Stores all execution frames.
    """

    frames: List[ExecutionFrame] = field(default_factory=list)

    def add_frame(self, frame: ExecutionFrame):

        self.frames.append(frame)

    def clear(self):

        self.frames.clear()

    def total_frames(self):

        return len(self.frames)

    def get_frame(self, index):

        if 0 <= index < len(self.frames):

            return self.frames[index]

        return None

    def last_frame(self):

        if self.frames:

            return self.frames[-1]

        return None

    def to_list(self):

        return [

            frame.to_dict()

            for frame in self.frames

        ]


# ==========================================================
# Program Information
# ==========================================================

@dataclass
class ProgramInfo:

    filename: str

    total_lines: int = 0

    total_frames: int = 0

    execution_time: float = 0.0

    status: str = "Ready"

    def summary(self):

        return {

            "filename": self.filename,

            "lines": self.total_lines,

            "frames": self.total_frames,

            "execution_time": self.execution_time,

            "status": self.status

        }


# ==========================================================
# Watch Variable
# ==========================================================

@dataclass
class WatchVariable:

    name: str

    history: List[Any] = field(default_factory=list)

    def update(self, value):

        self.history.append(value)

    def latest(self):

        if self.history:

            return self.history[-1]

        return None

    def clear(self):

        self.history.clear()


# ==========================================================
# Breakpoint
# ==========================================================

@dataclass
class Breakpoint:

    filename: str

    line_number: int

    enabled: bool = True

    def disable(self):

        self.enabled = False

    def enable(self):

        self.enabled = True


# ==========================================================
# Timeline
# ==========================================================

@dataclass
class Timeline:

    current_position: int = 0

    maximum_position: int = 0

    def next(self):

        if self.current_position < self.maximum_position:

            self.current_position += 1

    def previous(self):

        if self.current_position > 0:

            self.current_position -= 1

    def reset(self):

        self.current_position = 0


# ==========================================================
# Application State
# ==========================================================

@dataclass
class ApplicationState:

    running: bool = False

    paused: bool = False

    current_file: str = ""

    current_line: int = 0

    current_function: str = ""

    def reset(self):

        self.running = False

        self.paused = False

        self.current_file = ""

        self.current_line = 0

        self.current_function = ""