import os
import sys
import argparse

project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

from src.analyzer.complexity_analyzer import ComplexityAnalyzer
from src.analyzer.loop_detector import LoopDetector
from src.optimizer.code_optimizer import CodeOptimizer
from src.optimizer.gpu_accelerator import GPUAccelerator

def analyze_file(file_path):
    try:
        with open(file_path, 'r') as file:
            code = file.read()
            
        print(f"\n📂 Analyzing file: {file_path}")
        print("="*50)
        
        analyzer = ComplexityAnalyzer(code)
        analysis = analyzer.analyze_loops()
        print("\n🔍 Complexity Analysis:", analysis)

        detector = LoopDetector(code)
        numpy_ops = detector.detect_numpy_operations()
        print("\n🧪 NumPy Operations:", numpy_ops)

        optimizer = CodeOptimizer(code)
        suggestions = optimizer.suggest_optimizations()
        print("\n🛠️ Optimization Suggestions:", suggestions)

        if analysis["is_computation_heavy"]:
            print("\n⚠️ Program is Computationally Heavy")
            print("\nRecommended optimizations:")
            print("1. 🚀 GPU Acceleration using CuPy")
            print("2. 📊 Vectorization of numpy operations")
            print("3. ⚡ Parallel processing for heavy loops")
            
            print("\n📝 Optimized Code with GPU Acceleration:")
            gpu_code = GPUAccelerator.convert_numpy_to_cupy(code)
            print(gpu_code)
        else:
            print("\n✅ Program is not computationally intensive. No heavy optimizations required.")
            
    except FileNotFoundError:
        print(f"❌ Error: File {file_path} not found")
    except Exception as e:
        print(f"❌ Error analyzing file: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze Python code for computational complexity")
    parser.add_argument("file", help="Path to the Python file to analyze")
    args = parser.parse_args()
    
    analyze_file(args.file)