import re

class GPUAccelerator:
    @staticmethod
    def convert_numpy_to_cupy(code_string):
        code_string = re.sub(r'\bimport numpy as np\b', 'import cupy as cp', code_string)
        code_string = re.sub(r'\bnp\.', 'cp.', code_string)
        return code_string