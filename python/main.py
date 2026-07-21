import psutil

while True:
    cpu_usage = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    
    ram_used_gb = ram.used / (1024 ** 3)
    ram_total_gb = ram.total / (1024 ** 3)
    
    print(f"\rCPU: {cpu_usage}% | RAM: {ram_used_gb:.1f}/{ram_total_gb:.1f}GB      ", end="", flush=True)
    
    
    