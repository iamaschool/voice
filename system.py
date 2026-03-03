import os
import platform
import subprocess
import re
import multiprocessing
import time
import math

def get_cpu_score():
    cores = multiprocessing.cpu_count()
    # CPU benchmark: simple math test
    start = time.time()
    total = 0
    for i in range(5_000_000):
        total += math.sqrt(i)
    end = time.time()
    bench_time = end - start
    core_score = min(cores / 16, 1.0)
    bench_score = min(1 / bench_time, 1.0)
    return (core_score + bench_score) / 2

def get_ram_score():
    try:
        if platform.system() == "Windows":
            output = subprocess.check_output("wmic ComputerSystem get TotalPhysicalMemory", shell=True)
            numbers = re.findall(r"\d+", output.decode())
            ram_gb = int(numbers[0]) / (1024**3)
        elif platform.system() == "Linux":
            with open("/proc/meminfo") as f:
                for line in f:
                    if "MemTotal" in line:
                        ram_gb = int(line.split()[1]) / 1024 / 1024
        elif platform.system() == "Darwin":
            output = subprocess.check_output(["sysctl", "-n", "hw.memsize"])
            ram_gb = int(output.strip()) / (1024**3)
        else:
            ram_gb = 8
    except:
        ram_gb = 8
    return min(ram_gb / 32, 1.0)

def get_gpu_score():
    # Default: no GPU
    gpu_score = 0
    try:
        # NVIDIA check via nvidia-smi
        result = subprocess.check_output("nvidia-smi --query-gpu=memory.total,clocks.max.sm --format=csv,noheader,nounits", shell=True)
        lines = result.decode().strip().split("\n")
        max_score = 0
        for line in lines:
            mem, clock = map(int, line.split(","))
            # Normalize: 24GB VRAM, 2000 MHz max GPU clock
            mem_score = min(mem / 24000, 1.0)
            clock_score = min(clock / 2000, 1.0)
            total = (mem_score + clock_score) / 2
            if total > max_score:
                max_score = total
        gpu_score = max_score
    except Exception as e:
        gpu_score = 0  # No GPU or NVIDIA drivers not installed
    return gpu_score

def rate_system():
    cpu = get_cpu_score()
    ram = get_ram_score()
    gpu = get_gpu_score()
    # Weighted: GPU 70%, CPU 20%, RAM 10%
    final_score = gpu*0.7 + cpu*0.2 + ram*0.1
    return round(final_score * 10, 1)
