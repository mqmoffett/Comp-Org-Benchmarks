import time
def integer_benchmark():
    print("Running Integer Benchmark...")
    start_time = time.time()
    a = 0
    for _ in range(10**10):
        a += 1
    b = 1
    for _ in range(5 * 10**9):
        b *= 1
    c = 1000.0
    for _ in range(2 * 10**9):
        c /= 1.0000001
    end_time = time.time()
    print(f"Integer Benchmark Time: {end_time - start_time:.2f} seconds")
def float_benchmark():
    print("Running Floating Point Benchmark...")
    start_time = time.time()
    a = 1.1
    for _ in range(10**10):
        a += 0.1
    b = 1.1
    for _ in range(5 * 10**9):
        b *= 1.0000001
    c = 1000.0
    for _ in range(2 * 10**9):
        c /= 1.0000001
    end_time = time.time()
    print(f"Floating Point Benchmark Time: {end_time - start_time:.2f} seconds")
if __name__ == "__main__":
    integer_benchmark()
    float_benchmark()
def memory_benchmark():
    print("Running Memory Benchmark...")
    size = 10**7 
    data = [0] * size
    start_time = time.time()
    for i in range(5 * 10**9):
        data[i % size] = i
    for i in range(5 * 10**9):
        val = data[i % size]
    end_time = time.time()
    print(f"Memory Benchmark Time: {end_time - start_time:.2f} seconds")