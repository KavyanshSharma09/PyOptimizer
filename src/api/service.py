class APIService:
    def __init__(self, optimizer, analyzer):
        self.optimizer = optimizer
        self.analyzer = analyzer

    def fetch_optimized_code(self, code):
        # Analyze the code to determine if it's computation-heavy
        complexity_metrics = self.analyzer.analyze_complexity(code)
        if complexity_metrics['is_heavy']:
            optimized_code = self.optimizer.optimize_code(code)
            return optimized_code
        return code

    def analyze_code(self, code):
        # Analyze the code and return complexity metrics
        return self.analyzer.get_complexity_metrics(code)