import unittest
from src.optimizer.gpu_accelerator import GPUAccelerator
from src.optimizer.code_optimizer import CodeOptimizer

class TestGPUAccelerator(unittest.TestCase):
    def setUp(self):
        self.gpu_accelerator = GPUAccelerator()

    def test_enable_gpu(self):
        result = self.gpu_accelerator.enable_gpu()
        self.assertTrue(result)

    def test_optimize_with_cupy(self):
        # Assuming we have a mock NumPy array for testing
        import numpy as np
        np_array = np.array([1, 2, 3])
        result = self.gpu_accelerator.optimize_with_cupy(np_array)
        self.assertIsNotNone(result)

class TestCodeOptimizer(unittest.TestCase):
    def setUp(self):
        self.code_optimizer = CodeOptimizer()

    def test_optimize_code(self):
        code = "for i in range(1000): pass"
        optimized_code = self.code_optimizer.optimize_code(code)
        self.assertNotEqual(code, optimized_code)

    def test_get_optimized_version(self):
        code = "for i in range(1000): pass"
        optimized_version = self.code_optimizer.get_optimized_version(code)
        self.assertIsNotNone(optimized_version)

if __name__ == '__main__':
    unittest.main()