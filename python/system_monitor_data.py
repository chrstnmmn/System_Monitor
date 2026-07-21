import psutil

while True:
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Utilization: {cpu_usage}%")
    
    
    