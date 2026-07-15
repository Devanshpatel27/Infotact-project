"""
============================================================
PyChronicle
Program Executor

Author : Devansh Patel

Responsibilities
----------------
1. Load the target Python file
2. Compile the source code
3. Execute the program
4. Start/Stop the tracer
5. Handle runtime exceptions
============================================================
"""

import os
import traceback

from tracer import ExecutionTracer


class ProgramExecutor:

    def __init__(self, target_file):

        self.target_file = target_file

        self.tracer = ExecutionTracer()

    # ------------------------------------------------------

    def file_exists(self):

        return os.path.exists(self.target_file)

    # ------------------------------------------------------

    def load_source(self):

        with open(self.target_file, "r", encoding="utf-8") as file:

            return file.read()

    # ------------------------------------------------------

    def compile_source(self, source):

        return compile(

            source,

            self.target_file,

            "exec"

        )

    # ------------------------------------------------------

    def execute(self):

        if not self.file_exists():

            raise FileNotFoundError(

                f"{self.target_file} not found."

            )

        source = self.load_source()

        code = self.compile_source(source)

        namespace = {

            "__name__": "__main__",

            "__file__": self.target_file

        }

        print("\n")

        print("=" * 60)

        print("Program Execution Started")

        print("=" * 60)

        self.tracer.start()

        try:

            exec(code, namespace)

        except Exception:

            print("\n")

            print("=" * 60)

            print("Runtime Exception")

            print("=" * 60)

            traceback.print_exc()

        finally:

            self.tracer.stop()

            self.tracer.summary()

    # ------------------------------------------------------

    def get_history(self):

        return self.tracer.get_history()