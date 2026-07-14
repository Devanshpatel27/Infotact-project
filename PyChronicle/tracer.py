import sys


class ExecutionTracer:

    def __init__(self):
        self.execution_history = []

    def trace_function(self, frame, event, arg):

        # Only trace executed lines
        if event == "line":

            filename = frame.f_code.co_filename
            function_name = frame.f_code.co_name
            line_number = frame.f_lineno

            # Copy all local variables
            variables = frame.f_locals.copy()

            print("=" * 60)
            print(f"File      : {filename}")
            print(f"Function  : {function_name}")
            print(f"Line      : {line_number}")
            print("Variables :")

            if variables:
                for key, value in variables.items():
                    print(f"   {key} = {value}")
            else:
                print("   No Variables")

            # Save history
            self.execution_history.append({
                "file": filename,
                "function": function_name,
                "line": line_number,
                "variables": variables
            })

        return self.trace_function

    def start(self):

        sys.settrace(self.trace_function)

    def stop(self):

        sys.settrace(None)

    def show_summary(self):

        print("\n")
        print("=" * 60)
        print("Execution Summary")
        print("=" * 60)

        print(f"Total Frames : {len(self.execution_history)}")