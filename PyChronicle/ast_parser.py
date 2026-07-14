import ast


class VariableVisitor(ast.NodeVisitor):

    def visit_Assign(self, node):

        for target in node.targets:

            if isinstance(target, ast.Name):

                print("-" * 50)
                print(f"Variable Name : {target.id}")
                print(f"Line Number   : {node.lineno}")

        self.generic_visit(node)


class ASTParser:

    def __init__(self, filename):

        self.filename = filename
        self.source_code = ""
        self.tree = None

    def load_file(self):

        with open(self.filename, "r", encoding="utf-8") as file:
            self.source_code = file.read()

        print("\nSource File Loaded Successfully\n")

    def parse_ast(self):

        self.tree = ast.parse(self.source_code)

        print("AST Generated Successfully\n")

    def find_assignments(self):

        print("Searching Variable Assignments...\n")

        visitor = VariableVisitor()

        visitor.visit(self.tree)