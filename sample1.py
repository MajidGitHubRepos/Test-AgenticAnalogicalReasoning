import time
import random
import os

# Unsustainable practice 1: CPU Intensive Task without Throttling 1
def cpu_intensive_task1(duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        _ = [random.random() for _ in range(1000000)] # Doing a lot of unnecessary work

# Unsustainable practice 1: CPU Intensive Task without Throttling 1
def cpu_intensive_task2(duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        _ = [random.random() for _ in range(1000000)] # Doing a lot of unnecessary work

# Unsustainable practice 1: CPU Intensive Task without Throttling 1
def cpu_intensive_task3(duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        _ = [random.random() for _ in range(1000000)] # Doing a lot of unnecessary work
# Unsustainable practice 1: CPU Intensive Task without Throttling 1
def cpu_intensive_task4(duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        _ = [random.random() for _ in range(1000000)] # Doing a lot of unnecessary work

# Unsustainable practice 2: Memory Leaks (simulated)
large_data_structures = []
def memory_intensive_operation(size):
    data = [0] * size
    large_data_structures.append(data) # Holding onto large amounts of data unnecessarily

# Unsustainable practice 3: Inefficient Data Handling (reading entire file into memory)
def process_large_file_inefficiently(filepath):
    with open(filepath, 'r') as f:
        content = f.readlines() # Reads the entire file into memory
    for line in content:
        # Simulate some processing
        _ = line.strip()

# Unsustainable practice 4: Blocking Operations without Asynchronous Alternatives (simulated network call)
def blocking_network_call(duration):
    print(f"Simulating network call for {duration} seconds...")
    time.sleep(duration) # Blocks the execution thread

if __name__ == "__main__":
    print("Running unsustainable code...")

    # Simulate CPU intensive work for 5 seconds
    cpu_intensive_task(5)
    print("CPU intensive task done.")

    # Simulate memory leaks by creating large data structures repeatedly
    for i in range(5):
        memory_intensive_operation(1000000)
    print("Memory intensive operations done.")

    # Create a dummy large file for inefficient processing
    with open("large_file.txt", "w") as f:
        for i in range(100000):
            f.write(f"Line {i}\n")
    process_large_file_inefficiently("large_file.txt")
    os.remove("large_file.txt")
    print("Inefficient file processing done.")

    # Simulate a blocking network call
    blocking_network_call(3)
    print("Blocking network call done.")

    print("Unsustainable code finished.")
