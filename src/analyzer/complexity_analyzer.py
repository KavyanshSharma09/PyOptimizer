import ast

class ComplexityAnalyzer:
    def __init__(self, code_string):
        self.code_string = code_string
        self.tree = ast.parse(code_string)

    def analyze_loops(self):
        loop_count = 0
        nested_loops = 0
        is_computation_heavy = False

        for node in ast.walk(self.tree):
            if isinstance(node, (ast.For, ast.While)):
                loop_count += 1
                if any(isinstance(child, (ast.For, ast.While)) for child in ast.walk(node) if child is not node):
                    nested_loops += 1

        if loop_count > 2 or nested_loops > 0:
            is_computation_heavy = True

        return {
            "total_loops": loop_count,
            "nested_loops": nested_loops,
            "is_computation_heavy": is_computation_heavy
        }