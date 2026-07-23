import contextlib
import io
import tempfile
import time
import unittest
from datetime import datetime
from pathlib import Path

from config import TARGET_FILE
from database import DatabaseManager
from executor import ExecutionExecutor
from models import ExecutionFrame


class WeekTwoValidationTests(unittest.TestCase):
    """Validate Week 2 tracing and storage requirements."""

    def test_complex_loop_has_no_dropped_frames(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            database = DatabaseManager(Path(directory) / "trace.db")
            try:
                executor = ExecutionExecutor(TARGET_FILE, database)
                with contextlib.redirect_stdout(io.StringIO()):
                    executor.parse()
                    history = executor.execute()
                self.assertEqual(len(history), database.record_count())
                self.assertGreaterEqual(len(history), 15)
            finally:
                database.close()

    def test_thousands_of_frames_are_batched_efficiently(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            database = DatabaseManager(Path(directory) / "performance.db")
            frames = [
                ExecutionFrame(datetime.now(), "benchmark.py", "loop", index, [])
                for index in range(2_000)
            ]
            try:
                started = time.perf_counter()
                database.insert_frames(frames)
                elapsed = time.perf_counter() - started
                self.assertEqual(database.record_count(), 2_000)
                self.assertLess(elapsed, 5.0)
            finally:
                database.close()


if __name__ == "__main__":
    unittest.main()
