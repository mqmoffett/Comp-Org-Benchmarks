import time
import os

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
    print(f"Integer Benchmark Time: {time.time() - start_time:.2f} seconds")

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
    print(f"Floating Point Benchmark Time: {time.time() - start_time:.2f} seconds")

def memory_benchmark():
    print("Running Memory Benchmark...")
    size = 10**6 
    data = [0] * size
    start_time = time.time()
    for i in range(5 * 10**9):
        data[i % size] = i
    for i in range(5 * 10**9):
        _ = data[i % size]
    print(f"Memory Benchmark Time: {time.time() - start_time:.2f} seconds")

def disk_benchmark(block_size, label):
    print(f"Running {label}...")
    file_name = "test_file.bin"
    file_size = 10**9  # 1GB
    start_time = time.time()
    
    with open(file_name, "wb") as f:
        for _ in range(file_size // block_size):
            f.write(os.urandom(block_size))
    # Read
    with open(file_name, "rb") as f:
        for _ in range(file_size // block_size):
            f.read(block_size)
    if os.path.exists(file_name):
        os.remove(file_name)
    print(f"{label} Time: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    integer_benchmark()
    float_benchmark()
    memory_benchmark()
    disk_benchmark(100, "Hard Drive Benchmark 1")
    disk_benchmark(10000, "Hard Drive Benchmark 2")