import psutil
def print_hi(name):
    print(f'Hello, {name}!')

proc = psutil.process_iter()

for process in proc:
    cpu_percentages = process.cpu_percent()
    memory_usage = process.memory_percent()
    print(f"{cpu_percentages}, :::: {memory_usage}")

import os
print(os.getcwd())

print(os.mkdir("testing_data_path"))
import shutil

disku_use =shutil.disk_usage("./")
print(disku_use)
