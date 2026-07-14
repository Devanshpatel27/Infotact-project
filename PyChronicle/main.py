import os

from ast_parser import ASTParser
from tracer import ExecutionTracer


def banner():

    print("=" * 60)
    print("PyChronicle : AST Powered Time Travel Debugger")
    print("=" * 60)


def main():

    banner()

    target = "sample.py"

    if not os.path.exists(target):

        print("Target file not found.")
        return


    parser = ASTParser(target)

    parser.load_file()

    parser.parse_ast()

    parser.find_assignments()

    print("\n")

   

    tracer = ExecutionTracer()

    tracer.start()

    with open(target, "r", encoding="utf-8") as file:

        code = file.read()

    exec(code, {})

    tracer.stop()

    tracer.show_summary()


if __name__ == "__main__":

    main()