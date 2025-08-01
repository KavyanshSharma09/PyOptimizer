import unittest
from src.analyzer.complexity_analyzer import ComplexityAnalyzer
from src.analyzer.loop_detector import LoopDetector

class TestComplexityAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = ComplexityAnalyzer()

    def test_analyze_complexity(self):
        code = "for i in range(10): pass"
        result = self.analyzer.analyze_complexity(code)
        self.assertIsInstance(result, dict)

    def test_get_complexity_metrics(self):
        code = "for i in range(10): pass"
        self.analyzer.analyze_complexity(code)
        metrics = self.analyzer.get_complexity_metrics()
        self.assertIn('time_complexity', metrics)

class TestLoopDetector(unittest.TestCase):
    def setUp(self):
        self.detector = LoopDetector()

    def test_detect_loops(self):
        code = "for i in range(10): pass"
        loops = self.detector.detect_loops(code)
        self.assertGreater(len(loops), 0)

    def test_get_loop_count(self):
        code = "for i in range(10): pass\nwhile True: pass"
        self.detector.detect_loops(code)
        count = self.detector.get_loop_count()
        self.assertEqual(count, 2)

if __name__ == '__main__':
    unittest.main()