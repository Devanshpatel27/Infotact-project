from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True, frozen=True)
class VariableState:
    """A variable name and its display-safe captured value."""

    name: str
    value: str


@dataclass(slots=True)
class ExecutionFrame:
    """One traced line and the local state visible at that line."""

    timestamp: datetime
    filename: str
    function_name: str
    line_number: int
    variables: list[VariableState]
    id: int | None = None

    def variable_map(self) -> dict[str, str]:
        return {variable.name: variable.value for variable in self.variables}


@dataclass(slots=True)
class ExecutionHistory:
    """In-memory collection of frames captured during one execution."""

    frames: list[ExecutionFrame] = field(default_factory=list)

    def add(self, frame: ExecutionFrame) -> None:
        self.frames.append(frame)

    def clear(self) -> None:
        self.frames.clear()

    def __len__(self) -> int:
        return len(self.frames)
