import ast
import black
import autopep8
from typing import List

class CodeOptimizer:
    def __init__(self, code_string: str):
        self.code_string = code_string

    def format_code(self) -> str:
        try:
            formatted_code = black.format_str(self.code_string, mode=black.FileMode())
            formatted_code = autopep8.fix_code(formatted_code)
            return formatted_code
        except Exception as e:
            return f"Error formatting code: {str(e)}"

    def suggest_optimizations(self) -> List[str]:
        suggestions = []
        tree = ast.parse(self.code_string)

        for node in ast.walk(tree):
            if isinstance(node, ast.For):
                
                if isinstance(node.target, ast.Name) and isinstance(node.iter, ast.Call) and isinstance(node.iter.func, ast.Name) and node.iter.func.id == 'range':
                    suggestions.append(f"Consider using list comprehension for loop at line {node.lineno}")

                
                for child in ast.walk(node):
                    if isinstance(child, ast.Call) and isinstance(child.func, ast.Attribute) and isinstance(child.func.value, ast.Name) and child.func.value.id == 'np':
                        suggestions.append(f"Consider vectorizing numpy operation at line {child.lineno}")

        return suggestions


test_code = """
import numpy as np

def process_data(data):
    results = []
    for i in range(len(data)):
        results.append(np.dot(data[i], data[i]))
    return results

def heavy_computation():
    matrix = np.random.rand(1000, 1000)
    for i in range(100):
        matrix = np.dot(matrix, matrix)
    return matrix
"""

optimizer = CodeOptimizer(test_code)
suggestions = optimizer.suggest_optimizations()
print("\nOptimization Suggestions:")
for suggestion in suggestions:
    print(f"- {suggestion}")
