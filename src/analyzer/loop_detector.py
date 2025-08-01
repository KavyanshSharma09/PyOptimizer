import ast

class LoopDetector:
    def __init__(self, code_string):
        self.code_string = code_string
        self.tree = ast.parse(code_string)

    def detect_numpy_operations(self):
        numpy_ops = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name) and node.func.value.id == 'np':
                numpy_ops.append(ast.unparse(node))
        return numpy_ops