import psutil

while True:
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"\rCPU Utilization: {cpu_usage}%       ", end="", flush=True)
    
    
    