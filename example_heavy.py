import numpy as np

def matrix_operations(size):

    matrix_a = np.random.rand(size, size)
    matrix_b = np.random.rand(size, size)
    result = np.zeros((size, size))

  
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    
    for _ in range(100):
        result = np.dot(result, matrix_a)
        result = np.sin(result)
        result = np.exp(result)

    return result

def process_data(data):
    
    results = []
    for item in data:
        processed = np.sin(item) + np.cos(item)
        results.append(processed ** 2)
    return results

if __name__ == "__main__":
    
    size = 1000
    result = matrix_operations(size)
    data = np.random.rand(10000)
    processed = process_data(data)