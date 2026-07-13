import os
from ast_parser import ASTParser

def naneer():
    print("=" * 60)
    print("  pyChronicle - time Travel Debugger")
    print("=" * 60)

    def main():

        banner()

    target_file = "sample.py"

    if not os.path.exists(target_file):
        print(f"[ERROR] {target_file} not found.")
        return

    parser = ASTParser(target_file)

    parser.load_file()

    parser.parse_ast()

    parser.find_assignments()


if __name__ == "__main__":
    main()    

